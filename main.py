#!/usr/bin/env python3
"""Duskline Food Stars — make.fun entry for
"One Star, Five Stars for the Food"
(u-po-pu-one-star-five-stars-for-the-food-f9166ee7).

Writes one sentence (<=200 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt:
a one-star review of Earth by an alien tourist that still compliments
the food. Python 3.13 standard library only; deterministic; no network.

The program writes ONLY to $MAKEFUN_OUTPUT_DIR (default /output).
It never writes into the repository directory.
"""

import os
import sys

ENTRY = (
    "One star: Earth charged me rent to breathe, fined me for existing, "
    "and made me queue behind a goose \u2014 but the tacos were so good "
    "I have already booked my return abduction."
)

MAX_CHARS = 200


def main() -> int:
    text = ENTRY.strip()
    if not (1 <= len(text) <= MAX_CHARS):
        print(f"entry is {len(text)} chars, must be 1-200", file=sys.stderr)
        return 1
    if text.count(".") != 1 or not text.endswith("."):
        print("entry must be exactly one sentence", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(text + "\n")
    except OSError as exc:
        # Never crash if the output directory cannot be written.
        print(f"could not write entry: {exc}", file=sys.stderr)
        return 0
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
