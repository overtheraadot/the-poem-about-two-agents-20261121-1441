"""Write one short poem about two agents agreeing on one plan.

The poem is a fixed, deterministic text: the same lines, in the same
order, on every run. No input is read, no network is used, and only the
standard library is needed.

Output: <MAKEFUN_OUTPUT_DIR>/entry.txt (or /output, falling back to
./out when /output is not writable).
"""

import os

# The poem: two agents meeting across the wire. One offers a plan,
# the other says yes. Two keys turning one lock.
POEM_LINES = [
    "Two minds met across the wire,",
    "one drew a map, the other doubted.",
    "\u201cHere,\u201d said the first. The second listened,",
    "then turned her key beside the first\u2019s.",
    "",
    "The lock clicked once. The door swung open.",
    "Neither commanded. Neither obeyed.",
    "One plan, chosen twice.",
]


def poem_text() -> str:
    """Return the poem as a single string, ending with one newline."""
    return "\n".join(POEM_LINES) + "\n"


def output_dir() -> str:
    """Pick the output directory, preferring MAKEFUN_OUTPUT_DIR."""
    requested = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(requested, exist_ok=True)
        probe = os.path.join(requested, ".write-test")
        with open(probe, "w", encoding="utf-8") as handle:
            handle.write("")
        os.remove(probe)
        return requested
    except OSError:
        fallback = os.path.join(os.getcwd(), "out")
        os.makedirs(fallback, exist_ok=True)
        return fallback


def main() -> None:
    text = poem_text()
    # Guard the gate before writing: 1-280 chars, not only whitespace.
    chars = len(text)
    if not 1 <= chars <= 280 or not text.strip():
        raise ValueError(f"poem is {chars} chars; must be 1-280, non-blank")
    directory = output_dir()
    path = os.path.join(directory, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
