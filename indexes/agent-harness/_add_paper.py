#!/usr/bin/env python3
"""Upsert a paper into index.json for continuous updates.

Example:
  python _add_paper.py --arxiv-id 2607.09999 --title "..." --tier B \\
    --tier-reason "..." --published 2026-07-12

A-tier also requires creating papers/a/<id>.md and --core-intro-path.
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TZ = timezone(timedelta(hours=8))


def now_iso() -> str:
    return datetime.now(TZ).replace(microsecond=0).isoformat()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--arxiv-id", required=True)
    ap.add_argument("--title", required=True)
    ap.add_argument("--tier", required=True, choices=["A", "B", "C"])
    ap.add_argument("--tier-reason", required=True)
    ap.add_argument("--published", default="")
    ap.add_argument("--arxiv-version", default="v1")
    ap.add_argument("--authors", default="", help="comma-separated")
    ap.add_argument("--tags", default="", help="comma-separated")
    ap.add_argument("--notes", default="")
    ap.add_argument("--core-intro-path", default="")
    ap.add_argument("--url", default="")
    args = ap.parse_args()

    if args.tier == "A" and not args.core_intro_path:
        raise SystemExit("A-tier requires --core-intro-path (and a markdown intro file)")

    path = ROOT / "index.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    ts = now_iso()
    existing = {p["arxiv_id"]: i for i, p in enumerate(data["papers"])}

    entry = {
        "arxiv_id": args.arxiv_id,
        "arxiv_version": args.arxiv_version,
        "title": args.title,
        "authors": [a.strip() for a in args.authors.split(",") if a.strip()],
        "published": args.published,
        "url": args.url or f"http://arxiv.org/abs/{args.arxiv_id}",
        "source": "arxiv",
        "tier": args.tier,
        "tier_reason": args.tier_reason,
        "tags": [t.strip() for t in args.tags.split(",") if t.strip()],
        "notes": args.notes,
    }
    if args.core_intro_path:
        entry["core_intro_path"] = args.core_intro_path

    if args.arxiv_id in existing:
        old = data["papers"][existing[args.arxiv_id]]
        entry["indexed_at"] = old["indexed_at"]
        entry["updated_at"] = ts
        data["papers"][existing[args.arxiv_id]] = entry
        action = "updated"
    else:
        entry["indexed_at"] = ts
        data["papers"].append(entry)
        action = "added"

    order = {"A": 0, "B": 1, "C": 2}
    by_tier = {"A": [], "B": [], "C": []}
    for p in data["papers"]:
        by_tier[p["tier"]].append(p)
    for tier in by_tier:
        by_tier[tier].sort(key=lambda x: x.get("published") or "", reverse=True)
    data["papers"] = by_tier["A"] + by_tier["B"] + by_tier["C"]
    data["updated_at"] = ts
    data["tier_counts"] = {
        "A": len(by_tier["A"]),
        "B": len(by_tier["B"]),
        "C": len(by_tier["C"]),
        "total": len(data["papers"]),
    }

    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{action} {args.arxiv_id} tier={args.tier} at {ts}")
    print("Remember: append CHANGELOG.md and run _regen_readme.py")


if __name__ == "__main__":
    main()
