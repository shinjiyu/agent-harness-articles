#!/usr/bin/env python3
"""Promote watchlist candidates into index.json with abstract-level tiers."""

from __future__ import annotations

import html
import json
import re
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX_DIR = ROOT / "indexes" / "agent-harness"
INDEX_PATH = INDEX_DIR / "index.json"
WATCHLIST_PATH = INDEX_DIR / "watchlist.json"
TZ = timezone(timedelta(hours=8))
UA = "agent-harness-articles/0.1 (promote-watchlist)"
ATOM = "{http://www.w3.org/2005/Atom}"


def now_iso() -> str:
    return datetime.now(TZ).replace(microsecond=0).isoformat()


def arxiv_id_from_url(url: str) -> str:
    m = re.search(r"arXiv\.(\d{4}\.\d{4,5})", url or "", re.I)
    if m:
        return m.group(1)
    m = re.search(r"arxiv\.org/abs/(\d{4}\.\d{4,5})", url or "", re.I)
    return m.group(1) if m else ""


def clean_authors(authors: list[str]) -> list[str]:
    out = []
    for a in authors:
        a = re.sub(r"\s+\d{4}$", "", a.strip())  # drop dblp numbering suffix like "0001"
        a = re.sub(r"\s+\d{4}\b", "", a)
        a = html.unescape(a)
        if a:
            out.append(a)
    return out


def fetch_arxiv_meta(arxiv_id: str) -> dict:
    url = (
        "https://export.arxiv.org/api/query?"
        + f"id_list={arxiv_id}&max_results=1"
    )
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                raw = resp.read()
            break
        except urllib.error.HTTPError as e:
            if e.code == 429 and attempt < 3:
                time.sleep(10 * (attempt + 1))
                continue
            raise
    root = ET.fromstring(raw)
    entry = root.find(f"{ATOM}entry")
    if entry is None:
        return {}
    title = re.sub(r"\s+", " ", (entry.findtext(f"{ATOM}title") or "").strip())
    abstract = re.sub(r"\s+", " ", (entry.findtext(f"{ATOM}summary") or "").strip())
    published = (entry.findtext(f"{ATOM}published") or "")[:10]
    authors = [
        (a.findtext(f"{ATOM}name") or "").strip()
        for a in entry.findall(f"{ATOM}author")
    ]
    id_url = entry.findtext(f"{ATOM}id") or ""
    ver = re.search(r"(v\d+)$", id_url)
    return {
        "title": title,
        "abstract": abstract,
        "published": published,
        "authors": [a for a in authors if a],
        "arxiv_version": ver.group(1) if ver else "v1",
    }


# Manual abstract-level ratings (title + known role in literature).
RATINGS: dict[str, dict] = {
    "2605.27922": {
        "tier": "A",
        "tier_reason": "跨模型实测 harness 效应；与 Harness Effect 互补的评测基建。",
        "tags": ["evaluation", "benchmark", "methodology", "orchestration"],
        "notes": "Harness-Bench：模型–harness 配置是能力单位",
        "knowledge_ids": ["evaluation"],
    },
    "2606.15874": {
        "tier": "B",
        "tier_reason": "LLM-as-Code 架构主张清晰；实证偏案例，外推待核。",
        "tags": ["orchestration", "control", "architecture"],
        "notes": "控制流归程序，LLM 只作自适应组件",
    },
    "2606.12882": {
        "tier": "B",
        "tier_reason": "可学习双向 harness 控制器；工程贡献明确，域覆盖待核。",
        "tags": ["control", "adaptation", "orchestration"],
        "notes": "HarnessBridge：冻结执行器上的可学习控制层",
    },
    "2606.10106": {
        "tier": "B",
        "tier_reason": "给出 harness 必要充分条件的概念框架；偏定义文。",
        "tags": ["orchestration", "methodology"],
        "notes": "What makes a harness a harness",
    },
    "2604.25850": {
        "tier": "B",
        "tier_reason": "可观测驱动的编码 harness 自动演化；自演化路线实证。",
        "tags": ["self-evolution", "observability", "code-agent", "orchestration"],
        "notes": "Agentic Harness Engineering",
    },
    "2605.30621": {
        "tier": "B",
        "tier_reason": "区分「能更新 harness」与「更新带来收益」；对自演化叙事有纠偏。",
        "tags": ["self-evolution", "evaluation", "methodology"],
        "notes": "Harness Updating ≠ Harness Benefit",
    },
    "2604.07236": {
        "tier": "B",
        "tier_reason": "度量 harness 承担多少重活 vs LLM 残差角色；测量设计清楚。",
        "tags": ["evaluation", "orchestration", "planning"],
        "notes": "规划代理中 harness 的重活占比",
    },
    "2605.15184": {
        "tier": "B",
        "tier_reason": "讨论 harness 如何重塑 agentic search；偏经验/系统设计。",
        "tags": ["orchestration", "search"],
        "notes": "Is Grep All You Need?",
    },
    "2601.15322": {
        "tier": "B",
        "tier_reason": "金融工具调用代理的可重放/确定性保真 harness。",
        "tags": ["audit", "validation", "enterprise", "tool-calling"],
        "notes": "Replayable Financial Agents",
    },
    "2602.22480": {
        "tier": "B",
        "tier_reason": "用代理优化代理的评估 harness（VeRO）；评测基建。",
        "tags": ["evaluation", "benchmark"],
        "notes": "VeRO evaluation harness",
    },
    "2606.11686": {
        "tier": "B",
        "tier_reason": "对确定性脚手架做无 LLM 回归锁定测试；工程评测味道浓。",
        "tags": ["evaluation", "testing", "enterprise"],
        "notes": "Layer-Isolated Evaluation",
    },
    "2606.08348": {
        "tier": "B",
        "tier_reason": "后验引导的技能演化；自演化+harness 交叉。",
        "tags": ["self-evolution", "skill", "bayesian"],
        "notes": "Bayesian-Agent skill evolution",
    },
    "2606.20631": {
        "tier": "B",
        "tier_reason": "技能中介 LLM 代理的架构模式与参考架构；综述/模式文。",
        "tags": ["skill", "architecture", "orchestration"],
        "notes": "Agent Skills reference architecture",
    },
    "2606.21856": {
        "tier": "B",
        "tier_reason": "多用户 LLM 代理的安全治理 harness；领域专用。",
        "tags": ["security", "governance", "multi-agent", "permissions"],
        "notes": "Harness-MU",
    },
    "2605.15218": {
        "tier": "C",
        "tier_reason": "APDL/CAE 专域轻量 harness；与通用 harness 主线关联弱。",
        "tags": ["domain", "code-agent"],
        "notes": "CAX-Agent APDL",
    },
}


SKIP_TITLES = {
    "agentic artificial intelligence - harnessing ai agents to reinvent business, work, and life",
}


def write_a_intro(arxiv_id: str, title: str, published: str, authors: list[str], abstract: str, rating: dict) -> str:
    path = INDEX_DIR / "papers" / "a" / f"{arxiv_id}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    abs_short = abstract[:1200] + ("…" if len(abstract) > 1200 else "")
    body = f"""# {title}

- ArXiv: [{arxiv_id}](http://arxiv.org/abs/{arxiv_id})
- Tier: **A**
- Indexed: {now_iso()}

## 核心介绍

{rating.get('notes') or title}

### 分档理由

{rating['tier_reason']}

### 摘要要点（机器摘录）

{abs_short if abs_short else '（暂无摘要，待补）'}

### 挂载知识点

{', '.join(rating.get('knowledge_ids') or rating.get('tags') or [])}

### 阅读时注意

本介绍为摘要级入库笔记；完整机制与实验以 PDF/HTML 为准。
"""
    path.write_text(body, encoding="utf-8")
    return f"papers/a/{arxiv_id}.md"


def main() -> None:
    index = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
    watch = json.loads(WATCHLIST_PATH.read_text(encoding="utf-8"))
    existing = {p["arxiv_id"] for p in index["papers"] if p.get("arxiv_id")}
    existing_titles = {p["title"].lower().strip() for p in index["papers"]}

    added = []
    skipped = []
    ts = now_iso()

    for c in watch.get("candidates", []):
        title = html.unescape(c.get("title") or "").strip()
        if title.lower() in SKIP_TITLES:
            c["status"] = "skipped"
            c["skip_reason"] = "book / weak harness sense"
            skipped.append(title)
            continue

        aid = c.get("arxiv_id") or arxiv_id_from_url(c.get("url") or "")
        if not aid:
            c["status"] = "needs_manual"
            skipped.append(title)
            continue
        if aid in existing or title.lower() in existing_titles:
            c["status"] = "already_indexed"
            continue

        rating = RATINGS.get(aid)
        if not rating:
            c["status"] = "needs_manual"
            skipped.append(f"{aid} {title}")
            continue

        print(f"fetch {aid} ...")
        meta = {}
        try:
            meta = fetch_arxiv_meta(aid)
            time.sleep(3.5)
        except Exception as e:
            print(f"  arxiv fetch failed: {e}")

        authors = meta.get("authors") or clean_authors(c.get("authors") or [])
        published = meta.get("published") or (c.get("published") if "-" in str(c.get("published")) else "")
        if not published and c.get("published"):
            published = f"{c['published']}-01-01" if len(str(c["published"])) == 4 else str(c["published"])
        final_title = meta.get("title") or title
        abstract = meta.get("abstract") or c.get("abstract") or ""
        version = meta.get("arxiv_version") or "v1"

        entry = {
            "arxiv_id": aid,
            "arxiv_version": version,
            "title": final_title,
            "authors": authors[:12] if len(authors) > 12 else authors,
            "published": published,
            "url": f"http://arxiv.org/abs/{aid}",
            "source": "arxiv",
            "tier": rating["tier"],
            "tier_reason": rating["tier_reason"],
            "tags": rating.get("tags") or [],
            "notes": rating.get("notes") or "",
            "indexed_at": ts,
        }
        if rating.get("knowledge_ids"):
            entry["knowledge_ids"] = rating["knowledge_ids"]
        if rating["tier"] == "A":
            entry["core_intro_path"] = write_a_intro(
                aid, final_title, published, authors, abstract, rating
            )

        index["papers"].append(entry)
        existing.add(aid)
        existing_titles.add(final_title.lower())
        c["status"] = "promoted"
        c["arxiv_id"] = aid
        c["promoted_tier"] = rating["tier"]
        c["promoted_at"] = ts
        added.append((aid, rating["tier"], final_title))
        print(f"  + {rating['tier']} {aid} {final_title[:60]}")

    # reorder
    order = {"A": 0, "B": 1, "C": 2}
    by_tier = {"A": [], "B": [], "C": []}
    for p in index["papers"]:
        by_tier.setdefault(p["tier"], []).append(p)
    for t in by_tier:
        by_tier[t].sort(key=lambda x: x.get("published") or "", reverse=True)
    index["papers"] = by_tier.get("A", []) + by_tier.get("B", []) + by_tier.get("C", [])
    index["updated_at"] = ts
    index["tier_counts"] = {
        "A": len(by_tier.get("A", [])),
        "B": len(by_tier.get("B", [])),
        "C": len(by_tier.get("C", [])),
        "total": len(index["papers"]),
    }

    watch["updated_at"] = ts
    INDEX_PATH.write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    WATCHLIST_PATH.write_text(json.dumps(watch, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"\npromoted {len(added)} papers → index now {index['tier_counts']}")
    for aid, tier, title in added:
        print(f"  [{tier}] {aid} {title[:70]}")
    if skipped:
        print("skipped/needs_manual:")
        for s in skipped:
            print(" ", s[:80])


if __name__ == "__main__":
    main()
