#!/usr/bin/env python3
"""Six Words, One Story — make.fun entry.

Writes exactly one six-word story to /output/entry.txt.
Deterministic: same bytes on every run, no trailing newline.

The story: a wedding, a mistaken identity, and a choice —
six words, one whole life implied.
"""

import os

STORY = "Married the wrong twin. Stayed anyway."


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Exactly six words, 38 characters, no trailing newline.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
