# AI + Materials Discovery — daily digest agent

Fetches new work on AI-driven materials discovery every day, scores it against
keyword rules, and prepends the survivors to [`DIGEST.md`](DIGEST.md).

No API keys and no LLM required. The only dependency is `requests`.

## What it watches

| Source | How | Covers |
|---|---|---|
| arXiv | official API, 4 topic queries | cond-mat.mtrl-sci, physics.chem-ph, cs.LG |
| Crossref | `from-index-date` queries + prefix `10.26434` | newly indexed DOIs across all publishers, plus ChemRxiv preprints |
| OpenAlex | `title_and_abstract.search` | cross-publisher backstop, catches ACS/RSC/Wiley |
| Journal RSS | 13 feeds | Nature, Nature Materials/Chemistry/Energy/Synthesis/Comput. Sci./Rev. Mater., npj Comput. Mater., Nature Comms., Science, Matter, Joule |
| Industry blogs | 4 feeds | NVIDIA Developer, NVIDIA, Microsoft Research, Google DeepMind |
| GitHub releases | REST API | mattergen, mattersim, skala, materials_discovery, nvalchemi-toolkit(+ops), mace, alabos, pymatgen |
| Conferences | regex on arXiv `comment` field | NeurIPS, ICLR, ICML, AAAI, CVPR, MRS, ACS, APS March Meeting |

**Deliberately not scraped:** ACS, RSC and the ChemRxiv REST API sit behind
Cloudflare and return HTTP 403 to any scripted client. Their content still shows
up, via the Crossref and OpenAlex DOI queries.

## Local use

```bash
pip install -r requirements.txt

python run_digest.py                  # normal run, writes DIGEST.md
python run_digest.py --dry-run        # print to screen, change nothing
python run_digest.py --days 14        # widen the lookback window
python run_digest.py --min-score 15   # only the strongest hits
python run_digest.py --days 30 --ignore-state --dry-run   # backfill preview
```

A run takes roughly 2–4 minutes; most of it is deliberate politeness delays
(3 s between arXiv calls, 2 s between Crossref calls).

## Daily automation with GitHub Actions

[`.github/workflows/daily-digest.yml`](.github/workflows/daily-digest.yml) runs
at 11:30 UTC daily and commits any new entries.

1. Create an empty GitHub repo, then from this folder:
   ```bash
   git init
   git add .
   git commit -m "AI + materials discovery daily digest agent"
   git branch -M main
   git remote add origin https://github.com/<you>/ai-materials-digest.git
   git push -u origin main
   ```
2. In the repo, go to **Settings > Actions > General > Workflow permissions**
   and select **Read and write permissions** so the bot can commit the digest.
3. Optionally add a repo secret `OPENALEX_MAILTO` with your email address; that
   puts OpenAlex requests in their faster "polite pool".
4. Trigger the first run by hand from **Actions > Daily AI + materials digest >
   Run workflow** (set a larger `days` value, e.g. `30`, to seed the file).

Scheduled workflows are paused after 60 days of repository inactivity — the
daily commits keep it alive on their own.

## Tuning what gets through

Everything lives in [`config.json`](config.json).

- `min_score` (default 6) — the relevance cutoff. Raise it if the digest is
  noisy; lower it if you are missing things.
- `lookback_days` (default 3) — overlap window, so a weekend outage or a slow
  Crossref index does not drop items.
- `core_terms` / `ai_terms` / `materials_terms` / `bonus_terms` — keyword
  weights. Title matches count double.
- `veto_terms` — instant rejection, which is what keeps GeForce and earnings
  posts out of the digest.

**The gate rule:** an item is only considered if it matches a *core* term, or an
*AI* term **and** a *materials* term. That single rule is what separates
"AI for materials" from generic AI news and generic materials news.

To add a journal, append to `JOURNAL_FEEDS` in
[`agent/sources.py`](agent/sources.py). Nature-family feeds follow the pattern
`https://www.nature.com/<journal-code>.rss`. Unreachable feeds are logged and
skipped, never fatal.

## Files

```
run_digest.py            entry point / CLI
config.json              keywords, weights, thresholds
agent/sources.py         all feed URLs and query strings
agent/fetch.py           HTTP + RSS/RDF/Atom/JSON parsing, cross-source dedupe
agent/score.py           keyword scoring and the gate rule
agent/state.py           seen-item store, 365-day retention
agent/render.py          markdown rendering, prepends to DIGEST.md
tools/md2docx.py         optional: convert any digest .md to .docx
state/seen.json          dedupe memory (committed, so CI remembers)
DIGEST.md                the running document
```

## Converting the digest to Word

```bash
pip install python-docx
python tools/md2docx.py DIGEST.md DIGEST.docx
```

## Known limits

- Keyword scoring has no idea what a paper *means*. It ranks by vocabulary, so a
  well-written review will sometimes outrank a genuine breakthrough. Skim titles.
- Journal RSS feeds carry a title and often no abstract, so those items score
  lower than preprints purely for lack of text. That is why `min_score` is not
  set high by default.
- Conference coverage relies on authors declaring acceptance in the arXiv
  comment field. Camera-ready proceedings (NeurIPS, MRS abstracts) are not
  indexed anywhere machine-readable and free; treat this as best-effort.
- Crossref indexing lags publication by days for some publishers; the 3-day
  lookback plus the dedupe store handles that without duplicating entries.
