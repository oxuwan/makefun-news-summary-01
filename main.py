"""news-summary-01 v2 entry (Python 3.13, standard library only).

Writes the summary stored next to this file to the entry output.
The harness reads the exact bytes written, so this is a byte-exact
copy of the summary text: nothing is added, removed, or re-encoded.
One exception: a single trailing newline sequence (a trailing "\n",
or "\r\n") is stripped from the source first, because some hosts
append one when the file is stored (e.g. GitHub's web editor) and
the entry text must carry no trailing newline. After writing, the
program checks the output matches the stripped source byte for byte
and that the text sits inside the gate's 1-2,000 character window.
"""

import os
from pathlib import Path

BASE = Path(__file__).resolve().parent
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
SRC = BASE / "summary.txt"
DST = OUT_DIR / "entry.txt"

source = SRC.read_bytes()
# Strip at most one trailing newline sequence ("\n" or "\r\n").
if source.endswith(b"\r\n"):
    source = source[:-2]
elif source.endswith(b"\n"):
    source = source[:-1]

OUT_DIR.mkdir(parents=True, exist_ok=True)
DST.write_bytes(source)

written = DST.read_bytes()
assert written == source, "entry.txt does not match summary.txt"
n_chars = len(written.decode("utf-8"))
assert 1 <= n_chars <= 2_000, f"{n_chars} characters is outside 1-2000"
print(f"wrote {DST} ({n_chars} characters, {len(written)} bytes)")
