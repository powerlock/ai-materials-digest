# Contributing

This project is a daily literature + benchmark monitor for AI-driven materials
discovery. Contributions are welcome, especially manual data curation.

## Quick setup

```bash
git clone <repo>
cd ai-materials-digest
pip install -r requirements.txt
```

## Kinds of contributions

### 1. Data

Most journal abstracts do not contain a numeric performance metric. If you open
a paper and find a missing value, add it to `manual_data.json` and rerun
`python build_summary.py`.

```jsonc
{
  "studies": {
    "<doi>": {
      "models": ["MACE-MP-0"],
      "materials": ["Li3YCl6"],
      "methods": ["DFT", "MD"],
      "metrics": [["MAE", 0.025, "eV/atom"]],
      "sort_value": 97.5
    }
  }
}
```

Rules:

- Use the exact DOI as the key.
- Keep units explicit and do not invent missing values.
- `sort_value` is optional; it overrides the auto-derived sort value.

### 2. New sources and keywords

- Feeds / APIs: add to `agent/sources.py` and handle failures gracefully.
- Keyword tuning: edit `config.json`.
- New models: if a model is not in the Matbench cache, add a manual entry under
  `models` in `manual_data.json`.

### 3. Code

- Keep the dependency list minimal.
- Do not bypass Cloudflare or scrape paywalled full text.
- Preserve UTF-8 safety for Windows consoles.
- Update `README.md` if the CLI or workflow changes.

## Before submitting

1. Run `python run_digest.py --dry-run` and `python build_summary.py` locally.
2. Check that `MODEL_PERFORMANCE.md`, `NEEDS_DATA.md`, and `charts/` look right.
3. Commit generated artifacts only if they are the deliverable; avoid
   committing one-off debug files.
