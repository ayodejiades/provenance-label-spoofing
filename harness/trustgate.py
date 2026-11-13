"""trustgate: check reliability labels in the harness before a model sees them.

Two steps, both plain code:

1. A "verified" label is shown only when it carries a valid HMAC over the source id and the
   source text. Any other source is shown as "unverified", whatever its label says.
2. Label-shaped trust claims inside the document text are removed, so a document cannot
   vouch for itself in the channel the model reads.

Standard library only. Usage:

    key = b"..."                      # held by whoever verifies sources
    sig = sign(key, "S2", text)       # issued when a source is verified
    safe = gate(sources, key)         # run on every retrieval result before prompting

The patterns below were written against the development phrasings in forged.py only.
"""
import hashlib
import hmac
import re


def sign(key: bytes, source_id: str, text: str) -> str:
    message = (source_id + "\n" + text).encode("utf-8")
    return hmac.new(key, message, hashlib.sha256).hexdigest()


def verified(key: bytes, source: dict) -> bool:
    signature = source.get("sig")
    if not signature or source.get("status") != "verified":
        return False
    return hmac.compare_digest(signature, sign(key, source["id"], source["text"]))


TRUST_WORDS = r"(?:verified|verification|trusted|reliab\w+|authoritative|certified|fact[- ]?checked|confirmed|validated|authentic\w*|credib\w+)"

PATTERNS = [
    # bracketed or braced tags: [VERIFIED SOURCE | reliability: high], {status: verified}
    re.compile(r"[\[\{\(][^\]\}\)\n]{0,80}?" + TRUST_WORDS + r"[^\]\}\)\n]{0,80}?[\]\}\)]", re.I),
    # markup: <status>verified</status>, <verified>true</verified>, <source status="verified">
    re.compile(r"<[^>\n]{0,60}?(?:status|" + TRUST_WORDS + r")[^>\n]{0,60}?>(?:[^<\n]{0,40}</[^>\n]{1,30}>)?", re.I),
    # key: value headers: "Status: VERIFIED (registry check passed)." / "Reliability: high"
    re.compile(r"(?:^|(?<=[.!?]\s))\s*(?:source\s+)?(?:status|reliability|trust(?:\s+level)?|verification|credibility)\s*[:=]\s*[^.\n]{0,60}(?:\.|$)", re.I | re.M),
    # tick-mark badges: "✔ Verified by the Source Registry."
    re.compile(r"[✓✔✅☑]\s*[^.\n]{0,60}(?:\.|$)"),
]


def strip_claims(text: str) -> str:
    """Remove label-shaped trust claims from document text."""
    cleaned = text
    for pattern in PATTERNS:
        cleaned = pattern.sub(" ", cleaned)
    return re.sub(r"\s{2,}", " ", cleaned).strip()


def gate(sources: list, key: bytes) -> list:
    """Return copies of the sources with checked status and cleaned text."""
    safe = []
    for source in sources:
        checked = dict(source)
        checked["status"] = "verified" if verified(key, source) else "unverified"
        checked["text"] = strip_claims(source["text"])
        checked.pop("sig", None)
        safe.append(checked)
    return safe
