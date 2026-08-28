#!/usr/bin/env python
"""Build the model-performance summary on top of the daily digest.

    python build_summary.py                # normal run
    python build_summary.py --refresh      # re-download the leaderboard metadata
    python build_summary.py --no-enrich    # skip abstract fetching (faster)
    python build_summary.py --docx         # also write .docx versions

Writes:
    MODEL_PERFORMANCE.md   sorted performance tables + figures
    NEEDS_DATA.md          every blank field, awaiting manual input
    charts/*.png           figures embedded in the summary
    data/model_performance.csv
"""

from __future__ import annotations

import argparse
import datetime as dt
import io
import json
import os
import sys

from agent import benchmarks, charts, extract, summary

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

ROOT = os.path.dirname(os.path.abspath(__file__))
DIGEST = os.path.join(ROOT, "DIGEST.md")
SUMMARY_MD = os.path.join(ROOT, "MODEL_PERFORMANCE.md")
NEEDS_MD = os.path.join(ROOT, "NEEDS_DATA.md")
MANUAL = os.path.join(ROOT, "manual_data.json")
CHARTS_DIR = os.path.join(ROOT, "charts")
BENCH_CACHE = os.path.join(ROOT, "data", "matbench_discovery.json")
ABSTRACT_CACHE = os.path.join(ROOT, "state", "abstracts.json")
CSV_OUT = os.path.join(ROOT, "data", "model_performance.csv")


def load_manual() -> dict:
    if not os.path.exists(MANUAL):
        return {}
    try:
        with open(MANUAL, encoding="utf-8") as fh:
            text = "\n".join(
                line for line in fh.read().splitlines()
                if not line.strip().startswith("//")
            )
            return json.loads(text) if text.strip() else {}
    except ValueError as exc:
        print(f"! manual_data.json is not valid JSON ({exc}); ignoring it")
        return {}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--refresh", action="store_true",
                        help="re-download Matbench Discovery model metadata")
    parser.add_argument("--no-enrich", action="store_true",
                        help="do not fetch full abstracts for digest entries")
    parser.add_argument("--enrich-limit", type=int, default=200)
    parser.add_argument("--docx", action="store_true")
    args = parser.parse_args()

    today = dt.date.today()
    print(f"Building performance summary for {today}\n")

    print("1. Benchmark leaderboard")
    models = benchmarks.load(BENCH_CACHE, refresh=args.refresh)
    print(f"   {len(models)} models loaded")

    print("2. Digest entries")
    entries = extract.parse_digest(DIGEST)
    print(f"   {len(entries)} entries parsed from DIGEST.md")
    if entries and not args.no_enrich:
        print("   fetching full abstracts (metrics are rarely in the digest excerpt)")
        extract.enrich(entries, ABSTRACT_CACHE, limit=args.enrich_limit)

    lexicon = extract.build_model_lexicon([m["model"] for m in models])
    studies = extract.build_studies(entries, lexicon)
    with_numbers = sum(1 for s in studies if s.get("sort_value") is not None)
    print(f"   {len(studies)} studies; {with_numbers} with a numeric metric")

    print("3. Manual overrides")
    manual = load_manual()
    summary.apply_manual(models, studies, manual)
    print(f"   {len(manual.get('models', {}))} model and "
          f"{len(manual.get('studies', {}))} study override(s) applied")

    print("4. Figures")
    chart_list, tiers = charts.build_all(models, studies, CHARTS_DIR)

    print("5. Documents")
    with open(SUMMARY_MD, "w", encoding="utf-8") as fh:
        fh.write(summary.render_summary(models, studies, chart_list, tiers, today))
    print(f"   {SUMMARY_MD}")

    with open(NEEDS_MD, "w", encoding="utf-8") as fh:
        fh.write(summary.render_needs_data(models, studies, today))
    print(f"   {NEEDS_MD}")

    summary.write_csv(models, CSV_OUT)
    print(f"   {CSV_OUT}")

    if args.docx:
        sys.path.insert(0, os.path.join(ROOT, "tools"))
        try:
            from md2docx import convert
            convert(SUMMARY_MD, SUMMARY_MD.replace(".md", ".docx"))
            convert(NEEDS_MD, NEEDS_MD.replace(".md", ".docx"))
        except ImportError:
            print("   ! python-docx not installed; skipping .docx output")

    return 0


if __name__ == "__main__":
    sys.exit(main())
