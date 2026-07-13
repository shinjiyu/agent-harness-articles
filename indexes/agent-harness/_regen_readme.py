#!/usr/bin/env python3
"""Regenerate README.md from index.json. Run after any index update."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def main() -> None:
    data = json.loads((ROOT / "index.json").read_text(encoding="utf-8"))
    counts = data["tier_counts"]
    lines: list[str] = [
        f"# {data['topic']} 论文索引",
        "",
        f"- 主题关键词：`{data.get('query_keyword', data['topic'])}`",
        f"- 创建时间：`{data['created_at']}`",
        f"- 最近更新：`{data['updated_at']}`",
        f"- 条目数：**{counts['total']}**（A {counts['A']} / B {counts['B']} / C {counts['C']}）",
        f"- 评级依据：{data.get('rating_basis', '')}",
        "",
        "权威数据源是 [`index.json`](index.json)。更新约定见 [`SCHEMA.md`](SCHEMA.md)。变更历史见 [`CHANGELOG.md`](CHANGELOG.md)。",
        "",
        "## 分档标准（摘要级）",
        "",
        "| 档 | 含义 |",
        "|----|------|",
        "| **A** | 主张清晰，有受控对照或评测审计，可指导工程决策 |",
        "| **B** | 有实证，但样本/外推/复现有明显软肋 |",
        "| **C** | 愿景、平台、技术报告或与主线关联偏弱 |",
        "",
        "## A 档（含核心介绍）",
        "",
    ]

    by_tier = {"A": [], "B": [], "C": []}
    for p in data["papers"]:
        by_tier[p["tier"]].append(p)

    for p in by_tier["A"]:
        intro = p.get("core_intro_path", "")
        link = f"[核心介绍]({intro})" if intro else "—"
        lines.extend(
            [
                f"### [{p['arxiv_id']}]({p['url']}) · {p['title']}",
                "",
                f"- 分档：`A` — {p['tier_reason']}",
                f"- 入库时间：`{p['indexed_at']}`",
                f"- ArXiv 公布：`{p.get('published', '')}`",
                f"- {link}",
                "",
            ]
        )

    lines.extend(["## B 档", "", "| ArXiv | 标题 | 入库时间 | 理由 |", "|-------|------|----------|------|"])
    for p in by_tier["B"]:
        title = p["title"].replace("|", "\\|")
        lines.append(
            f"| [{p['arxiv_id']}]({p['url']}) | {title} | `{p['indexed_at']}` | {p['tier_reason']} |"
        )

    lines.extend(["", "## C 档", "", "| ArXiv | 标题 | 入库时间 | 理由 |", "|-------|------|----------|------|"])
    for p in by_tier["C"]:
        title = p["title"].replace("|", "\\|")
        lines.append(
            f"| [{p['arxiv_id']}]({p['url']}) | {title} | `{p['indexed_at']}` | {p['tier_reason']} |"
        )

    lines.extend(
        [
            "",
            "## 持续更新",
            "",
            "1. 按 `arxiv_id` 查重。",
            "2. 新文写入 `index.json`，填写 `indexed_at`（加入索引时间）与 `tier` / `tier_reason`。",
            "3. A 档必须新增 `papers/a/<arxiv_id>.md` 核心介绍，并设置 `core_intro_path`。",
            "4. 更新库级 `updated_at`，在 `CHANGELOG.md` 追加记录。",
            "5. 运行 `python _regen_readme.py` 刷新本页。",
            "",
        ]
    )

    (ROOT / "README.md").write_text("\n".join(lines), encoding="utf-8")
    print("wrote README.md")


if __name__ == "__main__":
    main()
