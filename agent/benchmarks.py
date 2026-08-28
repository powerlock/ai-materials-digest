"""Quantitative model performance from the Matbench Discovery leaderboard.

Why this source: MAE / RMSE / R2 / accuracy numbers almost never appear in paper
abstracts (they live in full-text tables, usually paywalled). Matbench Discovery
publishes them as structured YAML, one file per model, each with a DOI, the
training sets, the architecture and the evaluation task. That makes it the only
honest way to build a *sortable* performance table automatically.

Repo: https://github.com/janosh/matbench-discovery (CC-BY-4.0 data)
"""

from __future__ import annotations

import json
import os
from typing import Dict, List, Optional

import yaml

from . import fetch

REPO = "janosh/matbench-discovery"
TREE_URL = f"https://api.github.com/repos/{REPO}/git/trees/main?recursive=1"
RAW = f"https://raw.githubusercontent.com/{REPO}/main/"

# Test sets used by each metric group, so the table can state what was tested.
TEST_SETS = {
    "discovery": "WBM (unique prototypes), inorganic crystals vs MP convex hull",
    "phonons": "PhononDB / MDR phonon set",
    "geo_opt": "MP relaxed structures (geometry optimisation)",
    "diatomics": "Homonuclear diatomic curves (PBE reference)",
    "md": "MD stability suite",
}

TRAIN_TASK_METHODS = {
    "S2EFS": "DFT single-point + relaxation: energy, forces, stress",
    "S2EFSM": "DFT energy, forces, stress, magmoms",
    "S2EFS_G": "DFT energy, forces, stress + graph targets",
    "S2RE": "structure to relaxed energy",
    "RS2RE": "relaxed structure to relaxed energy",
    "IS2RE": "initial structure to relaxed energy",
    "IS2E": "initial structure to energy",
    "RP2RE": "relaxed prototype to relaxed energy",
}

# Reference level of theory implied by the training set.
TRAIN_SET_DFT = {
    "MPtrj": "DFT PBE(+U), Materials Project settings",
    "sAlex": "DFT PBE(+U), Alexandria",
    "Alex": "DFT PBE(+U), Alexandria",
    "OMat24": "DFT PBE(+U), OMat24",
    "OMAT24": "DFT PBE(+U), OMat24",
    "MP+Alex": "DFT PBE(+U)",
    "MPF": "DFT PBE(+U), MPF2021",
    "MP-2022": "DFT PBE(+U), Materials Project",
    "sAlex+MPtrj": "DFT PBE(+U)",
    "OMat24+MPtrj": "DFT PBE(+U)",
    "MatPES": "DFT PBE and r2SCAN, MatPES",
}


def _list_model_files() -> List[str]:
    resp = fetch.get(TREE_URL, headers={"Accept": "application/json"})
    resp.raise_for_status()
    tree = resp.json()["tree"]
    return [
        t["path"]
        for t in tree
        if t["path"].startswith("models/")
        and t["path"].endswith((".yml", ".yaml"))
        and t["path"].count("/") == 2
    ]


def _num(value) -> Optional[float]:
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _find_nested(node, suffix: str, depth: int = 4) -> Optional[float]:
    """Depth-first search for a numeric value whose key ends with `suffix`.

    Tolerates the leaderboard's Unicode metric names (κ_SRME, κ_SRE) and the
    extra nesting level it uses for phonon sub-benchmarks.
    """
    if depth < 0 or not isinstance(node, dict):
        return None
    for key, value in node.items():
        name = str(key).lower().replace("κ", "kappa").strip("_ ")
        if name.endswith(suffix) and not isinstance(value, (dict, list)):
            number = _num(value)
            if number is not None:
                return number
    for value in node.values():
        found = _find_nested(value, suffix, depth - 1)
        if found is not None:
            return found
    return None


def _normalise(doc: Dict) -> Optional[Dict]:
    if not isinstance(doc, dict) or not doc.get("model_name"):
        return None

    metrics = doc.get("metrics") or {}
    discovery = metrics.get("discovery") or {}
    # `unique_prototypes` is the leaderboard's headline split (no train/test leakage).
    disc = discovery.get("unique_prototypes") or discovery.get("full_test_set") or {}
    phonons = metrics.get("phonons") or {}
    geo = metrics.get("geo_opt") or {}

    # The leaderboard writes this key with a literal Greek kappa ("κ_SRME") and
    # nests it under a sub-key such as "kappa_103", so search by suffix.
    kappa = _find_nested(phonons, "srme")

    rmsd = symmetry = None
    if isinstance(geo, dict):
        for key, value in geo.items():
            if isinstance(value, dict) and "rmsd" in value:
                rmsd = _num(value.get("rmsd"))
                symmetry = _num(value.get("symmetry_match"))
                break

    training = doc.get("training_sets") or doc.get("training_set") or []
    if isinstance(training, str):
        training = [training]
    training = [str(t) for t in training]

    dft = ""
    for name in training:
        if name in TRAIN_SET_DFT:
            dft = TRAIN_SET_DFT[name]
            break
    if not dft and training:
        dft = "DFT (see training set)"

    task = doc.get("train_task") or ""
    dates = doc.get("dates") or {}
    arch = doc.get("architecture_types") or []
    if isinstance(arch, str):
        arch = [arch]

    accuracy = _num(disc.get("Accuracy"))
    mae = _num(disc.get("MAE"))

    return {
        "model": doc["model_name"],
        "key": doc.get("model_key", ""),
        "architecture": ", ".join(arch),
        "params": doc.get("model_params"),
        "openness": doc.get("openness", ""),
        "train_task": task,
        "targets": doc.get("targets", ""),
        "training_sets": ", ".join(training),
        "calc_method": "; ".join(
            p for p in [dft, TRAIN_TASK_METHODS.get(task, task)] if p
        ),
        "materials_tested": TEST_SETS["discovery"] if disc else "",
        "date": (dates.get("paper_published") or dates.get("benchmark_added") or ""),
        "doi": (doc.get("doi") or "").replace("https://doi.org/", ""),
        "paper": doc.get("paper", ""),
        "repo": doc.get("repo", ""),
        "license": ((doc.get("license") or {}).get("code") or ""),
        # Performance
        "accuracy_pct": round(accuracy * 100, 2) if accuracy is not None else None,
        "f1": _num(disc.get("F1")),
        "precision": _num(disc.get("Precision")),
        "recall": _num(disc.get("Recall")),
        "mae_mev_atom": round(mae * 1000, 1) if mae is not None else None,
        "rmse_mev_atom": (
            round(_num(disc.get("RMSE")) * 1000, 1)
            if _num(disc.get("RMSE")) is not None else None
        ),
        "r2": _num(disc.get("R2")),
        "daf": _num(disc.get("DAF")),
        "kappa_srme": kappa,
        "geo_opt_rmsd": rmsd,
        "symmetry_match": symmetry,
        "source": "Matbench Discovery",
    }


def load(cache_path: str, refresh: bool = False) -> List[Dict]:
    """Return normalised model records, using the on-disk cache when possible."""
    if os.path.exists(cache_path) and not refresh:
        with open(cache_path, encoding="utf-8") as fh:
            return json.load(fh)

    print("Fetching Matbench Discovery model metadata (65-ish YAML files)...")
    records = []
    for path in _list_model_files():
        try:
            resp = fetch.get(RAW + path)
            resp.raise_for_status()
            record = _normalise(yaml.safe_load(resp.text))
        except Exception as exc:
            print(f"  ! {path}: {type(exc).__name__}: {exc}")
            continue
        if record:
            records.append(record)
            print(f"  - {record['model']}")

    os.makedirs(os.path.dirname(cache_path), exist_ok=True)
    with open(cache_path, "w", encoding="utf-8") as fh:
        json.dump(records, fh, indent=1, sort_keys=True)
    print(f"Cached {len(records)} model records in {cache_path}")
    return records
