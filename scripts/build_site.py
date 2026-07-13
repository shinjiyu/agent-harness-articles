#!/usr/bin/env python3
"""Build the static learning site from curriculum + paper index."""

from __future__ import annotations

import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CURRICULUM = ROOT / "curriculum"
INDEX = ROOT / "indexes" / "agent-harness" / "index.json"
SITE = ROOT / "site"


def md_to_html(text: str) -> str:
    """Minimal Markdown → HTML for our curriculum files."""
    text = text.replace("\r\n", "\n")
    lines = text.split("\n")
    out: list[str] = []
    i = 0
    in_ul = False
    in_ol = False
    in_table = False
    table_rows: list[str] = []
    in_code = False
    code_lang = ""
    code_buf: list[str] = []
    in_bq = False
    bq_buf: list[str] = []

    def close_lists() -> None:
        nonlocal in_ul, in_ol
        if in_ul:
            out.append("</ul>")
            in_ul = False
        if in_ol:
            out.append("</ol>")
            in_ol = False

    def close_table() -> None:
        nonlocal in_table, table_rows
        if not in_table:
            return
        body = []
        for ri, row in enumerate(table_rows):
            cells = [c.strip() for c in row.strip("|").split("|")]
            tag = "th" if ri == 0 else "td"
            # skip separator row
            if ri == 1 and all(re.fullmatch(r":?-{3,}:?", c.replace(" ", "")) for c in cells):
                continue
            body.append("<tr>" + "".join(f"<{tag}>{inline(c)}</{tag}>" for c in cells) + "</tr>")
        out.append("<table>" + "".join(body) + "</table>")
        in_table = False
        table_rows = []

    def close_bq() -> None:
        nonlocal in_bq, bq_buf
        if not in_bq:
            return
        inner = " ".join(bq_buf)
        out.append(f'<div class="box tip"><span class="box-title">引用</span>{inline(inner)}</div>')
        in_bq = False
        bq_buf = []

    def inline(s: str) -> str:
        s = html.escape(s)
        s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
        s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
        s = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", s)
        s = re.sub(
            r"\[([^\]]+)\]\(([^)]+)\)",
            r'<a href="\2" target="_blank" rel="noopener noreferrer">\1</a>',
            s,
        )
        # restore simple math delimiters already escaped
        s = s.replace("\\(", "(").replace("\\)", ")")
        return s

    while i < len(lines):
        line = lines[i]

        if line.startswith("```"):
            close_lists()
            close_table()
            close_bq()
            if not in_code:
                in_code = True
                code_lang = line[3:].strip()
                code_buf = []
            else:
                code = html.escape("\n".join(code_buf))
                out.append(f"<pre><code>{code}</code></pre>")
                in_code = False
            i += 1
            continue

        if in_code:
            code_buf.append(line)
            i += 1
            continue

        if line.startswith("> "):
            close_lists()
            close_table()
            in_bq = True
            bq_buf.append(line[2:])
            i += 1
            continue
        elif in_bq:
            close_bq()

        if line.startswith("|"):
            close_lists()
            in_table = True
            table_rows.append(line)
            i += 1
            continue
        elif in_table:
            close_table()

        if re.match(r"^#{1,3} ", line):
            close_lists()
            level = len(line) - len(line.lstrip("#"))
            content = line[level + 1 :].strip()
            # lead style for first paragraph after h1 is handled separately
            out.append(f"<h{level}>{inline(content)}</h{level}>")
            i += 1
            continue

        m = re.match(r"^[-*] (.+)$", line)
        if m:
            close_table()
            if in_ol:
                out.append("</ol>")
                in_ol = False
            if not in_ul:
                out.append("<ul>")
                in_ul = True
            out.append(f"<li>{inline(m.group(1))}</li>")
            i += 1
            continue

        m = re.match(r"^(\d+)\. (.+)$", line)
        if m:
            close_table()
            if in_ul:
                out.append("</ul>")
                in_ul = False
            if not in_ol:
                out.append("<ol>")
                in_ol = True
            out.append(f"<li>{inline(m.group(2))}</li>")
            i += 1
            continue

        if not line.strip():
            close_lists()
            i += 1
            continue

        close_lists()
        # first non-heading paragraph after h1 → lead
        if out and out[-1].startswith("<h1>") and not any(
            x.startswith("<p") or x.startswith('<p class="lead"') for x in out[-3:]
        ):
            out.append(f'<p class="lead">{inline(line)}</p>')
        else:
            out.append(f"<p>{inline(line)}</p>")
        i += 1

    close_lists()
    close_table()
    close_bq()
    if in_code:
        out.append(f"<pre><code>{html.escape(chr(10).join(code_buf))}</code></pre>")

    # takeaways heuristic
    joined = "\n".join(out)
    joined = joined.replace(
        "<h3>关键要点</h3>",
        '<div class="takeaways box"><span class="box-title">关键要点</span>',
    )
    if '<div class="takeaways box">' in joined and "</div>" not in joined.split('<div class="takeaways box">')[-1]:
        # close after following ul
        joined = re.sub(
            r'(<div class="takeaways box"><span class="box-title">关键要点</span>\s*<ul>.*?</ul>)',
            r"\1</div>",
            joined,
            count=1,
            flags=re.S,
        )
    return joined


def paper_card(p: dict, *, show_intro: bool = False, intro_html: str = "") -> str:
    tags = " ".join(f'<span class="pill">{html.escape(t)}</span>' for t in p.get("tags", []))
    tier = p.get("tier", "?")
    tier_cls = {"A": "tier-a", "B": "tier-b", "C": "tier-c"}.get(tier, "")
    meta = (
        f'<div class="paper-meta">'
        f'<span class="tier-badge {tier_cls}">Tier {html.escape(tier)}</span>'
        f'<a href="{html.escape(p.get("url", "#"))}" target="_blank" rel="noopener noreferrer">'
        f'arXiv:{html.escape(p["arxiv_id"])}</a>'
        f'<span>入库 {html.escape(p.get("indexed_at", ""))}</span>'
        f'<span>公布 {html.escape(p.get("published", ""))}</span>'
        f"</div>"
    )
    reason = html.escape(p.get("tier_reason", ""))
    notes = html.escape(p.get("notes", "") or "")
    body = (
        f'<article class="paper-card" id="paper-{html.escape(p["arxiv_id"])}">'
        f'<h3><a href="{html.escape(p.get("url", "#"))}" target="_blank" rel="noopener noreferrer">'
        f'{html.escape(p["title"])}</a></h3>'
        f"{meta}"
        f'<p class="paper-reason">{reason}</p>'
    )
    if notes:
        body += f'<p class="paper-notes">{notes}</p>'
    if tags:
        body += f'<div class="paper-tags">{tags}</div>'
    if show_intro and intro_html:
        body += f'<div class="paper-intro">{intro_html}</div>'
    body += "</article>"
    return body


def load_intro_html(p: dict) -> str:
    rel = p.get("core_intro_path")
    if not rel:
        return ""
    path = ROOT / "indexes" / "agent-harness" / rel
    if not path.exists():
        return ""
    # Skip the duplicate title block; render from "## 核心介绍" or full
    text = path.read_text(encoding="utf-8")
    # Drop first H1 if present
    text = re.sub(r"^# .*\n+", "", text, count=1)
    return md_to_html(text)


def select_papers(papers: list[dict], chapter: dict) -> list[dict]:
    mode = chapter.get("papers_mode", "none")
    if mode == "none":
        return []
    if mode == "all_by_tier":
        order = {"A": 0, "B": 1, "C": 2}
        return sorted(papers, key=lambda p: (order.get(p["tier"], 9), p.get("published", "")), reverse=False)
    if mode == "tier_a":
        return [p for p in papers if p.get("tier") == "A"]

    tags = set(chapter.get("tags") or [])
    cid = chapter["id"]
    matched = []
    for p in papers:
        kids = set(p.get("knowledge_ids") or [])
        ptags = set(p.get("tags") or [])
        if cid in kids or (tags and ptags & tags):
            matched.append(p)

    # prefer A then B then C, then newer
    order = {"A": 0, "B": 1, "C": 2}
    matched.sort(key=lambda p: (order.get(p["tier"], 9), p.get("published", "")), reverse=False)
    # within tier, newer first
    by_tier: dict[str, list] = {"A": [], "B": [], "C": []}
    for p in matched:
        by_tier.setdefault(p["tier"], []).append(p)
    for t in by_tier:
        by_tier[t].sort(key=lambda p: p.get("published", ""), reverse=True)
    matched = by_tier.get("A", []) + by_tier.get("B", []) + by_tier.get("C", [])
    limit = chapter.get("papers_limit")
    if limit:
        matched = matched[: int(limit)]
    return matched


def papers_section(papers: list[dict], chapter: dict) -> str:
    mode = chapter.get("papers_mode", "none")
    if mode == "none" or not papers:
        return ""

    if mode == "all_by_tier":
        blocks = ['<h2>分档论文</h2>']
        for tier in ("A", "B", "C"):
            group = [p for p in papers if p.get("tier") == tier]
            if not group:
                continue
            blocks.append(f"<h3>Tier {tier}（{len(group)}）</h3>")
            blocks.append('<div class="paper-list">')
            for p in group:
                blocks.append(paper_card(p))
            blocks.append("</div>")
        return "\n".join(blocks)

    if mode == "tier_a":
        blocks = ['<h2>A 档论文与核心介绍</h2>', '<div class="paper-list">']
        for p in papers:
            blocks.append(paper_card(p, show_intro=True, intro_html=load_intro_html(p)))
        blocks.append("</div>")
        return "\n".join(blocks)

    blocks = [
        f'<h2>相关论文 <span class="muted">({len(papers)})</span></h2>',
        '<p class="section-note">由论文 <code>tags</code> / <code>knowledge_ids</code> 自动挂载到本章；入库时间见卡片。</p>',
        '<div class="paper-list">',
    ]
    for p in papers:
        blocks.append(paper_card(p))
    blocks.append("</div>")
    return "\n".join(blocks)


def build() -> None:
    catalog = json.loads((CURRICULUM / "catalog.json").read_text(encoding="utf-8"))
    index = json.loads(INDEX.read_text(encoding="utf-8"))
    papers = index["papers"]

    chapters_out = []
    for ch in catalog["chapters"]:
        md_path = CURRICULUM / "chapters" / ch["file"]
        body = md_to_html(md_path.read_text(encoding="utf-8"))
        related = select_papers(papers, ch)
        body += "\n" + papers_section(related, ch)
        keywords = ch.get("keywords", "")
        # also index paper titles for search
        for p in related:
            keywords += " " + p.get("title", "") + " " + p.get("arxiv_id", "")
        chapters_out.append(
            {
                "id": ch["id"],
                "module": ch["module"],
                "title": ch["title"],
                "keywords": keywords,
                "html": body,
            }
        )

    SITE.mkdir(parents=True, exist_ok=True)
    meta = {
        "built_from_index_updated_at": index.get("updated_at"),
        "paper_counts": index.get("tier_counts"),
        "chapter_count": len(chapters_out),
        "site": catalog["site"],
    }
    (SITE / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # content.js
    content_js = (
        "/* Auto-generated by scripts/build_site.py — do not edit by hand */\n"
        f"window.AH_META = {json.dumps(meta, ensure_ascii=False)};\n"
        f"window.AH_CONTENT = {json.dumps(chapters_out, ensure_ascii=False)};\n"
    )
    (SITE / "content.js").write_text(content_js, encoding="utf-8")

    # copy static shell if present (always rewrite index title from catalog)
    write_shell(catalog["site"], index)
    print(
        f"built site/ → {len(chapters_out)} chapters, "
        f"{index['tier_counts']['total']} papers "
        f"(A{index['tier_counts']['A']}/B{index['tier_counts']['B']}/C{index['tier_counts']['C']})"
    )


def write_shell(site: dict, index: dict) -> None:
    # html / css / js are maintained as templates in this function + separate files
    # Ensure script assets exist (written once by repo files)
    counts = index.get("tier_counts", {})
    subtitle = (
        f"索引更新 {index.get('updated_at', '')} · "
        f"论文 {counts.get('total', 0)} "
        f"(A {counts.get('A', 0)} / B {counts.get('B', 0)} / C {counts.get('C', 0)})"
    )
    # Patch a small generated snippet used by index if needed
    (SITE / "build-stamp.txt").write_text(subtitle + "\n", encoding="utf-8")


if __name__ == "__main__":
    build()
