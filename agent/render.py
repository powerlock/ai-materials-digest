"""Render a day's findings and prepend them to the running digest document."""

from __future__ import annotations

import datetime as dt
import os
from typing import Dict, List

MARKER = "<!-- NEW-ENTRIES-BELOW -->"

HEADER = """# AI and Materials Discovery - Daily Digest

Automatically compiled from arXiv, Crossref, OpenAlex, journal RSS feeds, the
NVIDIA / Microsoft Research / Google DeepMind blogs, and GitHub releases.
Newest entries appear directly below this line.

""" + MARKER + "\n"

SECTION_TITLES = [
    ("journals", "Journal articles"),
    ("preprints", "Preprints (arXiv / ChemRxiv / other)"),
    ("conferences", "Conference papers"),
    ("industry", "Industry labs and code releases"),
]


def _entry(item: Dict) -> str:
    title = item["title"].replace("\n", " ").strip().rstrip(".")
    line = f"- **[{title}]({item['url']})**\n"
    meta = [item["source"]]
    if item["date"]:
        meta.append(item["date"])
    if item["doi"]:
        meta.append("doi:" + item["doi"])
    meta.append(f"score {item['score']}")
    line += f"  <br>*{' | '.join(meta)}*\n"
    if item.get("extra"):
        line += f"  <br>{item['extra']}\n"
    if item["summary"]:
        line += f"\n  {item['summary']}\n"
    if item.get("matched"):
        line += f"\n  `matched: {', '.join(item['matched'])}`\n"
    return line + "\n"


def build_section(items: List[Dict], run_date: dt.date, cfg: Dict) -> str:
    if not items:
        return (
            f"## {run_date.isoformat()}\n\n"
            "_No new items cleared the relevance threshold today._\n\n"
        )

    out = [f"## {run_date.isoformat()}", ""]
    out.append(
        f"{len(items)} new item(s). Top hit: **{items[0]['title'][:110]}** "
        f"(score {items[0]['score']}, {items[0]['source']}).\n"
    )
    for key, label in SECTION_TITLES:
        bucket = [i for i in items if i["section"] == key]
        if not bucket:
            continue
        out.append(f"### {label}")
        out.append("")
        out.extend(_entry(i) for i in bucket)
    out.append("---")
    out.append("")
    return "\n".join(out)


def prepend(digest_path: str, block: str) -> None:
    if os.path.exists(digest_path):
        with open(digest_path, encoding="utf-8") as fh:
            existing = fh.read()
    else:
        existing = HEADER

    if MARKER not in existing:
        existing = HEADER + "\n" + existing

    head, tail = existing.split(MARKER, 1)
    updated = head + MARKER + "\n\n" + block.rstrip() + "\n" + tail
    with open(digest_path, "w", encoding="utf-8") as fh:
        fh.write(updated)
