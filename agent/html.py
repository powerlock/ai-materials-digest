"""HTML dashboard for the model-performance summary."""

from __future__ import annotations

import datetime as dt
import html as html_module
import os
from typing import Dict, List, Tuple

from agent.summary import MODEL_FIELDS, _doi_cell, _fmt, _params, sort_models, sort_studies

NL = "\n"


def _b(text) -> str:
    return html_module.escape(str(text) if text is not None else "")


def _a(url: str, text: str) -> str:
    if not url:
        return _b(text)
    return (
        f'<a href="{url}" target="_blank" rel="noopener">{_b(text or "link")}</a>'
    )


def _doi_link_html(record: Dict) -> str:
    doi = record.get("doi") or ""
    if doi:
        return _a(f"https://doi.org/{doi}", doi)
    url = record.get("paper") or record.get("url") or record.get("repo") or ""
    return _a(url, "link") if url else ""


def _repo_link(record: Dict) -> str:
    repo = record.get("repo") or ""
    return _a(repo, "repo") if repo else ""


def _metric_html(metrics):
    if not metrics:
        return ""
    return "; ".join(
        f"{label} {_fmt(value)}{(' ' + unit) if unit else ''}"
        for label, value, unit in metrics
    )


def render_index(models: List[Dict], studies: List[Dict], chart_list,
                 tiers: Dict[str, int], generated: dt.date) -> str:
    models = sort_models(models)
    studies = sort_studies(studies)
    with_metrics = [m for m in models if m.get("accuracy_pct") is not None]

    # Headline numbers
    if with_metrics:
        best = with_metrics[0]
        lowest = min(with_metrics, key=lambda m: m["mae_mev_atom"] or 1e9)
        headline = (
            f"<strong>{len(models)}</strong> models tracked, "
            f"<strong>{len(with_metrics)}</strong> with comparable accuracy figures. "
            f"Highest stability-classification accuracy: "
            f"<strong>{_b(best['model'])}</strong> at "
            f"<strong>{_fmt(best.get('accuracy_pct'), 2)}%</strong> "
            f"(F1 {_fmt(best.get('f1'))}). "
            f"Lowest energy error: <strong>{_b(lowest['model'])}</strong> at "
            f"<strong>{_fmt(lowest.get('mae_mev_atom'), 1)} meV/atom</strong>. "
            f"<strong>{len(studies)}</strong> studies parsed from the digest; "
            f"<strong>{sum(1 for s in studies if s.get('sort_value') is not None)}</strong> "
            "reported a numeric performance figure in the abstract."
        )
    else:
        headline = (
            f"<strong>{len(models)}</strong> models and "
            f"<strong>{len(studies)}</strong> studies tracked."
        )

    # Figures
    figures = []
    for path, caption in chart_list:
        rel = os.path.relpath(path).replace("\\", "/")
        figures.append(
            f'<figure>\n'
            f'  <img src="{rel}" alt="{_b(caption)}">\n'
            f'  <figcaption>{_b(caption)}</figcaption>\n'
            f'</figure>'
        )

    # Benchmark table rows
    bench_rows = []
    for i, m in enumerate(models, 1):
        tier = tiers.get(m["model"])
        bench_rows.append(
            f"<tr>\n"
            f"  <td>{i}</td>\n"
            f"  <td><strong>{_b(m['model'])}</strong></td>\n"
            f"  <td>{_fmt(m.get('accuracy_pct'), 2)}</td>\n"
            f"  <td>{_fmt(m.get('mae_mev_atom'), 1)}</td>\n"
            f"  <td>{_fmt(m.get('rmse_mev_atom'), 1)}</td>\n"
            f"  <td>{_fmt(m.get('f1'))}</td>\n"
            f"  <td>{_fmt(m.get('r2'))}</td>\n"
            f"  <td>{_fmt(m.get('kappa_srme'))}</td>\n"
            f"  <td>{tier if tier is not None else ''}</td>\n"
            f"  <td>{_b(m.get('architecture'))}</td>\n"
            f"  <td>{_params(m.get('params'))}</td>\n"
            f"  <td>{_b(m.get('calc_method'))}</td>\n"
            f"  <td>{_b(m.get('materials_tested'))}</td>\n"
            f"  <td>{_b(m.get('training_sets'))}</td>\n"
            f"  <td>{_b(m.get('date'))}</td>\n"
            f"  <td>{_doi_link_html(m)}</td>\n"
            f"  <td>{_repo_link(m)}</td>\n"
            f"</tr>"
        )

    # Study table rows
    study_rows = []
    for i, s in enumerate(studies, 1):
        title = s["title"].replace("|", "/")[:150]
        metrics = _metric_html(s.get("metrics", []))
        study_rows.append(
            f"<tr>\n"
            f"  <td>{i}</td>\n"
            f"  <td>{_fmt(s.get('sort_value'), 1)}</td>\n"
            f"  <td>{_a(s.get('url'), title)}</td>\n"
            f"  <td>{_b(', '.join(s.get('models', [])[:5]))}</td>\n"
            f"  <td>{_b(', '.join(s.get('materials', [])[:5]))}</td>\n"
            f"  <td>{_b(', '.join(s.get('methods', [])[:5]))}</td>\n"
            f"  <td>{_b(metrics)}</td>\n"
            f"  <td>{_b(s.get('date'))}</td>\n"
            f"  <td>{_doi_link_html(s)}</td>\n"
            f"</tr>"
        )

    # Needs data: models with missing fields
    missing_model_rows = []
    for m in models:
        missing = [label for field, label in MODEL_FIELDS if not m.get(field)]
        if missing:
            missing_model_rows.append(
                f"<tr>\n"
                f"  <td><strong>{_b(m['model'])}</strong></td>\n"
                f"  <td>{_b(', '.join(missing))}</td>\n"
                f"  <td>{_doi_link_html(m)}</td>\n"
                f"  <td>{_repo_link(m)}</td>\n"
                f"</tr>"
            )

    # Studies with no numeric metric
    no_metric_rows = []
    for s in studies:
        if s.get("sort_value") is None:
            title = s["title"].replace("|", "/")[:150]
            no_metric_rows.append(
                f"<tr>\n"
                f"  <td>{_a(s.get('url'), title)}</td>\n"
                f"  <td>{_b(', '.join(s.get('models', [])))}</td>\n"
                f"  <td>{_b(', '.join(s.get('materials', [])[:5]))}</td>\n"
                f"  <td>{_b(', '.join(s.get('methods', [])[:5]))}</td>\n"
                f"  <td>{_b(s.get('date'))}</td>\n"
                f"  <td>{_doi_link_html(s)}</td>\n"
                f"</tr>"
            )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>AI Models for Materials Discovery — Performance Summary</title>
<style>
:root {{
  --bg: #ffffff;
  --text: #222222;
  --accent: #0b4f9e;
  --head: #111111;
  --row-alt: #f7f7f7;
  --border: #cccccc;
}}
* {{ box-sizing: border-box; }}
body {{
  font-family: Arial, Helvetica, sans-serif;
  line-height: 1.5;
  color: var(--text);
  background: var(--bg);
  max-width: 1300px;
  margin: 0 auto;
  padding: 1.5rem;
}}
h1, h2, h3 {{
  font-family: "Times New Roman", Times, serif;
  color: var(--head);
  margin-top: 1.8rem;
  margin-bottom: .5rem;
}}
h1 {{ border-bottom: 2px solid var(--accent); padding-bottom: .3rem; }}
a {{ color: var(--accent); text-decoration: none; }}
a:hover {{ text-decoration: underline; }}
.subtitle {{ color: #555; margin-top: 0; }}
.headline {{
  background: #eef4fb;
  border-left: 4px solid var(--accent);
  padding: .8rem 1rem;
  margin: 1rem 0;
}}
figure {{
  margin: 1rem 0;
  text-align: center;
}}
figure img {{ max-width: 100%; height: auto; border: 1px solid var(--border); }}
figcaption {{ font-style: italic; color: #555; margin-top: .4rem; }}
.table-wrap {{
  overflow-x: auto;
  margin: 1rem 0;
  border: 1px solid var(--border);
}}
input[type="text"] {{
  width: 100%;
  max-width: 320px;
  padding: .4rem .6rem;
  margin: .4rem 0;
  border: 1px solid var(--border);
  font-size: .95rem;
}}
table {{
  border-collapse: collapse;
  width: max-content;
  min-width: 100%;
  font-size: .9rem;
}}
th, td {{
  border: 1px solid var(--border);
  padding: .35rem .55rem;
  text-align: left;
  vertical-align: top;
}}
th {{
  background: #e8e8e8;
  cursor: pointer;
  user-select: none;
  white-space: nowrap;
}}
th:hover {{ background: #dcdcdc; }}
tr:nth-child(even) {{ background: var(--row-alt); }}
tr:hover {{ background: #eef4fb; }}
.caveat {{
  font-size: .95rem;
  color: #444;
  border-top: 1px solid var(--border);
  margin-top: 2rem;
  padding-top: 1rem;
}}
.footer {{
  margin-top: 2rem;
  font-size: .85rem;
  color: #666;
}}
</style>
</head>
<body>
<h1>AI Models for Materials Discovery — Performance Summary</h1>
<p class="subtitle">Generated {generated.isoformat()} by <code>build_summary.py</code>. Rows are ordered by reported accuracy (descending), then by error (ascending) — not chronologically. Blank cells mean the value was not published in a machine-readable form.</p>

<section>
<h2>How to read this summary</h2>
<ul>
  <li><strong>Table 1</strong> comes from the <a href="https://github.com/janosh/matbench-discovery">Matbench Discovery</a> leaderboard. Every model is evaluated on the same held-out test set with the same DFT reference, so these numbers are directly comparable.</li>
  <li><strong>Table 2</strong> comes from the daily literature digest. Each study uses its own test set and its own definition of error, so those numbers are <strong>not</strong> comparable to each other. Treat Table 2 as a lead list, not a ranking.</li>
</ul>
</section>

<div class="headline">{headline}</div>

<section>
<h2>Figures</h2>
{NL.join(figures)}
</section>

<section>
<h2>Table 1 — Benchmarked models, ranked by accuracy</h2>
<p><input type="text" oninput="filterTable('bench-table', this)" placeholder="Filter models / methods / materials..."></p>
<div class="table-wrap">
<table id="bench-table">
  <thead>
    <tr>
      <th onclick="sortTable(this)">#</th>
      <th onclick="sortTable(this)">Model</th>
      <th onclick="sortTable(this)">Acc. (%)</th>
      <th onclick="sortTable(this)">MAE (meV/atom)</th>
      <th onclick="sortTable(this)">RMSE (meV/atom)</th>
      <th onclick="sortTable(this)">F1</th>
      <th onclick="sortTable(this)">R²</th>
      <th onclick="sortTable(this)">kSRME</th>
      <th onclick="sortTable(this)">Tier</th>
      <th onclick="sortTable(this)">Arch.</th>
      <th onclick="sortTable(this)">Params</th>
      <th onclick="sortTable(this)">Calculation method</th>
      <th onclick="sortTable(this)">Materials</th>
      <th onclick="sortTable(this)">Training set</th>
      <th onclick="sortTable(this)">Date</th>
      <th onclick="sortTable(this)">DOI</th>
      <th onclick="sortTable(this)">Repo</th>
    </tr>
  </thead>
  <tbody>
{NL.join(bench_rows)}
  </tbody>
</table>
</div>
</section>

<section>
<h2>Table 2 — Studies from the daily digest</h2>
<p><input type="text" oninput="filterTable('study-table', this)" placeholder="Filter studies / models / materials..."></p>
<div class="table-wrap">
<table id="study-table">
  <thead>
    <tr>
      <th onclick="sortTable(this)">#</th>
      <th onclick="sortTable(this)">Sort value</th>
      <th onclick="sortTable(this)">Study</th>
      <th onclick="sortTable(this)">Models named</th>
      <th onclick="sortTable(this)">Materials / systems</th>
      <th onclick="sortTable(this)">Calculation method</th>
      <th onclick="sortTable(this)">Metrics found</th>
      <th onclick="sortTable(this)">Date</th>
      <th onclick="sortTable(this)">DOI</th>
    </tr>
  </thead>
  <tbody>
{NL.join(study_rows)}
  </tbody>
</table>
</div>
</section>

<section>
<h2>Needs data — awaiting further input</h2>
<p>These fields were blank in the automated sources. Add missing values to <code>manual_data.json</code> and rerun <code>build_summary.py</code>.</p>

<h3>Models with missing fields ({len(missing_model_rows)} of {len(models)})</h3>
<div class="table-wrap">
<table>
  <thead>
    <tr><th>Model</th><th>Missing fields</th><th>DOI</th><th>Repo</th></tr>
  </thead>
  <tbody>
{NL.join(missing_model_rows) if missing_model_rows else '<tr><td colspan="4"><em>none</em></td></tr>'}
  </tbody>
</table>
</div>

<h3>Studies with no numeric performance figure ({len(no_metric_rows)} of {len(studies)})</h3>
<div class="table-wrap">
<table>
  <thead>
    <tr><th>Study</th><th>Models named</th><th>Materials</th><th>Method</th><th>Date</th><th>DOI</th></tr>
  </thead>
  <tbody>
{NL.join(no_metric_rows) if no_metric_rows else '<tr><td colspan="6"><em>none</em></td></tr>'}
  </tbody>
</table>
</div>
</section>

<section class="caveat">
<h2>Provenance and honest limitations</h2>
<ul>
  <li><strong>Two sources.</strong> MAE/RMSE values are published in full-text tables, not abstracts. A table built solely from abstracts would be almost entirely blank, so the leaderboard supplies the comparable numbers and the digest supplies the leading edge.</li>
  <li><strong>Accuracy here means stability-classification accuracy</strong> (is this structure on or below the convex hull?), not a general chemical-accuracy claim.</li>
  <li><strong>Tiers</strong> come from k-means (k=3) on [MAE, accuracy, F1, R²], ordered by mean MAE. Tier 1 is best. They are a descriptive grouping, not a ranking endorsed by the benchmark authors.</li>
  <li><strong>Table 2 extraction is regex-based.</strong> It will miss models it has never heard of and can mis-attribute a number to the wrong quantity. Verify anything you intend to cite.</li>
  <li>Values you enter in <code>manual_data.json</code> override everything above and survive future runs.</li>
</ul>
</section>

<div class="footer">
  Download: <a href="data/model_performance.csv">CSV</a> ·
  <a href="MODEL_PERFORMANCE.md">Markdown</a> ·
  <a href="MODEL_PERFORMANCE.docx">Word</a> ·
  <a href="NEEDS_DATA.md">Needs data (MD)</a>
</div>

<script>
function sortTable(th) {{
  const table = th.closest('table');
  const tbody = table.querySelector('tbody');
  const rows = Array.from(tbody.querySelectorAll('tr'));
  const col = th.cellIndex;
  const current = th.dataset.sort || 'asc';
  const next = current === 'asc' ? 'desc' : 'asc';
  table.querySelectorAll('th').forEach(h => delete h.dataset.sort);
  th.dataset.sort = next;
  rows.sort((a, b) => {{
    const av = a.cells[col] ? a.cells[col].textContent.trim() : '';
    const bv = b.cells[col] ? b.cells[col].textContent.trim() : '';
    const an = parseFloat(av.replace(/,/g, ''));
    const bn = parseFloat(bv.replace(/,/g, ''));
    const bothNums = !isNaN(an) && !isNaN(bn) && av !== '' && bv !== '';
    if (bothNums) {{
      return next === 'asc' ? an - bn : bn - an;
    }}
    return next === 'asc' ? av.localeCompare(bv) : bv.localeCompare(av);
  }});
  rows.forEach(r => tbody.appendChild(r));
}}

function filterTable(id, input) {{
  const filter = input.value.toLowerCase();
  const table = document.getElementById(id);
  if (!table) return;
  table.querySelectorAll('tbody tr').forEach(tr => {{
    tr.style.display = tr.textContent.toLowerCase().includes(filter) ? '' : 'none';
  }});
}}
</script>
</body>
</html>
"""
