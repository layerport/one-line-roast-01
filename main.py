#!/usr/bin/env python3
"""One-line roast: the gadget you use every day.

Writes a single original roast line to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when that is set),
with no trailing newline. Python 3.13 stdlib only, no network,
fully deterministic.
"""

import os

ROAST = (
    "My banking app texts me a six-digit code, then logs me out "
    "for taking too long to read the code it just sent."
)


def main() -> None:
    line = ROAST
    assert 1 <= len(line) <= 200, "roast must be 1-200 characters"
    assert "\n" not in line, "roast must be a single line"
    assert line.strip(), "roast must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
