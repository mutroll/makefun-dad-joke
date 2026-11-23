"""Dad Joke Showdown entry.

Writes one dad joke (at most 200 characters) to /output/entry.txt.
Python 3.13 standard library only; fully deterministic.
"""

from pathlib import Path

JOKE = "I asked the tire why it looked so tired. It sighed, 'I've been going around in circles all day.'"

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the file holds exactly the joke, nothing else.
    OUTPUT_PATH.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
