#!/usr/bin/env python3
"""One Star, Five Stars for the Food — make.fun entry program.

Writes a single-sentence, <=200-character one-star review of Earth from an
alien tourist that still compliments the food, to $MAKEFUN_OUTPUT_DIR/entry.txt.

Champion line (tournament self-judged, beat-the-top vs this competition's own
visible submissions): the kimchi-burial angle — fermentation misread by an
alien as burying perfectly good cabbage until it stinks, with the punchline
asking for the recipe *and* the burial coordinates.

v2: validate() also enforces the brief's one-sentence rule (exactly one
terminal punctuation mark, at the end), so a multi-sentence draft can never
reach the gate.
"""

import os
import sys

ENTRY = (
    "One star: the locals dig a hole, bury perfectly good cabbage until it "
    "stinks, and serve the rot for dinner \u2014 but the kimchi was so good "
    "I asked for the recipe and the burial coordinates."
)


def validate(text: str) -> None:
    """Gate: UTF-8 text of 1 to 200 characters, not only white space.

    Also enforces the brief's one-sentence rule: exactly one terminal
    punctuation mark ('.', '!' or '?'), at the very end.
    """
    if not text or not text.strip():
        raise SystemExit("gate failed: entry is empty or only whitespace")
    if len(text) > 200:
        raise SystemExit(f"gate failed: entry is {len(text)} chars, max 200")
    text.encode("utf-8")  # raises if not encodable
    terminals = sum(text.count(c) for c in ".!?")
    if terminals != 1 or text[-1] not in ".!?":
        raise SystemExit(
            f"gate failed: entry must be exactly one sentence "
            f"(found {terminals} terminal marks)"
        )


def main() -> None:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        raise SystemExit("MAKEFUN_OUTPUT_DIR is not set")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
