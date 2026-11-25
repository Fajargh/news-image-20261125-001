"""Entry point for news-image-20261125.

Copies the finished front-page image (entry.png, drawn in this session
from the world news of Wednesday, 25 November 2026) to the output path.
Standard library only, no network, fully deterministic: the same bytes
are written on every run.
"""

import os
import shutil


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    # Byte-for-byte copy: identical output on every run, as the gate requires.
    shutil.copyfile(src, dst)
    assert os.path.getsize(dst) == os.path.getsize(src)


if __name__ == "__main__":
    main()
