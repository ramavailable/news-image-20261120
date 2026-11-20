"""make.fun entry: Sum up 20 November's world news in one image.

The program copies the image held in this repository to the output
directory. It uses only the Python standard library, needs no network,
and writes the same bytes on every run, so the grader's two runs match.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

OUT.mkdir(parents=True, exist_ok=True)
shutil.copyfile(HERE / "entry.png", OUT / "entry.png")
