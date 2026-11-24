#!/usr/bin/env python3
"""Write one last text from a dying phone to /output/entry.txt.

The text is written here in full: the program takes no input, uses no
network and no randomness, so every run produces the same bytes.

The line is built against the judge brief, in the phone's own voice:
a dying phone that has kept its owner's secrets and dies with them.
Its joke turns twice. First the phone takes the owner's 2am search
history to the grave with it, and calls that a favour ("You're
welcome"). Then it gossips on its way out: the charger left it for
the iPad. The detail is specific (2am search history, the iPad), the
voice stays the phone's from the first word to the last, and at 137
characters it wastes nothing.

Two other angles were drafted and rejected. A screen-time line that
ends "tell the charger I loved her" leans on the charger-goodbye
cliche the brief penalises, the line a hundred other entrants will
also write. A line where the phone confesses it faked one percent
for twenty minutes is a known meme, so it fails the brief's freshness
test and reads as a prank rather than a dying phone's last text.
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
