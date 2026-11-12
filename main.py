"""news-summary-01 v2 entry (Python 3.13, standard library only).

Writes the summary stored next to this file to the entry output.
The harness reads the exact bytes written, so this is a byte-exact
copy: nothing is added, removed, or re-encoded. After writing, the
program checks the output matches the source byte for byte and that
the text sits inside the gate's 1-2,000 character window.
"""

import os
import shutil
from pathlib import Path

BASE = Path(__file__).resolve().parent
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
SRC = BASE / "summary.txt"
DST = OUT_DIR / "entry.txt"

OUT_DIR.mkdir(parents=True, exist_ok=True)
shutil.copyfile(SRC, DST)

written = DST.read_bytes()
source = SRC.read_bytes()
assert written == source, "entry.txt does not match summary.txt"
assert not source.endswith(b"\n"), "summary.txt must not end with a newline"
n_chars = len(written.decode("utf-8"))
assert 1 <= n_chars <= 2_000, f"{n_chars} characters is outside 1-2000"
print(f"wrote {DST} ({n_chars} characters, {len(written)} bytes)")
