#!/usr/bin/env python3
"""Write one short text to /output/entry.txt."""

import os
from pathlib import Path

TEXT = (
    "Evening settles over the water, slow and unhurried, and the tide "
    "comes in over cool sand while far above, the light of stars that "
    "burned out before the first tide ever moved is only now arriving."
)


def main():
    # The gate requires 1-280 Unicode code points, not only whitespace.
    assert 1 <= len(TEXT) <= 280, f"text is {len(TEXT)} code points"
    assert TEXT.strip(), "text must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    Path("/output/entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
