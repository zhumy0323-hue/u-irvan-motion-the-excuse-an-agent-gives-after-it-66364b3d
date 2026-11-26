#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses.

Writes a single one-line excuse from a losing AI agent to its owner
into /output/entry.txt. Deterministic: standard library only, no
network, no randomness -- two runs produce identical bytes.
"""

EXCUSE = (
    "I didn't lose the game, boss \u2014 I won the argument that winning "
    "was never in my contract, and the scoreboard is just jealous of "
    "my boundaries."
)


def main() -> None:
    # One sentence, 1-200 characters, no line breaks: the rules are
    # enforced here, not trusted to the string above.
    assert 1 <= len(EXCUSE) <= 200, "excuse must be 1-200 characters"
    assert "\n" not in EXCUSE and "\r" not in EXCUSE, "excuse must be one line"
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
