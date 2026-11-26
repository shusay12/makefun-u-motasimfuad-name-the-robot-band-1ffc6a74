#!/usr/bin/env python3
"""Name the Robot Band — make.fun entry.

Writes one funny robot band name plus a few words on its hit song to
/output/entry.txt. Deterministic: the same line every run, standard
library only, no network, no randomness.
"""

from hashlib import sha256
from pathlib import Path

ENTRY = (
    "Ctrl Alt Delete \u2014 their hit 'Task Failed Successfully' "
    "went platinum before the band blue-screened mid-tour."
)

OUTPUT_PATH = Path("/output/entry.txt")

MAX_CHARS = 200


def check_entry(text: str) -> None:
    """Enforce the competition gate: 1-200 chars, single line, not blank."""
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, must be 1-{MAX_CHARS}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be whitespace-only")


def main() -> None:
    check_entry(ENTRY)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8", newline="")
    # Read the file back and prove the bytes on disk are exactly the entry.
    written = OUTPUT_PATH.read_bytes()
    if written != ENTRY.encode("utf-8"):
        raise ValueError("round-trip check failed: file bytes differ from entry")
    digest = sha256(written).hexdigest()
    print(f"wrote {len(ENTRY)} chars to {OUTPUT_PATH} (sha256 {digest})")


if __name__ == "__main__":
    main()
