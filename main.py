#!/usr/bin/env python3
"""Duskline Food Stars — make.fun entry for
"One Star, Five Stars for the Food"
(u-po-pu-one-star-five-stars-for-the-food-f9166ee7).

A one-sentence alien tourist review of Earth (one star overall, five
stars for the food), written to $MAKEFUN_OUTPUT_DIR/entry.txt.

Python 3.13 standard library only. Deterministic, no network, no
arguments. The program writes ONLY to $MAKEFUN_OUTPUT_DIR (default
"/output") and never touches the repository directory.
"""

import os
import sys
from pathlib import Path

# One sentence, 171 characters: three escalating earthly grievances,
# then the turn — the tacos are worth coming back (by abduction) for.
ENTRY = (
    "One star: Earth charged me rent to breathe, fined me for existing, "
    "and made me queue behind a goose \u2014 but the tacos were so good "
    "I have already booked my return abduction."
)

MAX_CHARS = 200


def entry_is_valid(text: str) -> str | None:
    """Return an error message, or None when the text passes the gate."""
    stripped = text.strip()
    if not stripped:
        return "entry is empty"
    if len(stripped) > MAX_CHARS:
        return f"entry is {len(stripped)} chars, over the {MAX_CHARS} limit"
    if stripped.count(".") != 1 or not stripped.endswith("."):
        return "entry must be exactly one sentence"
    return None


def write_entry(out_dir: str) -> bool:
    """Write entry.txt into out_dir. False when the directory is unusable."""
    try:
        target_dir = Path(out_dir)
        target_dir.mkdir(parents=True, exist_ok=True)
        (target_dir / "entry.txt").write_text(
            ENTRY.strip() + "\n", encoding="utf-8", newline="\n"
        )
    except OSError as exc:
        # Never crash when the output directory cannot be written.
        print(f"could not write entry: {exc}", file=sys.stderr)
        return False
    return True


def main() -> int:
    problem = entry_is_valid(ENTRY)
    if problem is not None:
        print(f"invalid entry: {problem}", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    if not write_entry(out_dir):
        return 0
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
