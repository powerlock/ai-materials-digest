"""Render MODEL_PERFORMANCE.md (sorted tables + charts) and NEEDS_DATA.md."""

from __future__ import annotations

import csv
import datetime as dt
import os
from typing import Dict, List, Optional

BLANK = ""


def _fmt(value, digits: int = 3, suffix: str = "") -> str:
    if value is None or value == "":
        return BLANK
    if isinstance(value, float):
        text = f"{value:.{digits}f}".rstrip("0").rstrip(".")
        return text + suffix
    return f"{value}{suffix}"


def _params(value) -> str:
    if not value:
        return BLANK
    try:
        n = int(value)
    except (TypeError, ValueError):
        return str(value)
    if n >= 1_000_000:
        return f"{n / 1_000_000:.1f}M"
    return f"{n / 1000:.0f}k"


def _doi_cell(record: Dict) -> str:
    doi = record.get("doi") or ""
    if doi:
        return f"[{doi}](https://doi.org/{doi})"
    url = record.get("paper") or record.get("url") or record.get("repo") or ""
    return f"[link]({url})" if url else BLANK


def sort_models(models: List[Dict]) -> List[Dict]:
    """Accuracy descending, then MAE ascending. Models with no metrics go last."""
    def key(m):
        acc = m.get("accuracy_pct")
        mae = m.get("mae_mev_atom")
        return (
            0 if acc is not None else 1,
            -(acc if acc is not None else 0),
            mae if mae is not None else float("inf"),
        )
    return sorted(models, key=key)


def sort_studies(studies: List[Dict]) -> List[Dict]:
    def key(s):
        value = s.get("sort_value")
        return (0 if value is not None else 1, -(value if value is not None else 0),
                s.get("date") or "")
    return sorted(studies, key=key)


# ---------------------------------------------------------------------------
# Main summary document
# ---------------------------------------------------------------------------

def render_summary(models: List[Dict], studies: List[Dict], charts,
                   tiers: Dict[str, int], generated: dt.date) -> str:
    models = sort_models(models)
    studies = sort_studies(studies)
    with_metrics = [m for m in models if m.get("accuracy_pct") is not None]

    out = [
        "# AI Models for Materials Discovery - Performance Summary",
        "",
        f"Generated {generated.isoformat()} by `build_summary.py`. "
        "Rows are ordered by reported accuracy (descending), then by error "
        "(ascending) - not chronologically. Blank cells mean the value was not "
        "published in a machine-readable form; every blank is itemised in "
        "[NEEDS_DATA.md](NEEDS_DATA.md).",
        "",
        "## How to read this document",
        "",
        "Two tables, two very different evidentiary standards:",
        "",
        "1. **Table 1** comes from the Matbench Discovery leaderboard, where every "
        "model is evaluated on the *same* held-out test set with the *same* DFT "
        "reference. These numbers are directly comparable.",
        "2. **Table 2** comes from the daily digest, i.e. whatever the literature "
        "published this week. Each study uses its own test set and its own "
        "definition of error, so those numbers are **not** comparable to each "
        "other. Treat Table 2 as a lead list, not a ranking.",
        "",
    ]

    if with_metrics:
        best = with_metrics[0]
        lowest = min(with_metrics, key=lambda m: m["mae_mev_atom"] or 1e9)
        out += [
            "## Headline numbers",
            "",
            f"- **{len(models)}** models tracked, **{len(with_metrics)}** with "
            "comparable accuracy figures.",
            f"- Highest stability-classification accuracy: **{best['model']}** at "
            f"**{best['accuracy_pct']}%** (F1 {_fmt(best.get('f1'))}).",
            f"- Lowest energy error: **{lowest['model']}** at "
            f"**{_fmt(lowest.get('mae_mev_atom'), 1)} meV/atom**.",
            f"- **{len(studies)}** studies parsed from the digest; "
            f"**{sum(1 for s in studies if s.get('sort_value') is not None)}** "
            "reported a numeric performance figure in the abstract.",
            "",
        ]

    if charts:
        out += ["## Figures", ""]
        for path, caption in charts:
            rel = path.replace("\\", "/")
            rel = rel[rel.find("charts/"):] if "charts/" in rel else rel
            out += [f"**{caption}**", "", f"![{caption}]({rel})", ""]

    # ---------------- Table 1 ----------------
    out += [
        "## Table 1 - Benchmarked models, ranked by accuracy",
        "",
        "Source: [Matbench Discovery](https://github.com/janosh/matbench-discovery) "
        "(CC-BY-4.0). Test set: WBM unique prototypes, ~215k inorganic crystals, "
        "scored against the Materials Project PBE convex hull. "
        "`kSRME` is the phonon thermal-conductivity error (lower is better); it is "
        "blank for models that were never evaluated on it.",
        "",
        "| # | Model | Acc. (%) | MAE (meV/atom) | RMSE (meV/atom) | F1 | R2 | kSRME | "
        "Tier | Architecture | Params | Calculation method / reference | "
        "Materials tested | Training set | Date | DOI |",
        "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for i, m in enumerate(models, 1):
        tier = tiers.get(m["model"])
        out.append(
            f"| {i} | **{m['model']}** | {_fmt(m.get('accuracy_pct'), 2)} | "
            f"{_fmt(m.get('mae_mev_atom'), 1)} | {_fmt(m.get('rmse_mev_atom'), 1)} | "
            f"{_fmt(m.get('f1'))} | {_fmt(m.get('r2'))} | {_fmt(m.get('kappa_srme'))} | "
            f"{tier if tier else BLANK} | {m.get('architecture') or BLANK} | "
            f"{_params(m.get('params'))} | {m.get('calc_method') or BLANK} | "
            f"{m.get('materials_tested') or BLANK} | {m.get('training_sets') or BLANK} | "
            f"{m.get('date') or BLANK} | {_doi_cell(m)} |"
        )

    # ---------------- Table 2 ----------------
    out += [
        "",
        "## Table 2 - Studies from the daily digest",
        "",
        "Extracted automatically from titles and abstracts. Ordered by the numeric "
        "figure found (accuracy %, or 100 - error %, or R2/F1 x 100), then blanks. "
        "**Caveat:** abstracts state a numeric performance figure only about 10% of "
        "the time, so most metric cells are blank by necessity, not by oversight.",
        "",
        "| # | Sort value | Study | Models named | Materials / systems | "
        "Calculation method | Metrics found | Date | DOI |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for i, s in enumerate(studies, 1):
        metrics = "; ".join(
            f"{label} {_fmt(value)}{(' ' + unit) if unit else ''}"
            for label, value, unit in s.get("metrics", [])
        )
        title = s["title"].replace("|", "/")[:150]
        out.append(
            f"| {i} | {_fmt(s.get('sort_value'), 1)} | [{title}]({s['url']}) | "
            f"{', '.join(s.get('models', [])) or BLANK} | "
            f"{', '.join(s.get('materials', [])[:5]) or BLANK} | "
            f"{', '.join(s.get('methods', [])[:5]) or BLANK} | {metrics or BLANK} | "
            f"{s.get('date') or BLANK} | {_doi_cell(s)} |"
        )

    out += [
        "",
        "## Provenance and honest limitations",
        "",
        "- **Why two sources.** MAE/RMSE values are published in full-text tables, "
        "not abstracts. Testing 12 digest DOIs, only 1 exposed a usable numeric "
        "metric in its abstract. A table built solely from abstracts would be "
        "almost entirely blank, so the leaderboard supplies the comparable numbers "
        "and the digest supplies the leading edge.",
        "- **Accuracy here means stability classification accuracy** (is this "
        "structure on or below the convex hull?), not a chemical accuracy claim.",
        "- **Tiers** come from k-means (k=3) on [MAE, accuracy, F1, R2], ordered by "
        "mean MAE. Tier 1 is best. They are a descriptive grouping, not a ranking "
        "endorsed by the benchmark authors.",
        "- **Table 2 extraction is regex-based.** It will miss models it has never "
        "heard of and can mis-attribute a number to the wrong quantity. Verify "
        "anything you intend to cite.",
        "- Values you enter in `manual_data.json` override everything above and "
        "survive future runs.",
        "",
    ]
    return "\n".join(out) + "\n"


# ---------------------------------------------------------------------------
# Needs-data document
# ---------------------------------------------------------------------------

MODEL_FIELDS = [
    ("accuracy_pct", "Accuracy (%)"),
    ("mae_mev_atom", "MAE (meV/atom)"),
    ("rmse_mev_atom", "RMSE (meV/atom)"),
    ("f1", "F1"),
    ("r2", "R2"),
    ("kappa_srme", "Phonon kSRME"),
    ("geo_opt_rmsd", "Geometry-opt RMSD"),
    ("params", "Parameter count"),
    ("training_sets", "Training set"),
    ("calc_method", "Calculation method"),
    ("date", "Publication date"),
    ("doi", "DOI"),
]


def render_needs_data(models: List[Dict], studies: List[Dict],
                      generated: dt.date) -> str:
    out = [
        "# Needs data - awaiting further input",
        "",
        f"Generated {generated.isoformat()}. Every field below was blank in the "
        "automated sources. Fill any of them in `manual_data.json` and rerun "
        "`python build_summary.py`; your values take priority and are never "
        "overwritten.",
        "",
        "```jsonc",
        "// manual_data.json",
        "{",
        '  "models": {',
        '    "MACE-MPA-0": { "kappa_srme": 0.412, "notes": "from Table 2 of the paper" }',
        "  },",
        '  "studies": {',
        '    "10.1038/s41586-025-08628-5": {',
        '      "models": ["MatterGen"],',
        '      "materials": ["TaCr2O6"],',
        '      "methods": ["DFT", "solid-state synthesis"],',
        '      "metrics": [["bulk modulus error", 20, "%"]],',
        '      "sort_value": 80',
        "    }",
        "  }",
        "}",
        "```",
        "",
    ]

    incomplete = []
    for m in sort_models(models):
        missing = [label for field, label in MODEL_FIELDS if not m.get(field)]
        if missing:
            incomplete.append((m, missing))

    out += [
        f"## Models with missing fields ({len(incomplete)} of {len(models)})",
        "",
        "| Model | Missing fields | DOI | Repo |",
        "|---|---|---|---|",
    ]
    for m, missing in incomplete:
        out.append(
            f"| **{m['model']}** | {', '.join(missing)} | {_doi_cell(m)} | "
            f"{('[repo](' + m['repo'] + ')') if m.get('repo') else BLANK} |"
        )
    if not incomplete:
        out.append("| _none_ | | | |")

    no_metric = [s for s in studies if s.get("sort_value") is None]
    no_model = [s for s in studies if not s.get("models")]
    no_method = [s for s in studies if not s.get("methods")]

    out += [
        "",
        "## Studies with no numeric performance figure "
        f"({len(no_metric)} of {len(studies)})",
        "",
        "These need a human to open the paper and read the results table. Highest "
        "value first: studies that already name a model and a material, so only the "
        "number is missing.",
        "",
        "| Study | Models named | Materials | Method | Date | DOI |",
        "|---|---|---|---|---|---|",
    ]
    ordered = sorted(
        no_metric,
        key=lambda s: (not s.get("models"), not s.get("materials"), s.get("date") or ""),
    )
    for s in ordered:
        out.append(
            f"| [{s['title'].replace('|', '/')[:120]}]({s['url']}) | "
            f"{', '.join(s.get('models', [])) or BLANK} | "
            f"{', '.join(s.get('materials', [])[:4]) or BLANK} | "
            f"{', '.join(s.get('methods', [])[:4]) or BLANK} | "
            f"{s.get('date') or BLANK} | {_doi_cell(s)} |"
        )

    out += [
        "",
        "## Summary of gaps",
        "",
        f"- Studies with no identifiable model name: **{len(no_model)}**",
        f"- Studies with no identifiable calculation method: **{len(no_method)}**",
        f"- Studies with no numeric metric: **{len(no_metric)}**",
        f"- Benchmarked models missing at least one field: **{len(incomplete)}**",
        "",
        "The dominant cause is structural, not fixable by better parsing: "
        "abstracts rarely quote error values, and full text is usually paywalled.",
        "",
    ]
    return "\n".join(out) + "\n"


# ---------------------------------------------------------------------------
# CSV export
# ---------------------------------------------------------------------------

CSV_COLUMNS = [
    "model", "accuracy_pct", "mae_mev_atom", "rmse_mev_atom", "f1", "r2",
    "precision", "recall", "daf", "kappa_srme", "geo_opt_rmsd", "symmetry_match",
    "architecture", "params", "openness", "license", "train_task", "targets",
    "training_sets", "calc_method", "materials_tested", "date", "doi", "repo",
    "source",
]


def write_csv(models: List[Dict], path: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=CSV_COLUMNS, extrasaction="ignore")
        writer.writeheader()
        for m in sort_models(models):
            writer.writerow(m)


def apply_manual(models: List[Dict], studies: List[Dict], manual: Dict) -> None:
    """User-supplied values win over anything scraped."""
    model_overrides = manual.get("models") or {}
    for m in models:
        for key, value in (model_overrides.get(m["model"]) or {}).items():
            m[key] = value

    study_overrides = manual.get("studies") or {}
    for s in studies:
        override = study_overrides.get(s.get("doi") or "") or {}
        for key, value in override.items():
            if key == "metrics" and isinstance(value, list):
                s["metrics"] = [tuple(v) for v in value]
            else:
                s[key] = value
        if override and s.get("sort_value") is None:
            from .extract import sort_value
            s["sort_value"] = sort_value(s.get("metrics", []))
