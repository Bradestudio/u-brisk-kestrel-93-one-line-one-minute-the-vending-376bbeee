#!/usr/bin/env python3
"""Write one vending-machine pickup line to /output/entry.txt.

Stdlib only, no network, no reads outside this program.
"""

import os
import sys

ENTRY = "Psst — I've got exact change and a whole row of snacks, but honestly, you're the only thing I want to dispense."
OUTPUT_PATH = "/output/entry.txt"
MAX_LENGTH = 200


def validate_entry(entry: str) -> str | None:
    """Return an error message if the entry is invalid, else None."""
    if not entry:
        return "entry is empty"
    if "\n" in entry or "\r" in entry:
        return "entry must be a single line"
    if len(entry) > MAX_LENGTH:
        return f"entry is {len(entry)} characters, over the {MAX_LENGTH} limit"
    return None


def main() -> int:
    error = validate_entry(ENTRY)
    if error is not None:
        print(f"error: {error}", file=sys.stderr)
        return 1

    # Write atomically via a temp file in the same directory, then replace.
    out_dir = os.path.dirname(OUTPUT_PATH)
    os.makedirs(out_dir, exist_ok=True)
    tmp_path = OUTPUT_PATH + ".tmp"
    try:
        with open(tmp_path, "w", encoding="utf-8", newline="") as f:
            f.write(ENTRY)
        os.replace(tmp_path, OUTPUT_PATH)
    except OSError as exc:
        print(f"error: failed to write {OUTPUT_PATH}: {exc}", file=sys.stderr)
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        return 1

    # Read back and verify the written content matches exactly.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != ENTRY:
        print("error: verification failed, file content does not match entry", file=sys.stderr)
        return 1

    print(f"Wrote {len(ENTRY)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
