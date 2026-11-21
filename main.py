"""Entry program for make.fun's "The joke about the demo" bounty.

Writes one line of UTF-8 text to /output/entry.txt: a one-line joke
about working beside AI coding agents. Deterministic, no network,
no input — the same bytes come out on every run.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

JOKE = (
    "My AI coding agent finished the feature in four minutes "
    "— then spent forty explaining why it was my idea all along."
)


def render_entry() -> str:
    """Return the exact text the entry file must hold."""
    text = JOKE.strip()
    if not text:
        raise ValueError("entry text must not be blank")
    if len(text) > 280:
        raise ValueError("entry text exceeds the 280 character gate")
    return text + "\n"


def write_entry(path: Path = OUTPUT_PATH) -> Path:
    """Write the rendered entry text to path, creating /output if needed."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render_entry(), encoding="utf-8")
    return path


def main() -> None:
    written = write_entry()
    print(f"wrote {written} ({written.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
