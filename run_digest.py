#!/usr/bin/env python
"""Daily AI-for-materials-discovery digest.

    python run_digest.py                 # normal daily run
    python run_digest.py --dry-run       # print, do not write anything
    python run_digest.py --days 14       # widen the lookback window
    python run_digest.py --min-score 10  # be pickier for one run
"""

from __future__ import annotations

import argparse
import datetime as dt
import io
import json
import os
import sys

from agent import fetch, render, score, sources, state

# Windows consoles default to cp1252 and choke on accented author names.
if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

ROOT = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(ROOT, "config.json")
DIGEST_PATH = os.path.join(ROOT, "DIGEST.md")
STATE_PATH = os.path.join(ROOT, "state", "seen.json")


def load_config() -> dict:
    with open(CONFIG_PATH, encoding="utf-8") as fh:
        return json.load(fh)


def collect(cfg: dict, since: dt.date) -> list:
    items = []

    print("Journal and blog feeds:")
    for label, url, section, bonus in sources.JOURNAL_FEEDS + sources.BLOG_FEEDS:
        items += fetch.fetch_feed(label, url, section, bonus)

    print("arXiv:")
    for query in sources.ARXIV_QUERIES:
        items += fetch.fetch_arxiv(query)

    mailto = os.environ.get("OPENALEX_MAILTO", cfg.get("openalex_mailto", ""))

    print("Crossref:")
    for spec in sources.CROSSREF_QUERIES:
        items += fetch.fetch_crossref(spec, since, mailto=mailto)

    print("OpenAlex:")
    for query in sources.OPENALEX_QUERIES:
        items += fetch.fetch_openalex(query, since, mailto)

    print("GitHub releases:")
    token = os.environ.get("GITHUB_TOKEN", "")
    for repo in sources.GITHUB_REPOS:
        items += fetch.fetch_github_releases(repo, token)

    return items


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--days", type=int, default=None, help="lookback window")
    parser.add_argument("--min-score", type=int, default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--ignore-state", action="store_true",
                        help="do not filter against previously seen items")
    args = parser.parse_args()

    cfg = load_config()
    if args.days is not None:
        cfg["lookback_days"] = args.days
    if args.min_score is not None:
        cfg["min_score"] = args.min_score

    today = dt.date.today()
    since = today - dt.timedelta(days=cfg["lookback_days"])
    print(f"AI + materials digest for {today} (items since {since})\n")

    raw = collect(cfg, since)
    print(f"\nFetched {len(raw)} raw items")

    dated = [
        i for i in raw
        if not i["date"] or i["date"] >= since.isoformat()
    ]
    print(f"{len(dated)} within the {cfg['lookback_days']}-day window")

    unique = fetch.dedupe(dated)
    print(f"{len(unique)} after cross-source dedupe")

    seen = {} if args.ignore_state else state.load(STATE_PATH)
    fresh = state.filter_new(unique, seen)
    print(f"{len(fresh)} not previously reported")

    ranked = score.rank(fresh, cfg)
    print(f"{len(ranked)} cleared min_score={cfg['min_score']}")
    ranked = score.cap_per_section(ranked, cfg)
    print(f"{len(ranked)} kept after per-section caps; "
          "any overflow stays eligible on the next run\n")

    block = render.build_section(ranked, today, cfg)

    if args.dry_run:
        print(block)
        return 0

    render.prepend(DIGEST_PATH, block)
    state.mark(ranked, seen)
    state.save(STATE_PATH, seen)
    print(f"Wrote {len(ranked)} item(s) to {DIGEST_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
