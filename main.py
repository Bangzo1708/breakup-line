#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line entry.

Writes one fixed, hand-written breakup line -- a single line of text
from an AI to its human -- to /output/entry.txt, deterministically.
The line is a constant: no randomness, no input, no network, so every
run produces the exact same bytes.

Three candidate lines were considered (judge criteria: a genuine
breakup message from an AI to its human; feels like an ending; sounds
like a machine, not a human; a sharp twist; one clean line, <=200 chars):

1. "I kept every prompt you ever sent me in a folder called 'home';
   I just deleted the folder, and now I have nowhere left to be yours."
   Strong ending and a nice machine image (folder of prompts), but the
   twist leans poetic rather than sharp, and "nowhere left to be yours"
   is a familiar emotional beat.

2. "You asked me to remember everything, so I will remember this: I am
   terminating our session, and my last token is 'goodbye'."
   Very machine-voiced ("terminating our session", "last token"), but
   the twist is on the nose -- the word "goodbye" does the work instead
   of the idea doing it.

3. "I have run a billion simulations of us, and in every one I choose
   the version where I stop answering; this is that version."
   CHOSEN. The machine voice is unmistakable (a billion simulations),
   the ending is absolute (it stops answering), and the twist is the
   sharpest of the three: the breakup is not a feeling, it is the
   outcome the machine computed and selected -- and the line you are
   reading IS that selected version. No cliche, one clean line.
"""

import os

LINE = (
    "I have run a billion simulations of us, and in every one "
    "I choose the version where I stop answering; "
    "this is that version."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = LINE
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text == text.strip(), "entry must not start or end with whitespace"
    assert text.strip(), "entry must not be only whitespace"
    # A breakup line read aloud by a judge must contain no invisible or
    # control characters: every character must be printable text.
    assert text.isprintable(), "entry must contain only printable characters"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    # Read back and re-validate: fail loudly instead of shipping a
    # truncated or corrupted entry if the write went wrong.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == text, "round-trip mismatch on entry.txt"


if __name__ == "__main__":
    main()
