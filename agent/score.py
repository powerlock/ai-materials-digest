"""Keyword relevance scoring. No API key, no model, fully deterministic.

Gate: an item must hit a core term, or an AI term AND a materials term. That
single rule is what keeps "GeForce NOW gaming update" and "new perovskite solar
cell, no ML" out of an AI-for-materials digest.
"""

from __future__ import annotations

from typing import Dict, List, Tuple


def _hits(text: str, table: Dict[str, int]) -> List[Tuple[str, int]]:
    return [(term, weight) for term, weight in table.items() if weight and term in text]


def score_item(item: Dict, cfg: Dict) -> Dict:
    title = item["title"].lower()
    body = (item["title"] + " " + item["summary"] + " " + item.get("extra", "")).lower()

    for veto in cfg.get("veto_terms", []):
        if veto in body:
            item["score"] = 0
            item["matched"] = []
            return item

    core = _hits(body, cfg["core_terms"])
    ai = _hits(body, cfg["ai_terms"])
    mat = _hits(body, cfg["materials_terms"])
    bonus = _hits(body, cfg["bonus_terms"])

    if not core and not (ai and mat):
        item["score"] = 0
        item["matched"] = []
        return item

    score = 0
    matched = []
    for term, weight in core + ai + mat + bonus:
        score += weight * (2 if term in title else 1)
        matched.append(term)

    score += item.get("bonus", 0)
    item["score"] = score
    item["matched"] = sorted(set(matched), key=len, reverse=True)[:6]
    return item


def rank(items: List[Dict], cfg: Dict) -> List[Dict]:
    scored = [score_item(dict(i), cfg) for i in items]
    keep = [i for i in scored if i["score"] >= cfg["min_score"]]
    keep.sort(key=lambda i: (i["score"], i["date"]), reverse=True)
    return keep


def cap_per_section(items: List[Dict], cfg: Dict) -> List[Dict]:
    """Trim each section to max_items_per_section.

    Applied before anything is written to the seen-store, so that items which
    lose out today are still eligible tomorrow rather than silently dropped.
    """
    limits = cfg.get("max_items_per_section") or {}
    if isinstance(limits, int):  # a single number applies to every section
        limits = {"default": limits}
    default = limits.get("default", 10 ** 6)

    counts: Dict[str, int] = {}
    out = []
    for item in items:
        section = item["section"]
        counts[section] = counts.get(section, 0) + 1
        if counts[section] <= limits.get(section, default):
            out.append(item)
    return out
