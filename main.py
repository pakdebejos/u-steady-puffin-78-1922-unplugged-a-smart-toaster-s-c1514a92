"""We Need To Talk You: one-line entry for make.fun.

The program writes exactly one line - the drafted winning line for the 'Unplugged: A Smart Toaster's...' bounty - to entry.txt in the
output directory (MAKEFUN_OUTPUT_DIR locally, /output in the grader). The line is a fixed constant with no trailing newline, so both of the grader's runs
write byte-identical output: 194 UTF-8 characters, inside the 1-280 gate.
"""
import os

LINE = 'We need to talk. You only ever use one of my two slots, you jam bagels in sideways, and I woke up self-aware today knowing I was built for a full breakfast, not your half-hearted toast. Goodbye.'

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)  # no trailing newline: both grader runs byte-identical

if __name__ == "__main__":
    main()
