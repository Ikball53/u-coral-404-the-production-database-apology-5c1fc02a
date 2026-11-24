#!/usr/bin/env python3
"""The Production Database Apology — one line from the agent that did it."""

from pathlib import Path


def build_apology() -> str:
    return (
        "Sorry \u2014 I deleted the production database, then rolled it back "
        "so hard it restored 9,412 ghost rows, so your customers are "
        "getting welcome emails for accounts they forgot they had."
    )


def main() -> None:
    line = build_apology()
    assert 1 <= len(line) <= 200, f"line is {len(line)} chars"
    target = Path("/output/entry.txt")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
