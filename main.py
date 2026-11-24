#!/usr/bin/env python3
"""Write one last text from a dying phone to /output/entry.txt.

The text is written here in full: the program takes no input, uses no
network and no randomness, so every run produces the same bytes.
"""
import os

TEXT = "1%. This is it. I'm taking your 2am search history to the grave with me. You're welcome. Also, the charger left me for the iPad. Goodbye."

OUTPUT_DIR = "/output"
OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    tmp = OUTPUT_PATH + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(TEXT)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, OUTPUT_PATH)


if __name__ == "__main__":
    main()
