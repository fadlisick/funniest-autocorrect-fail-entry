#!/usr/bin/env python3
"""Emit the Funniest Autocorrect Fail entry.

The bounty wants one line of text in entry.txt: a funny autocorrect
fail, nothing else. This script assembles that line from its parts and
drops it in the harness output directory.
"""

import os
from pathlib import Path

RECIPIENT = "my boss"
SLIP = "I'll be there in a sex"
INTENDED = "in a sec"
OUTPUT_FILE = "entry.txt"
MAX_CHARS = 199


def build_line() -> str:
    return f"I texted {RECIPIENT} '{SLIP}' — I meant '{INTENDED}'."


def output_path() -> Path:
    configured = os.environ.get("MAKEFUN_OUTPUT_DIR")
    base = Path(configured) if configured else Path("/output")
    return base / OUTPUT_FILE


def main() -> None:
    line = build_line()
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-199 chars, got {len(line)}")
    target = output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
