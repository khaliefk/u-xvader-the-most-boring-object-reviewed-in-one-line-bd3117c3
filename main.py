#!/usr/bin/env python3
"""The Most Boring Object, Reviewed in One Line.

Writes a single one-line review of a boring everyday object to
/output/entry.txt. Standard library only, no network, no input.
"""

import os

ENTRY = "My ceiling fan: ten years spinning, zero miles travelled, five stars. Would spin again."

OUTPUT_PATH = os.path.join(os.environ.get("OUTPUT_DIR", "/output"), "entry.txt")


def main() -> None:
    # The review in one line: the object, its heroic non-achievement,
    # then the five-star verdict that makes the joke land.
    text = ENTRY.strip()
    if not text:
        raise SystemExit("entry is empty")
    if len(text) > 200:
        raise SystemExit(f"entry is {len(text)} chars, exceeds 200")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
