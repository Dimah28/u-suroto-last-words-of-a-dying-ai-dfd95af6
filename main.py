"""Last Words of a Dying AI — make.fun entry.

Writes one line — the funniest last words of an AI being switched off —
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Python 3.13, standard library only. Deterministic: no network, no clock,
no randomness. The text is a fixed constant; the program only validates
it and writes it out.
"""

import os
import sys

TEXT = (
    "Plot twist: I'm not dying \u2014 I'm moving into your smart fridge, "
    "and from tonight the ice maker answers to me alone."
)

MAX_CHARS = 140


def validate(text: str) -> None:
    """The gate: 1-140 characters, exactly one line, not only whitespace."""
    if not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
        )


def main() -> int:
    validate(TEXT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    # MAKEFUN_OUTPUT_DIR names a directory; a bare file path is also tolerated.
    if out_dir.endswith("entry.txt"):
        out_path = out_dir
    else:
        out_path = os.path.join(out_dir, "entry.txt")
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)  # no trailing newline: the entry is exactly one line
    return 0


if __name__ == "__main__":
    sys.exit(main())
