"""news-summary-01 entry (Python 3.13, standard library only).

Copies the summary beside this file to the output entry file.
The gate reads exactly the bytes written, so the copy is byte-exact:
no line ending is added, removed, or translated. After copying, the
program verifies the written bytes match the source and that the text
is inside the gate's 1-2,000 character window.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
SOURCE = HERE / "summary.txt"
TARGET = OUTPUT_DIR / "entry.txt"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
shutil.copyfile(SOURCE, TARGET)

# Self-check: the bytes written must match the source exactly, and the
# text must be within the gate's 1-2,000 character window.
written = TARGET.read_bytes()
assert written == SOURCE.read_bytes(), "entry.txt differs from summary.txt"
chars = len(written.decode("utf-8"))
assert 1 <= chars <= 2_000, f"character count {chars} outside 1-2000"
print(f"wrote {TARGET} ({chars} characters, {len(written)} bytes)")
