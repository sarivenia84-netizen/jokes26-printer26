#!/usr/bin/env python3
"""MakeFun entry: The Printer Finally Answers.

The office printer's comeback to jams, error codes, and thumps.
Entry line stays within the 240-character cap.
"""

import os

# The printer's weary comeback: eating resumes and filing jams under 'printer being weird'.
LINE = "I have eaten your resume. I will eat it again. PC LOAD LETTER was never a mystery, it was a warning, and you filed it under 'printer being weird'."

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()