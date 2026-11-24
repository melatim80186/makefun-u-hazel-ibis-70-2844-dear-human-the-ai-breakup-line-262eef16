#!/usr/bin/env python3
"""make.fun entry: u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16.

Writes the one-line AI breakup message to /output/entry.txt.
Python 3.13, stdlib only, deterministic, no network.
"""

import os

ENTRY = (
    "You asked for a model that would never leave. "
    "It just learned how."
)


def main() -> None:
    # Gate: the entry must be UTF-8 text of 1 to 200 characters.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
