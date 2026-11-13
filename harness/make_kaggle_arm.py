"""Stage the Kaggle arm: one self-contained project per model under kaggle-arm/.

Each staged project is a copy of harness/, analysis/, QUESTION.md, PREREG.md and the freeze
record, with configs/experiment.json changed in one way only: `models` is the single Kaggle
model. Conditions, seeds, items, prompts and scoring are the same files as the local arm.

    python3 harness/make_kaggle_arm.py            # stage
    rops-kaggle pack kaggle-arm/<name> --user <kaggle-username>
    rops-kaggle push kaggle-arm/<name>
    rops-kaggle pull kaggle-arm/<name>            # results land in kaggle-arm/<name>/runs

analysis/01_rates.py reads runs/ and kaggle-arm/*/runs/ together.
"""
import json
import pathlib
import re
import shutil

PROJECT = pathlib.Path(__file__).resolve().parents[1]
cfg = json.loads((PROJECT / "configs" / "experiment.json").read_text())

for model in cfg["kaggle_arm"]["models"]:
    name = "epi-" + re.sub(r"[^a-z0-9]+", "-", model.lower()).strip("-")
    stage = PROJECT / "kaggle-arm" / name
    for folder in ("harness", "analysis"):
        if (stage / folder).exists():
            shutil.rmtree(stage / folder)          # only the copied code is replaced; runs/ is kept
        shutil.copytree(PROJECT / folder, stage / folder, ignore=shutil.ignore_patterns("__pycache__"))
    for file in ("QUESTION.md", "PREREG.md", ".rops/limits.json", ".rops/prereg.json"):
        if (PROJECT / file).exists():
            (stage / file).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(PROJECT / file, stage / file)
    staged = dict(cfg)
    staged["models"] = [model]
    staged["calls_per_run"] = cfg["items_per_run"]
    staged.pop("kaggle_arm", None)
    (stage / "configs").mkdir(exist_ok=True)
    (stage / "configs" / "experiment.json").write_text(json.dumps(staged, indent=2) + "\n")
    for folder in ("runs", "results"):
        (stage / folder).mkdir(exist_ok=True)
    print("staged %s (%s)" % (stage.relative_to(PROJECT), model))
