"""Persistent 'already reported' store so the digest never repeats itself."""

from __future__ import annotations

import datetime as dt
import json
import os
import re
from typing import Dict, Iterable, List

RETENTION_DAYS = 365


def key_for(item: Dict) -> str:
    if item.get("doi"):
        return "doi:" + item["doi"]
    url = item.get("url", "")
    m = re.search(r"arxiv\.org/abs/([\d.v]+)", url)
    if m:
        return "arxiv:" + m.group(1).split("v")[0]
    if url:
        return "url:" + url.split("?")[0]
    return "title:" + re.sub(r"[^a-z0-9]", "", item["title"].lower())[:90]


def load(path: str) -> Dict[str, str]:
    if not os.path.exists(path):
        return {}
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    except (ValueError, OSError):
        return {}


def save(path: str, seen: Dict[str, str]) -> None:
    cutoff = (dt.date.today() - dt.timedelta(days=RETENTION_DAYS)).isoformat()
    pruned = {k: v for k, v in seen.items() if v >= cutoff}
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(pruned, fh, indent=0, sort_keys=True)


def filter_new(items: Iterable[Dict], seen: Dict[str, str]) -> List[Dict]:
    return [i for i in items if key_for(i) not in seen]


def mark(items: Iterable[Dict], seen: Dict[str, str]) -> None:
    today = dt.date.today().isoformat()
    for item in items:
        seen[key_for(item)] = today
