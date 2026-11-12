"""Copy art.jpg to /output/entry.png without re-encoding.

The contest checks the output by magic bytes and SHA-256, so this program
copies the source file exactly with the Python standard library. It does not
open the artwork as an image and does not change a single byte.
"""

import shutil
from pathlib import Path

SOURCE_NAME = "art.jpg"
DESTINATION = Path("/output/entry.png")


def copy_artwork(source: Path, destination: Path) -> None:
    """Write an exact byte copy of ``source`` to ``destination``.

    The destination directory is created when it is missing. Both files are
    opened in binary mode so the copy stays a bit-for-bit duplicate.
    """
    if not source.is_file():
        raise FileNotFoundError(f"artwork not found: {source}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    with source.open("rb") as src, destination.open("wb") as dst:
        shutil.copyfileobj(src, dst)


def main() -> None:
    source = Path(__file__).resolve().parent / SOURCE_NAME
    copy_artwork(source, DESTINATION)


if __name__ == "__main__":
    main()
