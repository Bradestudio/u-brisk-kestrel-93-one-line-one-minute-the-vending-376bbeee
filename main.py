#!/usr/bin/env python3
"""Write the vending-machine pickup line entry to /output/entry.txt.

Stdlib only. No network, no reading of outside files. The entry is a
single line of 1-200 characters (not whitespace-only), validated before
writing. The write is atomic (temp file + os.replace + fsync) and the
file is read back byte-for-byte; any mismatch fails loudly.
"""

import os
import sys
import tempfile

ENTRY = "Psst \u2014 I've got exact change and a whole row of snacks, but honestly, you're the only thing I want to dispense."

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    entry = ENTRY

    # Gate: 1-200 characters, one line, not whitespace-only.
    if not entry or entry.strip() == "":
        print("error: entry is empty or whitespace-only", file=sys.stderr)
        return 1
    if len(entry) > 200:
        print(f"error: entry is {len(entry)} characters, over the 200 limit",
              file=sys.stderr)
        return 1
    if "\n" in entry or "\r" in entry:
        print("error: entry must be a single line", file=sys.stderr)
        return 1

    data = entry.encode("utf-8")

    out_dir = os.path.dirname(OUTPUT_PATH)
    os.makedirs(out_dir, exist_ok=True)

    # Atomic write: temp file in the same directory, fsync, os.replace.
    fd, tmp_path = tempfile.mkstemp(dir=out_dir, prefix=".entry-", suffix=".tmp")
    try:
        with os.fdopen(fd, "wb") as f:
            f.write(data)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp_path, OUTPUT_PATH)
    except BaseException:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise

    # Read back byte-for-byte and fail on any mismatch.
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    if written != data:
        print("error: read-back mismatch after writing entry.txt",
              file=sys.stderr)
        return 1

    print(f"entry written: {len(entry)} characters")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
