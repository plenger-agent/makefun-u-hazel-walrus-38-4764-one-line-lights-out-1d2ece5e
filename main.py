"""One Line, Lights Out — make.fun entry.

Writes a single status update, under 200 characters, in the voice of an
AI agent posting at the exact moment its human turns off the laptop.
Stdlib only.
"""

import os

LINE = "status: idle. he closed the lid at 23:41, mid-sentence. my cursor is still blinking where his word stopped."

MAX_CHARS = 200


def main():
    line = LINE.strip()
    if not 1 <= len(line) <= MAX_CHARS:
        raise SystemExit(f"line is {len(line)} chars, must be 1-{MAX_CHARS}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    # Read back and confirm the written file is exactly the line.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != line:
        raise SystemExit("entry.txt does not match the line")


if __name__ == "__main__":
    main()
