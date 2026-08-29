"""Pull models, materials, calculation methods and metrics out of digest entries.

Reality check that shapes this module: paper abstracts state numbers only about
10% of the time, so most fields legitimately come back empty. Empty fields are
left blank in the summary table and listed in NEEDS_DATA.md for manual entry.
"""

from __future__ import annotations

import json
import os
import re
from typing import Dict, List, Optional, Tuple

from . import fetch

# ---------------------------------------------------------------------------
# Lexicons
# ---------------------------------------------------------------------------

# Seed list; the benchmark leaderboard model names are added at runtime.
MODEL_SEEDS = [
    "MatterGen", "MatterSim", "GNoME", "ALCHEMI", "Skala", "MACE", "CHGNet",
    "M3GNet", "NequIP", "Allegro", "SevenNet", "eSEN", "GRACE", "Orb", "OrbMol",
    "AIMNet2", "TensorNet", "ANI-2x", "ANI-1x", "DeePMD", "SchNet", "DimeNet",
    "GemNet", "PaiNN", "ALIGNN", "CGCNN", "MEGNet", "UMA", "EquiformerV2",
    "Equiformer", "MatGL", "CrystaLLM", "CDVAE", "DiffCSP", "FlowMM", "SyMat",
    "UniMat", "Graphormer", "AlphaFold", "GPT-4", "Llama", "Gemini", "Nemotron",
]

CALC_METHODS = [
    ("r2SCAN", r"r2?SCAN|r\$\^2\$SCAN"),
    ("PBE+U", r"PBE\s*\+\s*U|Hubbard\s+U|DFT\+U"),
    ("PBE", r"\bPBE\b|GGA-PBE"),
    ("HSE06", r"HSE06|\bHSE\b"),
    ("meta-GGA", r"meta-?GGA"),
    ("hybrid DFT", r"hybrid functional|B3LYP|PBE0"),
    ("GW", r"\bGW\b|G0W0"),
    ("CCSD(T)", r"CCSD\(?T\)?|coupled[- ]cluster"),
    ("DMFT", r"\bDMFT\b"),
    ("QMC", r"quantum Monte Carlo|\bQMC\b"),
    ("DFT", r"\bDFT\b|density functional theory|first[- ]principles|ab initio"),
    ("DFT-D3", r"DFT-?D3|D3 dispersion|Grimme"),
    ("AIMD", r"\bAIMD\b|ab initio molecular dynamics"),
    ("MD", r"molecular dynamics|\bMD simulation"),
    ("Monte Carlo", r"Monte Carlo|kinetic Monte Carlo|\bkMC\b"),
    ("phonons", r"phonon|phonopy|lattice dynamics|DFPT"),
    ("NEB", r"\bNEB\b|nudged elastic band"),
    ("tight-binding", r"tight[- ]binding|GFN2?-?xTB|\bDFTB\b"),
    ("MLIP", r"machine[- ]learn\w+ interatomic potential|\bMLIP\b|\bMLFF\b|"
             r"neural network potential|universal potential|foundation model"),
    ("free energy", r"free energy|thermodynamic integration|Gibbs"),
    ("finite element", r"finite element|\bFEM\b"),
]

MATERIAL_CLASSES = [
    ("perovskite", r"perovskite"),
    ("halide perovskite", r"halide perovskite"),
    ("solid electrolyte", r"solid[- ]state electrolyte|solid electrolyte|superionic"),
    ("Li-ion battery", r"lithium[- ]ion|Li-ion|cathode|anode|\bLiPF6\b"),
    ("catalyst", r"catalys[ti]|\bOER\b|\bHER\b|\bORR\b|electrocatalys"),
    ("MOF", r"\bMOFs?\b|metal[- ]organic framework"),
    ("zeolite", r"zeolite"),
    ("2D material", r"\b2D material|monolayer|graphene|MXene|van der Waals hetero"),
    ("alloy", r"\balloys?\b|high[- ]entropy alloy|\bHEA\b"),
    ("semiconductor", r"semiconductor|\bIII-V\b"),
    ("superconductor", r"superconduct"),
    ("thermoelectric", r"thermoelectric|\bZT\b"),
    ("photovoltaic", r"photovoltaic|solar cell"),
    ("magnetic material", r"magnetic material|ferromagnet|permanent magnet|magnetocalor"),
    ("oxide", r"\boxides?\b"),
    ("sulfide", r"\bsulfides?\b|chalcogenide"),
    ("nitride", r"\bnitrides?\b"),
    ("polymer", r"\bpolymers?\b"),
    ("glass / amorphous", r"amorphous|\bglass\b|glassy"),
    ("molecule / organic", r"organic molecul|drug-like|small molecul"),
    ("surface / slab", r"\bslab\b|surface adsorption|adsorbate"),
    ("high pressure", r"high[- ]pressure|\bGPa\b"),
]

ELEMENTS = set("""H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni
Cu Zn Ga Ge As Se Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba La Ce Pr Nd
Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn Fr Ra Ac Th Pa U
Np Pu Am Cm Bk Cf Es Fm Md No Lr""".split())

FORMULA_RE = re.compile(r"\b((?:[A-Z][a-z]?\d{0,3}){2,8})\b")

# ---------------------------------------------------------------------------
# Metric patterns. Each returns (label, value, unit).
# ---------------------------------------------------------------------------

# Order matters: the longest unit must come first, otherwise "eV/atom" is
# truncated to "eV/A" by the angstrom alternative.
UNIT = (r"meV\s*/?\s*atom|eV\s*/?\s*atom|meV\s*/?\s*(?:Å|A(?![a-z])|angstrom)|"
        r"eV\s*/?\s*(?:Å|A(?![a-z])|angstrom)|meV|eV|"
        r"kcal\s*/?\s*mol|kJ\s*/?\s*mol|mHa|GPa|%|K\b|W\s*/?\s*mK")

METRIC_PATTERNS = [
    ("MAE", re.compile(
        r"(?:MAE|mean absolute error)[^.;]{0,60}?(\d+(?:\.\d+)?)\s*(" + UNIT + r")", re.I)),
    ("MAE", re.compile(
        r"(\d+(?:\.\d+)?)\s*(" + UNIT + r")[^.;]{0,30}?(?:MAE|mean absolute error)", re.I)),
    ("RMSE", re.compile(
        r"(?:RMSE|root[- ]mean[- ]squared? error)[^.;]{0,60}?(\d+(?:\.\d+)?)\s*("
        + UNIT + r")", re.I)),
    ("accuracy", re.compile(
        r"accurac\w+[^.;]{0,50}?(\d+(?:\.\d+)?)\s*(%)", re.I)),
    ("accuracy", re.compile(
        r"(\d+(?:\.\d+)?)\s*(%)[^.;]{0,25}?accurac", re.I)),
    ("error", re.compile(
        r"error[^.;]{0,50}?(?:of|below|under|less than|within)?\s*(\d+(?:\.\d+)?)\s*("
        + UNIT + r")", re.I)),
    ("R2", re.compile(r"R\s*\^?\s*2[^.;]{0,40}?(\d\.\d+)()", re.I)),
    ("F1", re.compile(r"\bF1[^.;]{0,40}?(\d\.\d+)()", re.I)),
    ("success rate", re.compile(
        r"(?:success rate|hit rate|yield)[^.;]{0,40}?(\d+(?:\.\d+)?)\s*(%)", re.I)),
    ("speedup", re.compile(r"(\d+(?:,\d{3})*(?:\.\d+)?)\s*(?:x|-fold|times)\s*"
                          r"(?:faster|speed-?up|acceleration)()", re.I)),
]


def _model_pattern(name: str):
    """Word-boundary matcher for a model name.

    Substring matching is not safe here: 'eSEN' occurs inside 'present', 'UMA'
    inside 'human', 'Orb' inside 'absorb'. Short or all-caps names are therefore
    matched case-sensitively, longer ones case-insensitively.
    """
    escaped = re.escape(name).replace(r"\ ", r"[\s\-]+").replace(r"\-", r"[\s\-]?")
    pattern = r"(?<![A-Za-z0-9])" + escaped + r"(?![A-Za-z0-9])"
    short_or_acronym = len(name) <= 5 or name.isupper()
    return re.compile(pattern, 0 if short_or_acronym else re.I)


def build_model_lexicon(extra: List[str]) -> List[Tuple[str, object]]:
    names = set(MODEL_SEEDS)
    for name in extra:
        if name and len(name) > 2:
            names.add(name)
    # Longest first so "MACE-MPA-0" is preferred over bare "MACE".
    return [(n, _model_pattern(n)) for n in sorted(names, key=len, reverse=True)]


def find_models(text: str, lexicon: List[Tuple[str, object]]) -> List[str]:
    found: List[str] = []
    for name, pattern in lexicon:
        if not pattern.search(text):
            continue
        # Skip a shorter name already covered by a longer match (MACE vs MACE-MPA-0).
        if any(name.lower() in f.lower() for f in found):
            continue
        found.append(name)
    return found[:6]


def find_labelled(text: str, table) -> List[str]:
    out = []
    for label, pattern in table:
        if re.search(pattern, text, re.I):
            out.append(label)
    return out


def find_formulas(text: str) -> List[str]:
    out = []
    for match in FORMULA_RE.findall(text):
        symbols = re.findall(r"[A-Z][a-z]?", match)
        if len(symbols) < 2 or not all(s in ELEMENTS for s in symbols):
            continue
        if not re.search(r"\d", match):  # "CoO" style pairs are too ambiguous
            continue
        if match not in out:
            out.append(match)
    return out[:5]


# Generic "error" is only reported when no specific metric claimed the number.
LABEL_PRIORITY = {"MAE": 0, "RMSE": 0, "accuracy": 0, "R2": 0, "F1": 0,
                  "success rate": 0, "speedup": 0, "error": 1}


def find_metrics(text: str) -> List[Tuple[str, float, str]]:
    found: Dict[Tuple[float, str], Tuple[str, float, str]] = {}
    for label, pattern in METRIC_PATTERNS:
        for value, unit in pattern.findall(text):
            try:
                number = float(str(value).replace(",", ""))
            except ValueError:
                continue
            unit = re.sub(r"\s+", "", unit or "")
            if label == "speedup":
                unit = "x"
            key = (number, unit)
            existing = found.get(key)
            # Same number found by two patterns: keep the more specific label.
            if existing is None or LABEL_PRIORITY.get(label, 2) < LABEL_PRIORITY.get(
                    existing[0], 2):
                found[key] = (label, number, unit)
    return list(found.values())[:6]


# ---------------------------------------------------------------------------
# Digest parsing
# ---------------------------------------------------------------------------

ENTRY_RE = re.compile(
    r"^- \*\*\[(?P<title>.+?)\]\((?P<url>[^)]+)\)\*\*\s*\n"
    r"\s*<br>\*(?P<meta>.+?)\*\s*\n"
    r"(?P<body>(?:.*\n)*?)(?=^- \*\*\[|^#|^---|\Z)",
    re.M,
)


def parse_digest(path: str) -> List[Dict]:
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as fh:
        text = fh.read()

    entries = []
    for match in ENTRY_RE.finditer(text):
        meta = match.group("meta")
        doi_match = re.search(r"doi:(\S+)", meta)
        date_match = re.search(r"(\d{4}-\d{2}-\d{2})", meta)
        body = re.sub(r"`matched:[^`]*`", " ", match.group("body"))
        body = re.sub(r"<br>", " ", body)
        entries.append({
            "title": match.group("title").strip(),
            "url": match.group("url").strip(),
            "source": meta.split("|")[0].strip(),
            "date": date_match.group(1) if date_match else "",
            "doi": doi_match.group(1).rstrip(".,") if doi_match else "",
            "text": " ".join(body.split()),
        })
    return entries


# ---------------------------------------------------------------------------
# Abstract enrichment
# ---------------------------------------------------------------------------

def enrich(entries: List[Dict], cache_path: str, limit: int = 200) -> None:
    """Replace truncated digest summaries with full abstracts where possible."""
    cache: Dict[str, str] = {}
    if os.path.exists(cache_path):
        try:
            with open(cache_path, encoding="utf-8") as fh:
                cache = json.load(fh)
        except ValueError:
            cache = {}

    fetched = 0
    for entry in entries:
        doi = entry.get("doi")
        if not doi:
            continue
        if doi in cache:
            abstract = cache[doi]
        elif fetched >= limit:
            continue
        else:
            abstract = _fetch_abstract(doi)
            cache[doi] = abstract
            fetched += 1
        if abstract and len(abstract) > len(entry["text"]):
            entry["text"] = abstract

    os.makedirs(os.path.dirname(cache_path), exist_ok=True)
    with open(cache_path, "w", encoding="utf-8") as fh:
        json.dump(cache, fh, indent=0, sort_keys=True)
    print(f"  abstract cache: {len(cache)} DOIs ({fetched} newly fetched)")


def _fetch_abstract(doi: str) -> str:
    try:
        resp = fetch.get(f"https://api.crossref.org/works/{doi}",
                         headers={"Accept": "application/json"}, retries=2)
        if resp.status_code == 200:
            abstract = fetch.clean(resp.json()["message"].get("abstract", ""), 100000)
            if abstract:
                return abstract
    except Exception:
        pass
    try:
        resp = fetch.get(f"https://api.openalex.org/works/doi:{doi}",
                         headers={"Accept": "application/json"}, retries=2)
        if resp.status_code == 200:
            inv = resp.json().get("abstract_inverted_index")
            if inv:
                positions = {}
                for word, idxs in inv.items():
                    for i in idxs:
                        positions[i] = word
                return " ".join(positions[k] for k in sorted(positions))
    except Exception:
        pass
    return ""


# ---------------------------------------------------------------------------
# Study records
# ---------------------------------------------------------------------------

def sort_value(metrics: List[Tuple[str, float, str]]) -> Optional[float]:
    """A single comparable number: accuracy % where stated, else 100 - error %."""
    for label, value, unit in metrics:
        if label in ("accuracy", "success rate") and unit == "%":
            return value
    for label, value, unit in metrics:
        if label in ("error", "MAE", "RMSE") and unit == "%":
            return 100.0 - value
    for label, value, unit in metrics:
        if label in ("R2", "F1") and not unit:
            return value * 100.0
    return None


def _title_key(title: str) -> str:
    return re.sub(r"[^a-z0-9]", "", title.lower())


def build_studies(entries: List[Dict], lexicon: List[str]) -> List[Dict]:
    def has_doi(entry: Dict) -> bool:
        doi = entry.get("doi") or ""
        url = entry.get("url") or ""
        return (bool(doi) and doi.startswith("10.")) or "doi.org" in url

    # Prefer DOI-bearing records and longer abstracts, then drop title duplicates.
    def sort_key(entry: Dict):
        return (-int(has_doi(entry)), -len(entry.get("text", "")), entry.get("title", ""))

    studies = []
    seen = {}
    for entry in sorted(entries, key=sort_key):
        key = _title_key(entry["title"])
        if key in seen:
            continue
        text = entry["title"] + ". " + entry["text"]
        metrics = find_metrics(text)
        study = {
            "title": entry["title"],
            "url": entry["url"],
            "doi": entry["doi"],
            "date": entry["date"],
            "source": entry["source"],
            "models": find_models(text, lexicon),
            "materials": find_labelled(text, MATERIAL_CLASSES) + find_formulas(text),
            "methods": find_labelled(text, CALC_METHODS),
            "metrics": metrics,
            "sort_value": sort_value(metrics),
        }
        seen[key] = study
        studies.append(study)
    return studies
