"""HTTP fetchers and feed parsing. Only dependency is `requests`.

RSS 2.0, RSS 1.0 (RDF, used by Nature/Science/Cell) and Atom are all handled by
the same parser, so no feedparser install is needed.
"""

from __future__ import annotations

import datetime as dt
import re
import time
import xml.etree.ElementTree as ET
from typing import Dict, Iterable, List, Optional
from urllib.parse import quote_plus

import requests

USER_AGENT = (
    "ai-materials-digest/1.0 (daily research digest; +https://github.com/)"
)
TIMEOUT = 40

NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "rss1": "http://purl.org/rss/1.0/",
    "dc": "http://purl.org/dc/elements/1.1/",
    "prism": "http://prismstandard.org/namespaces/basic/2.0/",
    "arxiv": "http://arxiv.org/schemas/atom",
}

TAG_RE = re.compile(r"<[^>]+>")
WS_RE = re.compile(r"\s+")


def clean(text: Optional[str], limit: int = 700) -> str:
    if not text:
        return ""
    text = TAG_RE.sub(" ", text)
    text = (
        text.replace("&amp;", "&")
        .replace("&lt;", "<")
        .replace("&gt;", ">")
        .replace("&#39;", "'")
        .replace("&quot;", '"')
        .replace("&nbsp;", " ")
    )
    text = WS_RE.sub(" ", text).strip()
    return text[:limit].rstrip() + ("..." if len(text) > limit else "")


def get(url: str, headers: Optional[Dict[str, str]] = None, retries: int = 3, **kwargs):
    """GET with polite exponential backoff on rate limits and 5xx."""
    h = {"User-Agent": USER_AGENT, "Accept": "*/*"}
    if headers:
        h.update(headers)
    delay = 4
    for attempt in range(retries):
        resp = requests.get(url, headers=h, timeout=TIMEOUT, **kwargs)
        if resp.status_code in (429, 500, 502, 503, 504) and attempt < retries - 1:
            wait = int(resp.headers.get("Retry-After", delay))
            print(f"    ({resp.status_code}, waiting {wait}s)")
            time.sleep(min(wait, 30))
            delay *= 2
            continue
        return resp
    return resp


def parse_date(value: Optional[str]) -> Optional[dt.date]:
    if not value:
        return None
    value = value.strip()
    fmts = (
        "%a, %d %b %Y %H:%M:%S %z",
        "%a, %d %b %Y %H:%M:%S %Z",
        "%a, %d %b %Y %H:%M:%S",
        "%Y-%m-%dT%H:%M:%S%z",
        "%Y-%m-%dT%H:%M:%SZ",
        "%Y-%m-%dT%H:%M:%S",
        "%Y-%m-%d",
    )
    for fmt in fmts:
        try:
            return dt.datetime.strptime(value.replace("GMT", "+0000"), fmt).date()
        except ValueError:
            continue
    m = re.search(r"(\d{4})-(\d{2})-(\d{2})", value)
    if m:
        return dt.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    return None


def _text(elem, *paths) -> Optional[str]:
    for path in paths:
        found = elem.find(path, NS)
        if found is not None:
            if found.text and found.text.strip():
                return found.text
            href = found.get("href")
            if href:
                return href
    return None


def make_item(
    title: str,
    url: str,
    summary: str,
    date: Optional[dt.date],
    source: str,
    section: str,
    bonus: int = 0,
    doi: Optional[str] = None,
    extra: str = "",
) -> Dict:
    return {
        "title": clean(title, 300),
        "url": (url or "").strip(),
        "summary": clean(summary),
        "date": date.isoformat() if date else "",
        "source": source,
        "section": section,
        "bonus": bonus,
        "doi": (doi or "").lower().replace("https://doi.org/", "").strip(),
        "extra": extra,
    }


# ---------------------------------------------------------------------------
# Generic feeds
# ---------------------------------------------------------------------------

def fetch_feed(label: str, url: str, section: str, bonus: int) -> List[Dict]:
    try:
        resp = get(url)
        resp.raise_for_status()
        root = ET.fromstring(resp.content)
    except Exception as exc:  # a dead feed must never kill the run
        print(f"  ! {label}: {type(exc).__name__}: {exc}")
        return []

    entries = (
        root.findall(".//item")
        or root.findall(".//rss1:item", NS)
        or root.findall(".//atom:entry", NS)
    )
    items = []
    for entry in entries:
        title = _text(entry, "title", "rss1:title", "atom:title") or ""
        link = _text(entry, "link", "rss1:link", "atom:link") or ""
        summary = (
            _text(
                entry,
                "description",
                "rss1:description",
                "atom:summary",
                "content",
                "atom:content",
                "dc:description",
            )
            or ""
        )
        date = parse_date(
            _text(entry, "pubDate", "dc:date", "atom:published", "atom:updated", "prism:publicationDate")
        )
        doi = _text(entry, "prism:doi", "dc:identifier")
        if doi and not doi.startswith("10."):
            doi = None
        if title:
            items.append(make_item(title, link, summary, date, label, section, bonus, doi))
    print(f"  - {label}: {len(items)} entries")
    return items


# ---------------------------------------------------------------------------
# arXiv
# ---------------------------------------------------------------------------

CONFERENCE_RE = re.compile(
    r"\b(NeurIPS|ICLR|ICML|AAAI|KDD|CVPR|MRS (?:Spring|Fall)?\s*Meeting|"
    r"ACS (?:Spring|Fall)\s*\d{4}|APS March Meeting|AISTATS|IJCAI)\b",
    re.I,
)


def fetch_arxiv(query: str, max_results: int = 60) -> List[Dict]:
    url = (
        "http://export.arxiv.org/api/query?search_query="
        + quote_plus(query)
        + f"&sortBy=submittedDate&sortOrder=descending&max_results={max_results}"
    )
    try:
        resp = get(url)
        resp.raise_for_status()
        root = ET.fromstring(resp.content)
    except Exception as exc:
        print(f"  ! arXiv query failed: {type(exc).__name__}: {exc}")
        return []

    items = []
    for entry in root.findall("atom:entry", NS):
        title = _text(entry, "atom:title") or ""
        summary = _text(entry, "atom:summary") or ""
        link = _text(entry, "atom:id") or ""
        date = parse_date(_text(entry, "atom:published"))
        comment = _text(entry, "arxiv:comment") or ""
        doi = _text(entry, "arxiv:doi")
        authors = [
            (a.findtext("atom:name", "", NS) or "").strip()
            for a in entry.findall("atom:author", NS)
        ]
        conf = CONFERENCE_RE.search(comment)
        section = "conferences" if conf else "preprints"
        extra = f"Accepted/presented: {conf.group(0)}" if conf else ""
        if authors:
            extra = (extra + " | " if extra else "") + ", ".join(authors[:4]) + (
                " et al." if len(authors) > 4 else ""
            )
        item = make_item(title, link, summary, date, "arXiv", section, 1, doi, extra)
        if conf:
            item["bonus"] += 3
        items.append(item)
    time.sleep(3)  # arXiv API asks for one request per 3 seconds
    print(f"  - arXiv ({query[:40]}...): {len(items)} entries")
    return items


# ---------------------------------------------------------------------------
# Crossref
# ---------------------------------------------------------------------------

def fetch_crossref(spec: Dict, since: dt.date, rows: int = 60, mailto: str = "") -> List[Dict]:
    filters = ["from-index-date:" + since.isoformat()]
    if spec.get("filter_extra"):
        filters.append(spec["filter_extra"])
    url = (
        "https://api.crossref.org/works?query="
        + quote_plus(spec["query"])
        + "&filter=" + ",".join(filters)
        + f"&sort=created&order=desc&rows={rows}"
        + "&select=DOI,title,abstract,URL,container-title,created,type,author"
    )
    if mailto:
        url += "&mailto=" + quote_plus(mailto)
    try:
        resp = get(url, headers={"Accept": "application/json"})
        resp.raise_for_status()
        payload = resp.json()["message"]["items"]
    except Exception as exc:
        print(f"  ! Crossref '{spec['query'][:30]}': {type(exc).__name__}: {exc}")
        return []

    items = []
    for work in payload:
        title_list = work.get("title") or []
        if not title_list:
            continue
        container = (work.get("container-title") or ["Crossref"])[0]
        is_preprint = work.get("type") == "posted-content"
        parts = work.get("created", {}).get("date-parts", [[None]])[0]
        date = dt.date(*parts[:3]) if parts and parts[0] and len(parts) >= 3 else None
        authors = [
            (a.get("family") or "") for a in (work.get("author") or [])[:4] if a.get("family")
        ]
        items.append(
            make_item(
                title_list[0],
                work.get("URL", "https://doi.org/" + work.get("DOI", "")),
                work.get("abstract", ""),
                date,
                container or "Crossref",
                "preprints" if is_preprint else "journals",
                2 if is_preprint else 1,
                work.get("DOI"),
                ", ".join(authors) + (" et al." if len(authors) == 4 else ""),
            )
        )
    print(f"  - Crossref '{spec['query'][:34]}': {len(items)} entries")
    time.sleep(2)  # stay inside Crossref's polite request rate
    return items


# ---------------------------------------------------------------------------
# OpenAlex
# ---------------------------------------------------------------------------

def fetch_openalex(query: str, since: dt.date, mailto: str = "", per_page: int = 50) -> List[Dict]:
    url = (
        "https://api.openalex.org/works?filter=from_publication_date:"
        + since.isoformat()
        + ",title_and_abstract.search:" + quote_plus(query)
        + f"&sort=publication_date:desc&per-page={per_page}"
    )
    if mailto:
        url += "&mailto=" + quote_plus(mailto)
    try:
        resp = get(url, headers={"Accept": "application/json"})
        resp.raise_for_status()
        results = resp.json().get("results", [])
    except Exception as exc:
        print(f"  ! OpenAlex '{query[:30]}': {type(exc).__name__}: {exc}")
        return []

    items = []
    for work in results:
        title = work.get("title") or work.get("display_name") or ""
        if not title:
            continue
        venue = ((work.get("primary_location") or {}).get("source") or {}).get(
            "display_name"
        ) or "OpenAlex"
        abstract = ""
        inv = work.get("abstract_inverted_index")
        if inv:
            positions = {}
            for word, idxs in inv.items():
                for i in idxs:
                    positions[i] = word
            abstract = " ".join(positions[k] for k in sorted(positions))
        authors = [
            (a.get("author") or {}).get("display_name", "")
            for a in (work.get("authorships") or [])[:4]
        ]
        items.append(
            make_item(
                title,
                work.get("doi") or work.get("id", ""),
                abstract,
                parse_date(work.get("publication_date")),
                venue,
                "preprints" if work.get("type") == "preprint" else "journals",
                1,
                (work.get("doi") or "").replace("https://doi.org/", ""),
                ", ".join(a for a in authors if a),
            )
        )
    print(f"  - OpenAlex '{query[:34]}': {len(items)} entries")
    return items


# ---------------------------------------------------------------------------
# GitHub releases
# ---------------------------------------------------------------------------

def fetch_github_releases(repo: str, token: str = "") -> List[Dict]:
    headers = {"Accept": "application/vnd.github+json"}
    if token:
        headers["Authorization"] = "Bearer " + token
    try:
        resp = get(f"https://api.github.com/repos/{repo}/releases?per_page=5", headers=headers)
        if resp.status_code == 404:
            return []
        resp.raise_for_status()
        releases = resp.json()
    except Exception as exc:
        print(f"  ! GitHub {repo}: {type(exc).__name__}: {exc}")
        return []

    items = []
    for rel in releases:
        if rel.get("draft"):
            continue
        name = rel.get("name") or rel.get("tag_name") or "release"
        items.append(
            make_item(
                f"{repo} {name}",
                rel.get("html_url", ""),
                rel.get("body", ""),
                parse_date(rel.get("published_at")),
                f"GitHub: {repo}",
                "industry",
                3,
                None,
                "Code release",
            )
        )
    print(f"  - GitHub {repo}: {len(items)} releases")
    return items


def dedupe(items: Iterable[Dict]) -> List[Dict]:
    """Collapse the same paper arriving from arXiv, Crossref and OpenAlex."""
    best: Dict[str, Dict] = {}
    for item in items:
        key = item["doi"] or re.sub(r"[^a-z0-9]", "", item["title"].lower())[:90]
        if not key:
            continue
        current = best.get(key)
        if current is None or len(item["summary"]) > len(current["summary"]):
            if current is not None:
                item["bonus"] = max(item["bonus"], current["bonus"])
            best[key] = item
    return list(best.values())
