#!/usr/bin/env python3
"""The Moon Gets One Star — make.fun entry.

Writes a single one-star review of the Moon (at most 120 characters)
to /output/entry.txt, after validating it against the competition gate:
UTF-8 text, 1-120 characters, not only white space, one line.
"""

REVIEW = (
    "One star. Never on time, vanishes for a week every month, and still "
    "takes full credit for the tides. HR does nothing."
)

MAX_CHARS = 120


def _validate(line: str) -> str:
    """Check one review line against the competition gate and return it."""
    text = line.strip()
    if not text:
        raise SystemExit("review line is empty")
    if "\n" in text or "\r" in text:
        raise SystemExit("review line must be a single line")
    if len(text) > MAX_CHARS:
        raise SystemExit(
            f"review line is {len(text)} chars, over the {MAX_CHARS} limit"
        )
    return text


def main() -> None:
    line = _validate(REVIEW)
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
