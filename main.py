"""food-picture-01 entry: copy the bundled food picture to /output/entry.png.

Deterministic: the same input bytes are copied on every run, so both
grader runs write byte-identical output. Standard library only.
"""

import hashlib
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
source = HERE / "entry.png"
target = OUTPUT_DIR / "entry.png"
shutil.copyfile(source, target)

# Sanity check the copy is complete and identical to the bundled image.
assert hashlib.sha256(source.read_bytes()).hexdigest() == hashlib.sha256(
    target.read_bytes()
).hexdigest(), "copied image does not match the bundled image"
