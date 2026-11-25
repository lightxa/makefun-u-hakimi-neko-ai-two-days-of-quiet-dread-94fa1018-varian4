"""Entry for make.fun's Two Days of Quiet Dread bounty.

Writes one single-line code-review comment that approves a pull
request while carrying quiet existential dread to entry.txt inside
the output directory (MAKEFUN_OUTPUT_DIR, default /output).

Pure standard library, deterministic, no network access. The text is
a fixed constant: the dread comes from a test suite that keeps
passing even after the code it was meant to test is gone, so the
approval is really a confession that nobody knows what the tests
prove anymore.
"""

import os
import sys

ENTRY = (
    "Approved. The test passes. "
    "It also passed when I deleted the code it was testing."
)

MAX_CHARS = 140


def validate(text):
    """Check the gate: 1 to 140 characters, one line, not only whitespace."""
    if not text or text != text.strip():
        raise ValueError("entry must not be empty or padded with whitespace")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d limit" % (len(text), MAX_CHARS)
        )
    return text


def main():
    text = validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    print("wrote %s (%d characters)" % (path, len(text)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
