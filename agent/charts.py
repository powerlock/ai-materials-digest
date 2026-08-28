"""Figures for the summary document.

Clustering is a small deterministic k-means implemented on numpy rather than a
sklearn dependency: the feature space is four columns wide, so there is nothing
to gain from a heavier library.
"""

from __future__ import annotations

import collections
import datetime as dt
import os
from typing import Dict, List, Tuple

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

plt.rcParams.update({
    "figure.dpi": 130,
    "font.family": "serif",
    "font.serif": ["Times New Roman", "DejaVu Serif"],
    "font.size": 9,
    "axes.titlesize": 10,
    "axes.labelsize": 9,
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "axes.grid": True,
    "grid.alpha": 0.3,
    "axes.spines.top": False,
    "axes.spines.right": False,
})

TIER_COLORS = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"]


def kmeans(features: np.ndarray, k: int = 3, iters: int = 60) -> np.ndarray:
    """Deterministic k-means: quantile initialisation, no random seed needed."""
    if len(features) <= k:
        return np.arange(len(features))
    scaled = (features - features.mean(axis=0)) / (features.std(axis=0) + 1e-9)
    order = np.argsort(scaled[:, 0])
    centroids = np.array(
        [scaled[order[int((i + 0.5) * len(order) / k)]] for i in range(k)]
    )
    labels = np.zeros(len(scaled), dtype=int)
    for _ in range(iters):
        distances = ((scaled[:, None, :] - centroids[None, :, :]) ** 2).sum(axis=2)
        new = distances.argmin(axis=1)
        if (new == labels).all():
            break
        labels = new
        for j in range(k):
            if (labels == j).any():
                centroids[j] = scaled[labels == j].mean(axis=0)
    return labels


def _annotate_sparse(ax, points, min_dist: float = 0.06, max_labels: int = 12):
    """Label points, skipping any that would collide with an existing label.

    Without this, the dozen models that share an 18 meV/atom MAE overprint into
    an illegible smear.
    """
    placed = []
    x0, x1 = ax.get_xlim()
    y0, y1 = ax.get_ylim()
    logx = ax.get_xscale() == "log"
    logy = ax.get_yscale() == "log"

    def norm(x, y):
        if logx:
            fx = (np.log10(max(x, 1e-9)) - np.log10(max(x0, 1e-9))) / (
                np.log10(max(x1, 1e-9)) - np.log10(max(x0, 1e-9)) + 1e-9)
        else:
            fx = (x - x0) / (x1 - x0 + 1e-9)
        if logy:
            fy = (np.log10(max(y, 1e-9)) - np.log10(max(y0, 1e-9))) / (
                np.log10(max(y1, 1e-9)) - np.log10(max(y0, 1e-9)) + 1e-9)
        else:
            fy = (y - y0) / (y1 - y0 + 1e-9)
        return fx, fy

    for x, y, label in points:
        if len(placed) >= max_labels:
            break
        fx, fy = norm(x, y)
        if any((fx - px) ** 2 + (fy - py) ** 2 < min_dist ** 2 for px, py in placed):
            continue
        placed.append((fx, fy))
        ax.annotate(label, (x, y), fontsize=6.5, xytext=(5, 4),
                    textcoords="offset points",
                    bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none", alpha=0.7))


def _save(fig, path: str) -> str:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    fig.tight_layout()
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)
    print(f"  chart: {path}")
    return path


def cluster_scatter(models: List[Dict], path: str) -> Tuple[str, Dict[str, int]]:
    """MAE vs accuracy, k-means clustered into performance tiers."""
    rows = [
        m for m in models
        if m.get("mae_mev_atom") is not None and m.get("accuracy_pct") is not None
        and m.get("f1") is not None and m.get("r2") is not None
    ]
    if len(rows) < 4:
        return "", {}

    features = np.array([
        [m["mae_mev_atom"], m["accuracy_pct"], m["f1"], m["r2"]] for m in rows
    ], dtype=float)
    labels = kmeans(features, k=3)

    # Order clusters best-to-worst by mean MAE so tier numbers are meaningful.
    means = {j: features[labels == j, 0].mean() for j in set(labels)}
    rank = {j: r for r, (j, _) in enumerate(sorted(means.items(), key=lambda kv: kv[1]))}
    tiers = {m["model"]: rank[int(l)] + 1 for m, l in zip(rows, labels)}

    fig, ax = plt.subplots(figsize=(8.4, 5.4))
    for j in sorted(set(labels), key=lambda j: rank[j]):
        mask = labels == j
        tier = rank[j] + 1
        ax.scatter(
            features[mask, 0], features[mask, 1],
            s=46, alpha=0.85, color=TIER_COLORS[tier - 1],
            label=f"Tier {tier}  (mean MAE {means[j]:.0f} meV/atom, n={mask.sum()})",
            edgecolor="white", linewidth=0.6,
        )

    ax.set_xscale("log")
    ax.set_xlabel("Energy-above-hull MAE (meV/atom, log scale) - lower is better")
    ax.set_ylabel("Stability classification accuracy (%)")
    ax.set_title("Model performance clusters: accuracy vs error\n"
                 "Matbench Discovery, WBM unique-prototype split")
    ax.legend(loc="lower left", fontsize=7.5, framealpha=0.9)

    ranked = sorted(rows, key=lambda m: m["mae_mev_atom"])
    _annotate_sparse(
        ax,
        [(m["mae_mev_atom"], m["accuracy_pct"], m["model"])
         for m in ranked + ranked[::-1][:4]],
        min_dist=0.075, max_labels=11,
    )
    return _save(fig, path), tiers


def progress_trend(models: List[Dict], path: str) -> str:
    """MAE against paper date, with a best-so-far frontier."""
    rows = [
        m for m in models
        if m.get("mae_mev_atom") is not None and len(m.get("date") or "") >= 7
    ]
    if len(rows) < 4:
        return ""

    def to_date(value: str):
        for fmt in ("%Y-%m-%d", "%Y-%m"):
            try:
                return dt.datetime.strptime(value[:len(fmt) + 2], fmt)
            except ValueError:
                continue
        return None

    points = [(to_date(m["date"]), m["mae_mev_atom"], m["model"]) for m in rows]
    points = sorted([p for p in points if p[0]], key=lambda p: p[0])
    if len(points) < 4:
        return ""

    dates = [p[0] for p in points]
    maes = [p[1] for p in points]

    fig, ax = plt.subplots(figsize=(8.4, 5.0))
    ax.scatter(dates, maes, s=34, color="#1f77b4", alpha=0.75,
               edgecolor="white", linewidth=0.5, label="Model (paper date)")

    frontier_x, frontier_y, record_setters = [], [], []
    best = float("inf")
    for date, mae, name in points:
        if mae < best:
            record_setters.append((date, mae, name))
        best = min(best, mae)
        frontier_x.append(date)
        frontier_y.append(best)
    ax.step(frontier_x, frontier_y, where="post", color="#d62728", linewidth=1.8,
            label="Best MAE achieved so far")

    ax.set_yscale("log")
    ax.set_ylabel("Energy-above-hull MAE (meV/atom, log)")
    ax.set_xlabel("Paper / benchmark date")
    ax.set_title("Trend: how fast the error frontier is falling\n"
                 "labelled points are the models that set a new record")
    ax.legend(fontsize=7.5)
    # Only record-setters get labels; everything else is visual noise.
    _annotate_sparse(ax, [(matplotlib.dates.date2num(d), m, n)
                          for d, m, n in record_setters],
                     min_dist=0.07, max_labels=9)
    fig.autofmt_xdate()
    return _save(fig, path)


def architecture_summary(models: List[Dict], path: str) -> str:
    """Which architecture families exist, and how they perform on average."""
    groups: Dict[str, List[float]] = collections.defaultdict(list)
    for m in models:
        arch = (m.get("architecture") or "unspecified").split(",")[0].strip() or "unspecified"
        if m.get("mae_mev_atom") is not None:
            groups[arch].append(m["mae_mev_atom"])
    groups = {k: v for k, v in groups.items() if v}
    if not groups:
        return ""

    order = sorted(groups, key=lambda k: np.mean(groups[k]))
    means = [float(np.mean(groups[k])) for k in order]
    counts = [len(groups[k]) for k in order]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.6, 4.2))
    ax1.barh(order, means, color="#4c72b0")
    ax1.set_xlabel("Mean MAE (meV/atom)")
    ax1.set_title("Average error by architecture family")
    ax1.invert_yaxis()
    for i, (mean, count) in enumerate(zip(means, counts)):
        ax1.text(mean, i, f" {mean:.0f}", va="center", fontsize=7)

    ax2.barh(order, counts, color="#dd8452")
    ax2.set_xlabel("Number of models benchmarked")
    ax2.set_title("Model count by architecture family")
    ax2.invert_yaxis()
    for i, count in enumerate(counts):
        ax2.text(count, i, f" {count}", va="center", fontsize=7)
    return _save(fig, path)


def energy_vs_thermal(models: List[Dict], path: str) -> str:
    """Does a low energy error imply good thermal-conductivity prediction?"""
    rows = [
        m for m in models
        if m.get("mae_mev_atom") is not None and m.get("kappa_srme") is not None
    ]
    if len(rows) < 5:
        return ""

    x = np.array([m["mae_mev_atom"] for m in rows], dtype=float)
    y = np.array([m["kappa_srme"] for m in rows], dtype=float)

    fig, ax = plt.subplots(figsize=(7.6, 5.0))
    ax.scatter(x, y, s=40, color="#55a868", alpha=0.85, edgecolor="white", linewidth=0.5)

    r = float(np.corrcoef(np.log10(x), y)[0, 1]) if x.std() > 0 else 0.0
    strength = ("no", "a weak", "a moderate", "a strong")[
        min(3, int(abs(r) / 0.25))
    ]
    ax.text(0.03, 0.96, f"Pearson r (log MAE vs kSRME) = {r:.2f}",
            transform=ax.transAxes, fontsize=8, va="top",
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="0.8"))

    ax.set_xscale("log")
    ax.set_xlabel("Energy-above-hull MAE (meV/atom, log)")
    ax.set_ylabel("Phonon kappa_SRME (lower is better)")
    ax.set_title("Energy accuracy vs thermal-transport accuracy\n"
                 f"{strength} relationship: a good energy model is "
                 f"{'usually' if abs(r) >= 0.5 else 'not necessarily'} "
                 "a good phonon model")

    best = sorted(rows, key=lambda m: m["kappa_srme"])
    _annotate_sparse(
        ax,
        [(m["mae_mev_atom"], m["kappa_srme"], m["model"])
         for m in best + sorted(rows, key=lambda m: -m["kappa_srme"])[:3]],
        min_dist=0.08, max_labels=9,
    )
    return _save(fig, path)


def literature_trend(studies: List[Dict], path: str, top_n: int = 8) -> str:
    """Which models the new literature is actually talking about, over time."""
    counts: Dict[str, collections.Counter] = collections.defaultdict(collections.Counter)
    totals: collections.Counter = collections.Counter()
    for study in studies:
        month = (study.get("date") or "")[:7]
        if not month:
            continue
        for model in study.get("models", []):
            counts[month][model] += 1
            totals[model] += 1
    if not totals:
        return ""

    months = sorted(counts)
    top = [m for m, _ in totals.most_common(top_n)]
    if not top:
        return ""

    # With a single month there is no trend to draw; a ranked bar is honest.
    if len(months) < 2:
        fig, ax = plt.subplots(figsize=(7.6, 4.4))
        names = [m for m, _ in totals.most_common(12)][::-1]
        values = [totals[m] for m in names]
        ax.barh(names, values, color="#4c72b0")
        for i, v in enumerate(values):
            ax.text(v, i, f" {v}", va="center", fontsize=7)
        ax.set_xlabel("Studies mentioning the model")
        ax.set_title(f"Models named in the digested literature ({months[0]})\n"
                     "single month of data so far - trend view appears once "
                     "the digest spans 2+ months")
        return _save(fig, path)

    fig, ax = plt.subplots(figsize=(8.6, 4.6))
    bottom = np.zeros(len(months))
    cmap = plt.get_cmap("tab10")
    for i, model in enumerate(top):
        values = np.array([counts[m][model] for m in months], dtype=float)
        ax.bar(months, values, bottom=bottom, label=model, color=cmap(i % 10))
        bottom += values

    ax.set_ylabel("Mentions in digested studies")
    ax.set_xlabel("Month")
    ax.set_title("Which models the incoming literature is using")
    ax.legend(fontsize=7, ncol=2)
    if len(months) > 6:
        fig.autofmt_xdate()
    return _save(fig, path)


def build_all(models: List[Dict], studies: List[Dict], charts_dir: str):
    """Returns (list of chart paths, model -> tier mapping)."""
    paths = []
    scatter, tiers = cluster_scatter(models, os.path.join(charts_dir, "model_clusters.png"))
    if scatter:
        paths.append((scatter, "Performance clusters: accuracy vs error"))
    for func, name, caption in [
        (progress_trend, "error_trend.png", "Trend: error frontier over time"),
        (architecture_summary, "architectures.png", "Architecture families and their mean error"),
        (energy_vs_thermal, "energy_vs_thermal.png", "Energy accuracy vs thermal transport accuracy"),
    ]:
        path = func(models, os.path.join(charts_dir, name))
        if path:
            paths.append((path, caption))
    lit = literature_trend(studies, os.path.join(charts_dir, "literature_trend.png"))
    if lit:
        paths.append((lit, "Model mentions in the incoming literature"))
    return paths, tiers
