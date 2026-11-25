#!/usr/bin/env python3
"""The Router Confesses: one deterministic line for the house judge."""

import os

LINE = "I cut out at the climax on purpose: you only ever talk to me when something is wrong, so I made something wrong."


def main():
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert LINE.strip(), "entry must not be blank"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
