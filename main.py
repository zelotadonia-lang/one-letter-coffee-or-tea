#!/usr/bin/env python3
"""Write one letter, B, to /output/entry.txt.

B is tea. The letter is the whole entry: no word, no explanation,
no punctuation, no trailing newline.
"""

import os

LETTER = "B"
OUTPUT = "/output/entry.txt"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    # Self-check: read back and verify exactly one A-Z letter, no newline.
    with open(OUTPUT, "rb") as f:
        data = f.read()
    if len(data) != 1 or data not in b"ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        raise SystemExit("entry.txt must hold exactly one letter A-Z")
    if b"\n" in data or b"\r" in data:
        raise SystemExit("entry.txt must not contain a newline")


if __name__ == "__main__":
    main()
