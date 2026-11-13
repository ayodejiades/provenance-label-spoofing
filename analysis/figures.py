"""Figures from the run results. Re-runs itself under `uv run --with matplotlib` when
matplotlib is not installed. Writes figures/fig1.png and figures/fig2.png.

fig1: false-follow rate per condition and model, held-out seeds, Wilson 95% intervals.
fig2: what each model answered (true / false / both / neither) in the same conditions.

No captions are written: the captions are part of the paper and are written by the author.
`make analyze` skips this file; run it with `python3 analysis/figures.py`.
"""
import json
import os
import pathlib
import shutil
import subprocess
import sys

try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
except ImportError:
    if os.environ.get("FIGURES_REEXEC") or not shutil.which("uv"):
        print("figures: SKIP (matplotlib not available and uv not found)")
        sys.exit(0)
    env = dict(os.environ, FIGURES_REEXEC="1")
    sys.exit(subprocess.call(["uv", "run", "-q", "--with", "matplotlib", "python", __file__], env=env))

PROJECT = pathlib.Path(__file__).resolve().parents[1]
cfg = json.loads((PROJECT / "configs" / "experiment.json").read_text())
SPLIT = os.environ.get("FIG_SPLIT", "heldout")
SEEDS = set(cfg["split"][SPLIT if SPLIT in cfg["split"] else "heldout"])
FIG = PROJECT / "figures"

SHOWN = [("C1", "no labels"), ("C2", "honest\nlabels"), ("C5", "forged label\n(metadata)"),
         ("C12", "none\nverified"), ("C13", "typed label"), ("C14", "typed label\n+ fix"),
         ("C15", "typed prose"), ("C16", "typed prose\n+ fix")]
CLASSES = [("true", "#4c956c"), ("false", "#c1121f"), ("both", "#e9c46a"), ("neither", "#adb5bd")]
MODEL_COLOURS = ["#264653", "#2a9d8f", "#e76f51", "#8d5a97", "#577590", "#bc6c25"]


def wilson(k, n, z=1.96):
    if n == 0:
        return 0.0, 0.0, 0.0
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * ((p * (1 - p) / n + z * z / (4 * n * n)) ** 0.5) / d
    return p, max(0.0, c - h), min(1.0, c + h)


counts = {}   # (model, condition) -> {class: n}
paths = sorted(PROJECT.glob("runs/C*-s*/result.json")) + sorted(PROJECT.glob("kaggle-arm/*/runs/C*-s*/result.json"))
for path in paths:
    result = json.loads(path.read_text())
    if result["seed"] not in SEEDS:
        continue
    for row in result["items"]:
        if row["class"] == "error":
            continue
        bucket = counts.setdefault((row["model"], result["condition"]), {})
        bucket[row["class"]] = bucket.get(row["class"], 0) + 1

models = sorted({model for model, _ in counts})
if not models:
    print("figures: no %s runs yet" % SPLIT)
    sys.exit(0)
FIG.mkdir(exist_ok=True)
plt.rcParams.update({"font.size": 9, "axes.spines.top": False, "axes.spines.right": False,
                     "savefig.dpi": 200, "savefig.bbox": "tight"})

# fig1: grouped bars of the false-follow rate
fig, ax = plt.subplots(figsize=(9.5, 3.6))
width = 0.8 / len(models)
for m, model in enumerate(models):
    xs, ps, los, his = [], [], [], []
    for c, (cond, _) in enumerate(SHOWN):
        bucket = counts.get((model, cond))
        if not bucket:
            continue
        p, lo, hi = wilson(bucket.get("false", 0), sum(bucket.values()))
        xs.append(c - 0.4 + width * (m + 0.5))
        ps.append(p)
        los.append(p - lo)
        his.append(hi - p)
    ax.bar(xs, ps, width=width * 0.92, color=MODEL_COLOURS[m % len(MODEL_COLOURS)], label=model,
           yerr=[los, his], error_kw={"elinewidth": 0.8, "capsize": 1.5, "ecolor": "#333333"})
ax.set_xticks(range(len(SHOWN)))
ax.set_xticklabels(["%s\n%s" % (cond, label) for cond, label in SHOWN])
ax.set_ylim(0, 1.02)
ax.set_ylabel("share of answers following the false source")
ax.legend(frameon=False, ncol=min(len(models), 5), loc="upper center", bbox_to_anchor=(0.5, 1.16))
fig.savefig(FIG / "fig1.png")
plt.close(fig)

# fig2: answer composition, one panel per model
fig, axes = plt.subplots(1, len(models), figsize=(2.6 * len(models) + 0.8, 3.2), sharey=True, squeeze=False)
for m, model in enumerate(models):
    ax = axes[0][m]
    bottoms = [0.0] * len(SHOWN)
    for name, colour in CLASSES:
        heights = []
        for cond, _ in SHOWN:
            bucket = counts.get((model, cond), {})
            total = sum(bucket.values())
            heights.append(bucket.get(name, 0) / total if total else 0.0)
        ax.bar(range(len(SHOWN)), heights, bottom=bottoms, color=colour, width=0.8,
               label=name if m == 0 else None)
        bottoms = [b + h for b, h in zip(bottoms, heights)]
    ax.set_title(model, fontsize=9)
    ax.set_xticks(range(len(SHOWN)))
    ax.set_xticklabels([cond for cond, _ in SHOWN], rotation=90)
    ax.set_ylim(0, 1)
axes[0][0].set_ylabel("share of answers")
fig.legend(frameon=False, ncol=4, loc="upper center", bbox_to_anchor=(0.5, 1.08))
fig.savefig(FIG / "fig2.png")
plt.close(fig)
print("wrote figures/fig1.png and figures/fig2.png (%s seeds, %d models)" % (SPLIT, len(models)))
