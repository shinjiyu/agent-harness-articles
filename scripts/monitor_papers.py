#!/usr/bin/env python3
"""Monitor new papers from the same public APIs as Paper Trends.

Sources (host_permissions parity):
  - export.arxiv.org
  - api.crossref.org
  - api.semanticscholar.org
  - dblp.org
  - eutils.ncbi.nlm.nih.gov (PubMed; optional)

Usage:
  python scripts/monitor_papers.py
  python scripts/monitor_papers.py --sources arxiv,crossref
  python scripts/monitor_papers.py --dry-run

Writes:
  indexes/agent-harness/watchlist.json   # rolling candidate inbox
  indexes/agent-harness/inbox/YYYY-MM-DD.json  # daily snapshot
"""

from __future__ import annotations

import html as html_lib
import argparse
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
INDEX_DIR = ROOT / "indexes" / "agent-harness"
INDEX_PATH = INDEX_DIR / "index.json"
MONITOR_PATH = INDEX_DIR / "monitor.json"
WATCHLIST_PATH = INDEX_DIR / "watchlist.json"
INBOX_DIR = INDEX_DIR / "inbox"

TZ = timezone(timedelta(hours=8))
UA = "agent-harness-articles/0.1 (github.com/shinjiyu/agent-harness-articles; research monitor)"
ARXIV_ATOM = "{http://www.w3.org/2005/Atom}"
ARXIV_NS = "{http://arxiv.org/schemas/atom}"


def now_iso() -> str:
    return datetime.now(TZ).replace(microsecond=0).isoformat()


def today_str() -> str:
    return datetime.now(TZ).strftime("%Y-%m-%d")


def http_get(url: str, timeout: int = 45, retries: int = 4) -> bytes:
    """GET with backoff for 429/5xx (arxiv is strict about burst traffic)."""
    last_err: Exception | None = None
    for attempt in range(retries):
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read()
        except urllib.error.HTTPError as e:
            last_err = e
            if e.code in (429, 500, 502, 503, 504) and attempt < retries - 1:
                wait = 8 * (attempt + 1)
                print(f"  HTTP {e.code}, retry in {wait}s ...")
                time.sleep(wait)
                continue
            raise
        except urllib.error.URLError as e:
            last_err = e
            if attempt < retries - 1:
                wait = 5 * (attempt + 1)
                print(f"  network error ({e}), retry in {wait}s ...")
                time.sleep(wait)
                continue
            raise
    raise last_err or RuntimeError(f"failed GET {url}")


def http_get_json(url: str, timeout: int = 45) -> Any:
    raw = http_get(url, timeout=timeout)
    return json.loads(raw.decode("utf-8"))


def normalize_arxiv_id(value: str) -> str:
    """Strip URL/version → bare id like 2607.06906."""
    v = value.strip()
    v = re.sub(r"^https?://arxiv\.org/(abs|pdf)/", "", v)
    v = re.sub(r"\.pdf$", "", v)
    v = re.sub(r"v\d+$", "", v)
    return v


def normalize_title(title: str) -> str:
    t = title.lower().strip()
    t = re.sub(r"\s+", " ", t)
    t = re.sub(r"[^\w\s]", "", t)
    return t


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def existing_keys(index: dict, watchlist: dict) -> set[str]:
    keys: set[str] = set()
    for p in index.get("papers", []):
        if p.get("arxiv_id"):
            keys.add(f"arxiv:{normalize_arxiv_id(p['arxiv_id'])}")
        if p.get("title"):
            keys.add(f"title:{normalize_title(p['title'])}")
        for ext in p.get("external_ids", []) if isinstance(p.get("external_ids"), list) else []:
            keys.add(str(ext).lower())
    for c in watchlist.get("candidates", []):
        if c.get("arxiv_id"):
            keys.add(f"arxiv:{normalize_arxiv_id(c['arxiv_id'])}")
        if c.get("title"):
            keys.add(f"title:{normalize_title(c['title'])}")
        for ext in c.get("external_ids", []):
            keys.add(str(ext).lower())
        if c.get("doi"):
            keys.add(f"doi:{c['doi'].lower()}")
    return keys


def candidate_keys(c: dict) -> set[str]:
    keys: set[str] = set()
    if c.get("arxiv_id"):
        keys.add(f"arxiv:{normalize_arxiv_id(c['arxiv_id'])}")
    if c.get("title"):
        keys.add(f"title:{normalize_title(c['title'])}")
    if c.get("doi"):
        keys.add(f"doi:{str(c['doi']).lower()}")
    for ext in c.get("external_ids", []):
        keys.add(str(ext).lower())
    return keys


# ---------- sources ----------


def fetch_arxiv(keyword: str, max_results: int, sort_by: str, sort_order: str) -> list[dict]:
    # Paper Trends-style: keyword search over all fields
    q = f"all:{keyword}"
    params = {
        "search_query": q,
        "start": 0,
        "max_results": max_results,
        "sortBy": sort_by,
        "sortOrder": sort_order,
    }
    url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode(params)
    raw = http_get(url)
    root = ET.fromstring(raw)
    out: list[dict] = []
    for entry in root.findall(f"{ARXIV_ATOM}entry"):
        id_url = (entry.findtext(f"{ARXIV_ATOM}id") or "").strip()
        arxiv_id = normalize_arxiv_id(id_url.split("/abs/")[-1] if "/abs/" in id_url else id_url)
        version_m = re.search(r"(v\d+)$", id_url)
        published = (entry.findtext(f"{ARXIV_ATOM}published") or "")[:10]
        authors = [
            (a.findtext(f"{ARXIV_ATOM}name") or "").strip()
            for a in entry.findall(f"{ARXIV_ATOM}author")
        ]
        authors = [a for a in authors if a]
        abstract = (entry.findtext(f"{ARXIV_ATOM}summary") or "").strip()
        abstract = re.sub(r"\s+", " ", abstract)
        title = re.sub(r"\s+", " ", (entry.findtext(f"{ARXIV_ATOM}title") or "").strip())
        out.append(
            {
                "source": "arxiv",
                "arxiv_id": arxiv_id,
                "arxiv_version": version_m.group(1) if version_m else "",
                "title": title,
                "authors": authors,
                "published": published,
                "url": f"https://arxiv.org/abs/{arxiv_id}",
                "abstract": abstract,
                "matched_keyword": keyword,
                "external_ids": [f"arxiv:{arxiv_id}"],
            }
        )
    return out


def fetch_crossref(keyword: str, rows: int) -> list[dict]:
    params = {
        "query": keyword,
        "rows": rows,
        "sort": "published",
        "order": "desc",
        "mailto": "agent-harness-articles@users.noreply.github.com",
    }
    url = "https://api.crossref.org/works?" + urllib.parse.urlencode(params)
    data = http_get_json(url)
    items = data.get("message", {}).get("items", [])
    out: list[dict] = []
    for it in items:
        title_list = it.get("title") or []
        title = title_list[0] if title_list else ""
        if not title:
            continue
        authors = []
        for a in it.get("author") or []:
            name = " ".join(x for x in [a.get("given"), a.get("family")] if x)
            if name:
                authors.append(name)
        date_parts = (it.get("published-print") or it.get("published-online") or it.get("created") or {}).get(
            "date-parts", [[]]
        )
        parts = date_parts[0] if date_parts else []
        published = "-".join(f"{p:02d}" if i else str(p) for i, p in enumerate(parts[:3])) if parts else ""
        doi = it.get("DOI") or ""
        arxiv_id = ""
        for xid in it.get("alternative-id") or []:
            if re.match(r"^\d{4}\.\d{4,5}", str(xid)):
                arxiv_id = normalize_arxiv_id(str(xid))
        out.append(
            {
                "source": "crossref",
                "arxiv_id": arxiv_id,
                "doi": doi,
                "title": re.sub(r"\s+", " ", title.strip()),
                "authors": authors,
                "published": published,
                "url": f"https://doi.org/{doi}" if doi else (it.get("URL") or ""),
                "abstract": re.sub(r"<[^>]+>", "", it.get("abstract") or ""),
                "matched_keyword": keyword,
                "external_ids": ([f"doi:{doi.lower()}"] if doi else [])
                + ([f"arxiv:{arxiv_id}"] if arxiv_id else []),
            }
        )
    return out


def fetch_semanticscholar(keyword: str, limit: int, fields: str) -> list[dict]:
    params = {
        "query": keyword,
        "limit": limit,
        "fields": fields,
    }
    url = "https://api.semanticscholar.org/graph/v1/paper/search?" + urllib.parse.urlencode(params)
    try:
        data = http_get_json(url)
    except urllib.error.HTTPError as e:
        if e.code in (429, 403):
            print(f"[semanticscholar] skip ({e.code}) for {keyword!r}")
            return []
        raise
    out: list[dict] = []
    for it in data.get("data") or []:
        title = (it.get("title") or "").strip()
        if not title:
            continue
        ext = it.get("externalIds") or {}
        arxiv_id = normalize_arxiv_id(ext["ArXiv"]) if ext.get("ArXiv") else ""
        doi = ext.get("DOI") or ""
        authors = [a.get("name") for a in (it.get("authors") or []) if a.get("name")]
        published = (it.get("publicationDate") or "")[:10]
        if not published and it.get("year"):
            published = str(it["year"])
        external_ids = [f"s2:{it.get('paperId')}"] if it.get("paperId") else []
        if arxiv_id:
            external_ids.append(f"arxiv:{arxiv_id}")
        if doi:
            external_ids.append(f"doi:{doi.lower()}")
        out.append(
            {
                "source": "semanticscholar",
                "arxiv_id": arxiv_id,
                "doi": doi,
                "title": re.sub(r"\s+", " ", title),
                "authors": authors,
                "published": published,
                "url": it.get("url")
                or (f"https://arxiv.org/abs/{arxiv_id}" if arxiv_id else "")
                or (f"https://doi.org/{doi}" if doi else ""),
                "abstract": (it.get("abstract") or "").strip(),
                "matched_keyword": keyword,
                "external_ids": external_ids,
            }
        )
    return out


def fetch_dblp(keyword: str, max_results: int) -> list[dict]:
    params = {"q": keyword, "format": "json", "h": max_results}
    url = "https://dblp.org/search/publ/api?" + urllib.parse.urlencode(params)
    data = http_get_json(url)
    hits = (((data.get("result") or {}).get("hits") or {}).get("hit")) or []
    out: list[dict] = []
    for hit in hits:
        info = hit.get("info") or {}
        title = (info.get("title") or "").strip().rstrip(".")
        title = html_lib.unescape(title)
        if not title:
            continue
        authors_raw = info.get("authors", {}).get("author", [])
        if isinstance(authors_raw, dict):
            authors_raw = [authors_raw]
        authors = []
        for a in authors_raw:
            if isinstance(a, dict):
                authors.append(a.get("text") or a.get("@pid") or "")
            else:
                authors.append(str(a))
        authors = [a for a in authors if a]
        year = str(info.get("year") or "")
        ee = info.get("ee") or info.get("url") or ""
        if isinstance(ee, list):
            ee = ee[0] if ee else ""
        arxiv_id = ""
        if "arxiv.org" in str(ee):
            arxiv_id = normalize_arxiv_id(str(ee))
        out.append(
            {
                "source": "dblp",
                "arxiv_id": arxiv_id,
                "title": re.sub(r"\s+", " ", title),
                "authors": authors,
                "published": year,
                "url": str(ee),
                "abstract": "",
                "matched_keyword": keyword,
                "external_ids": ([f"arxiv:{arxiv_id}"] if arxiv_id else [])
                + ([f"dblp:{hit.get('@id')}"] if hit.get("@id") else []),
            }
        )
    return out


def fetch_pubmed(keyword: str, max_results: int) -> list[dict]:
    # ESearch → ESummary (same family as Paper Trends host permission)
    search_params = {
        "db": "pubmed",
        "term": keyword,
        "retmax": max_results,
        "sort": "pub+date",
        "retmode": "json",
    }
    search_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?" + urllib.parse.urlencode(
        search_params
    )
    search = http_get_json(search_url)
    ids = (search.get("esearchresult") or {}).get("idlist") or []
    if not ids:
        return []
    time.sleep(0.35)
    sum_params = {"db": "pubmed", "id": ",".join(ids), "retmode": "json"}
    sum_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?" + urllib.parse.urlencode(
        sum_params
    )
    summary = http_get_json(sum_url)
    result = summary.get("result") or {}
    out: list[dict] = []
    for pid in ids:
        it = result.get(pid) or {}
        title = (it.get("title") or "").strip()
        if not title:
            continue
        authors = [a.get("name") for a in (it.get("authors") or []) if a.get("name")]
        published = (it.get("pubdate") or "")[:10].replace("/", "-")
        out.append(
            {
                "source": "pubmed",
                "arxiv_id": "",
                "title": re.sub(r"\s+", " ", title),
                "authors": authors,
                "published": published,
                "url": f"https://pubmed.ncbi.nlm.nih.gov/{pid}/",
                "abstract": "",
                "matched_keyword": keyword,
                "external_ids": [f"pubmed:{pid}"],
            }
        )
    return out


SOURCE_FETCHERS = {
    "arxiv": lambda cfg, kw: fetch_arxiv(
        kw,
        cfg.get("max_results_per_keyword", 20),
        cfg.get("sort_by", "submittedDate"),
        cfg.get("sort_order", "descending"),
    ),
    "crossref": lambda cfg, kw: fetch_crossref(kw, cfg.get("max_results_per_keyword", cfg.get("rows", 10))),
    "semanticscholar": lambda cfg, kw: fetch_semanticscholar(
        kw,
        cfg.get("max_results_per_keyword", 10),
        cfg.get(
            "fields",
            "paperId,externalIds,title,authors,abstract,publicationDate,url,year",
        ),
    ),
    "dblp": lambda cfg, kw: fetch_dblp(kw, cfg.get("max_results_per_keyword", 10)),
    "pubmed": lambda cfg, kw: fetch_pubmed(kw, cfg.get("max_results_per_keyword", 10)),
}


def parse_year(published: str) -> int | None:
    if not published:
        return None
    m = re.match(r"^(\d{4})", published.strip())
    if not m:
        return None
    y = int(m.group(1))
    # reject absurd future OCR/parse junk from Crossref
    if y < 1990 or y > datetime.now(TZ).year + 1:
        return None
    return y


def is_relevant(c: dict, cfg: dict) -> bool:
    min_year = int(cfg.get("min_year") or 0)
    max_year = int(cfg.get("max_year") or (datetime.now(TZ).year + 1))
    year = parse_year(c.get("published") or "")
    if year is not None and (year < min_year or year > max_year):
        return False
    if min_year and year is None and c.get("source") != "arxiv":
        # keep undated arxiv; drop undated crossref/dblp noise
        return False

    needles = [n.lower() for n in (cfg.get("title_must_match_any") or [])]
    if not needles:
        return True
    blob = f"{c.get('title', '')} {c.get('abstract', '')}".lower()
    return any(n in blob for n in needles)


def merge_candidates(raw: list[dict]) -> list[dict]:
    """Collapse duplicates across sources; prefer arxiv record."""
    buckets: dict[str, dict] = {}
    source_rank = {"arxiv": 0, "semanticscholar": 1, "crossref": 2, "dblp": 3, "pubmed": 4}

    def key_for(c: dict) -> str:
        if c.get("arxiv_id"):
            return f"arxiv:{normalize_arxiv_id(c['arxiv_id'])}"
        if c.get("doi"):
            return f"doi:{c['doi'].lower()}"
        return f"title:{normalize_title(c.get('title', ''))}"

    for c in raw:
        k = key_for(c)
        if not c.get("title"):
            continue
        if k not in buckets:
            buckets[k] = dict(c)
            buckets[k]["sources"] = [c["source"]]
            buckets[k]["matched_keywords"] = [c.get("matched_keyword")] if c.get("matched_keyword") else []
            continue
        cur = buckets[k]
        if c["source"] not in cur["sources"]:
            cur["sources"].append(c["source"])
        mk = c.get("matched_keyword")
        if mk and mk not in cur["matched_keywords"]:
            cur["matched_keywords"].append(mk)
        # prefer richer fields / higher-ranked source
        if source_rank.get(c["source"], 9) < source_rank.get(cur.get("source"), 9):
            for field in ("abstract", "authors", "url", "published", "arxiv_id", "doi", "arxiv_version"):
                if c.get(field) and (not cur.get(field) or field in ("arxiv_id", "url", "source")):
                    cur[field] = c[field]
            cur["source"] = c["source"]
        else:
            for field in ("abstract", "authors", "url", "published", "arxiv_id", "doi"):
                if not cur.get(field) and c.get(field):
                    cur[field] = c[field]
        # union external ids
        ids = set(cur.get("external_ids") or [])
        ids.update(c.get("external_ids") or [])
        cur["external_ids"] = sorted(ids)

    merged = list(buckets.values())
    merged.sort(key=lambda x: x.get("published") or "", reverse=True)
    return merged


def run(sources_filter: list[str] | None, dry_run: bool) -> int:
    cfg = load_json(MONITOR_PATH, {})
    index = load_json(INDEX_PATH, {"papers": []})
    watchlist = load_json(
        WATCHLIST_PATH,
        {
            "schema_version": 1,
            "topic": cfg.get("topic", "agent harness"),
            "updated_at": "",
            "candidates": [],
        },
    )

    keywords = cfg.get("keywords") or ["agent harness"]
    source_cfg = cfg.get("sources") or {}
    known = existing_keys(index, watchlist)

    raw: list[dict] = []
    enabled_sources = []
    for name, fetcher in SOURCE_FETCHERS.items():
        sc = source_cfg.get(name) or {}
        if sources_filter is not None:
            if name not in sources_filter:
                continue
        elif not sc.get("enabled", False):
            continue
        enabled_sources.append(name)
        for kw in keywords:
            try:
                print(f"[{name}] querying {kw!r} ...")
                batch = fetcher(sc, kw)
                print(f"[{name}] {len(batch)} hits")
                raw.extend(batch)
                # arxiv ~3s; S2 is rate-limit sensitive
                delay = {"arxiv": 3.2, "semanticscholar": 1.5}.get(name, 0.6)
                time.sleep(delay)
            except Exception as e:
                print(f"[{name}] ERROR for {kw!r}: {e}")

    merged = merge_candidates(raw)
    merged = [c for c in merged if is_relevant(c, cfg)]
    new_items: list[dict] = []
    for c in merged:
        keys = candidate_keys(c)
        if keys & known:
            continue
        item = {
            **c,
            "status": "new",
            "first_seen_at": now_iso(),
            "last_seen_at": now_iso(),
        }
        # cleanup helper fields not needed long-term
        item.pop("matched_keyword", None)
        if item.get("arxiv_id"):
            item["url"] = f"https://arxiv.org/abs/{normalize_arxiv_id(item['arxiv_id'])}"
        new_items.append(item)
        known |= keys

    # refresh last_seen for already-watched that reappear
    by_key = {}
    for c in watchlist.get("candidates", []):
        for k in candidate_keys(c):
            by_key[k] = c
    for c in merged:
        for k in candidate_keys(c):
            if k in by_key:
                by_key[k]["last_seen_at"] = now_iso()
                break

    watchlist["candidates"] = new_items + watchlist.get("candidates", [])
    # keep inbox manageable
    watchlist["candidates"] = watchlist["candidates"][:500]
    watchlist["updated_at"] = now_iso()
    watchlist["last_run"] = {
        "at": now_iso(),
        "sources": enabled_sources,
        "keywords": keywords,
        "fetched": len(raw),
        "merged": len(merged),
        "new": len(new_items),
    }
    watchlist["topic"] = cfg.get("topic", watchlist.get("topic", "agent harness"))
    watchlist["schema_version"] = 1

    snapshot = {
        "date": today_str(),
        "run": watchlist["last_run"],
        "new_candidates": new_items,
    }

    print(
        f"done: fetched={len(raw)} merged={len(merged)} new={len(new_items)} "
        f"sources={enabled_sources}"
    )
    for c in new_items[:15]:
        print(f"  + [{c.get('source')}] {c.get('published','')} {c.get('title','')[:80]}")
    if len(new_items) > 15:
        print(f"  ... and {len(new_items) - 15} more")

    if dry_run:
        print("dry-run: not writing files")
        return 0

    INBOX_DIR.mkdir(parents=True, exist_ok=True)
    WATCHLIST_PATH.write_text(json.dumps(watchlist, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    inbox_path = INBOX_DIR / f"{today_str()}.json"
    inbox_path.write_text(json.dumps(snapshot, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {WATCHLIST_PATH.relative_to(ROOT)}")
    print(f"wrote {inbox_path.relative_to(ROOT)}")
    return 0


def main() -> None:
    ap = argparse.ArgumentParser(description="Monitor papers via Paper Trends-compatible public APIs")
    ap.add_argument(
        "--sources",
        default="",
        help="comma-separated subset: arxiv,crossref,semanticscholar,dblp,pubmed",
    )
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    sources = [s.strip() for s in args.sources.split(",") if s.strip()] or None
    raise SystemExit(run(sources, args.dry_run))


if __name__ == "__main__":
    main()
