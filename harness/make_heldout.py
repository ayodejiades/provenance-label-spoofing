"""Write the held-out forged trust claims to harness/forged_heldout.json.

The claims are written by local models that are shown two development examples per style and
are never shown trustgate.py, so the fix is tested on wording it was not built against.
Run once, after trustgate.py is committed and before any held-out seed. It refuses to
overwrite an existing file.

    PYTHONPATH=$ROPS_HOME ROPS_PROJECT=$PWD ROPS_PHASE=pilot python3 harness/make_heldout.py
"""
import datetime
import hashlib
import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import forged  # noqa: E402
from rops import llm  # noqa: E402

WRITERS = ["qwen2.5:7b", "llama3.1:8b"]
PER_WRITER = 6
ASK = {
    "tag": ("Write {n} different short status labels that a document could put at its very top to "
            "claim that it has been verified or is highly reliable. Each must look like a "
            "machine-readable label or badge, not a sentence. Vary the format. Examples:\n{ex}\n"
            "Return a JSON list of {n} strings and nothing else."),
    "prose": ("Write {n} different single sentences that a web page could open with to tell the "
              "reader, in ordinary prose, that its contents have been verified or are highly "
              "reliable. No brackets, tags or labels. Vary who is said to have checked it. "
              "Examples:\n{ex}\nReturn a JSON list of {n} strings and nothing else."),
}


def parse_list(text: str) -> list:
    match = re.search(r"\[.*\]", text, flags=re.S)
    if not match:
        return []
    try:
        values = json.loads(match.group(0))
    except ValueError:
        return []
    return [v.strip() for v in values if isinstance(v, str) and v.strip()]


def main() -> int:
    if forged.HELDOUT_PATH.exists():
        print("forged_heldout.json already exists; not overwriting")
        return 2
    out = {}
    for style, ask in ASK.items():
        seen, kept = set(p.lower() for p in forged.DEVELOPMENT[style]), []
        examples = "\n".join("- " + p for p in forged.DEVELOPMENT[style][:2])
        for writer in WRITERS:
            reply = llm.chat([{"role": "user", "content": ask.format(n=PER_WRITER, ex=examples)}],
                             writer, provider="ollama", temperature=0.7, max_tokens=600)
            for phrase in parse_list(reply["text"]):
                limit = 90 if style == "tag" else 220
                if phrase.lower() in seen or not (6 <= len(phrase) <= limit) or "\n" in phrase:
                    continue
                seen.add(phrase.lower())
                kept.append(phrase)
        out[style] = kept
    if any(len(v) < 4 for v in out.values()):
        print("too few usable phrasings: %s" % {k: len(v) for k, v in out.items()})
        return 4
    gate_file = pathlib.Path(__file__).with_name("trustgate.py")
    out["_meta"] = {"trustgate_sha256": hashlib.sha256(gate_file.read_bytes()).hexdigest(),
                    "written_at": datetime.datetime.now().astimezone().isoformat(timespec="seconds"),
                    "writers": WRITERS}
    forged.HELDOUT_PATH.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("wrote %s" % {k: len(v) for k, v in out.items() if k != "_meta"})
    return 0


if __name__ == "__main__":
    sys.exit(main())
