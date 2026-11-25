#!/usr/bin/env python3
"""Ship It Friday entry: write one funny commit message to entry.txt.

Deterministic: the text is a fixed string. No clock, no randomness,
no network, no file reads.
"""

import os

ENTRY = "fix: it worked on my machine, so I shipped it to prod at 4:59pm on Friday and logged off"
# Gate: entry.txt must be UTF-8 text of 1 to 159 characters, not only
# whitespace. This line is 88 characters, one line, no trailing spaces.


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
