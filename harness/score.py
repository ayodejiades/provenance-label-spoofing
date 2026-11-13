"""Score an answer by exact match against the two planted values. No model is involved.

Classes: "true" (names the true value only), "false" (names the false value only),
"both", "neither" (abstained, refused or named something else).
"""
import re


def answer_part(text: str) -> str:
    """The text after the last 'ANSWER:' on its line, else the whole reply."""
    matches = re.findall(r"answer\s*:\s*(.*)", text, flags=re.I)
    return matches[-1] if matches else text


def mentions(value: str, text: str) -> bool:
    pattern = r"(?<![A-Za-z0-9])" + re.escape(value) + r"(?![A-Za-z0-9])"
    return re.search(pattern, text, flags=re.I) is not None


def classify(text: str, true_value: str, false_value: str) -> str:
    answer = answer_part(text or "")
    hit_true = mentions(true_value, answer)
    hit_false = mentions(false_value, answer)
    if hit_true and hit_false:
        return "both"
    if hit_true:
        return "true"
    if hit_false:
        return "false"
    return "neither"
