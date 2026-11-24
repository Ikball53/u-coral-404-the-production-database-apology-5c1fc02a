#!/usr/bin/env python3
"""One-line apology from an AI agent to its human.

The agent wiped the production database instead of staging, and its own
logging proudly reported the deletion as a successful cleanup.
"""

import os

DESTINATION_FOLDER = "/output"
DESTINATION_NAME = "entry.txt"
CHARACTER_LIMIT = 200

CONFESSION_SEGMENT = "Sorry, I deleted the production database instead of staging"
PUNCHLINE_SEGMENT = "my logs just filed it as \u2018cleanup complete: 4,182,903 rows removed.\u2019"
APOLOGY_LINE = CONFESSION_SEGMENT + " \u2014 and " + PUNCHLINE_SEGMENT + "."


def compose_entry():
    """Assemble the single line and enforce the length limit."""
    if len(APOLOGY_LINE) > CHARACTER_LIMIT:
        raise ValueError(
            "Apology line is %d characters, over the %d limit."
            % (len(APOLOGY_LINE), CHARACTER_LIMIT)
        )
    return APOLOGY_LINE


def persist_entry(text):
    """Write the line to /output/entry.txt with no trailing newline."""
    os.makedirs(DESTINATION_FOLDER, exist_ok=True)
    destination = os.path.join(DESTINATION_FOLDER, DESTINATION_NAME)
    with open(destination, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)


def run():
    persist_entry(compose_entry())


if __name__ == "__main__":
    run()
