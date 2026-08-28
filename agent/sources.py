"""Source definitions for the AI + materials discovery digest.

Every URL here was probed and confirmed reachable. Publishers behind Cloudflare
(ACS, RSC, the ChemRxiv REST API) return HTTP 403 to scripted clients, so their
content is picked up through Crossref and OpenAlex DOI queries instead.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# RSS / RDF / Atom feeds: (label, url, section, source_bonus)
# ---------------------------------------------------------------------------

JOURNAL_FEEDS = [
    ("Nature", "https://www.nature.com/nature.rss", "journals", 4),
    ("Science", "https://www.science.org/rss/news_current.xml", "journals", 4),
    ("Nature Materials", "https://www.nature.com/nmat.rss", "journals", 4),
    ("Nature Chemistry", "https://www.nature.com/nchem.rss", "journals", 3),
    ("Nature Energy", "https://www.nature.com/nenergy.rss", "journals", 3),
    ("Nature Nanotechnology", "https://www.nature.com/nnano.rss", "journals", 2),
    ("Nature Synthesis", "https://www.nature.com/natsynth.rss", "journals", 3),
    ("Nature Computational Science", "https://www.nature.com/natcomputsci.rss", "journals", 3),
    ("Nature Reviews Materials", "https://www.nature.com/natrevmats.rss", "journals", 3),
    ("npj Computational Materials", "https://www.nature.com/npjcompumats.rss", "journals", 3),
    ("Nature Communications", "https://www.nature.com/ncomms.rss", "journals", 1),
    ("Matter", "https://www.cell.com/matter/inpress.rss", "journals", 2),
    ("Joule", "https://www.cell.com/joule/inpress.rss", "journals", 2),
]

BLOG_FEEDS = [
    ("NVIDIA Developer Blog", "https://developer.nvidia.com/blog/feed", "industry", 3),
    ("NVIDIA Blog", "https://blogs.nvidia.com/feed/", "industry", 1),
    ("Microsoft Research", "https://www.microsoft.com/en-us/research/feed/", "industry", 3),
    ("Google DeepMind", "https://deepmind.google/blog/rss.xml", "industry", 3),
]

# ---------------------------------------------------------------------------
# arXiv API queries. Conference acceptances are detected from the <comment>
# field (authors routinely write "accepted at NeurIPS 2026" there).
# ---------------------------------------------------------------------------

ARXIV_QUERIES = [
    'cat:cond-mat.mtrl-sci AND (abs:"machine learning" OR abs:"deep learning" '
    'OR abs:"neural network" OR abs:"generative model" OR abs:"foundation model")',
    'cat:physics.chem-ph AND (abs:"machine learning" OR abs:"interatomic potential" '
    'OR abs:"neural network")',
    'cat:cs.LG AND (abs:"materials discovery" OR abs:"crystal structure" '
    'OR abs:"interatomic potential" OR abs:"molecular dynamics")',
    'abs:"crystal structure prediction" OR abs:"machine learning interatomic potential" '
    'OR abs:"autonomous laboratory" OR abs:"self-driving laboratory"',
]

# ---------------------------------------------------------------------------
# Crossref queries. `prefix:10.26434` is ChemRxiv.
# ---------------------------------------------------------------------------

CROSSREF_QUERIES = [
    {"query": "machine learning materials discovery"},
    {"query": "machine learning interatomic potential"},
    {"query": "generative model inorganic crystal design"},
    {"query": "autonomous laboratory materials synthesis"},
    {"query": "machine learning materials", "filter_extra": "prefix:10.26434"},
]

# ---------------------------------------------------------------------------
# OpenAlex searches (polite pool; set OPENALEX_MAILTO for a better rate limit).
# ---------------------------------------------------------------------------

OPENALEX_QUERIES = [
    "machine learning interatomic potential",
    "generative model materials discovery",
    "crystal structure prediction deep learning",
    "autonomous laboratory materials synthesis",
]

# ---------------------------------------------------------------------------
# Code releases worth knowing about the day they ship.
# ---------------------------------------------------------------------------

GITHUB_REPOS = [
    "microsoft/mattergen",
    "microsoft/mattersim",
    "microsoft/skala",
    "google-deepmind/materials_discovery",
    "NVIDIA/nvalchemi-toolkit",
    "NVIDIA/nvalchemi-toolkit-ops",
    "ACEsuit/mace",
    "CederGroupHub/alabos",
    "materialsproject/pymatgen",
]
