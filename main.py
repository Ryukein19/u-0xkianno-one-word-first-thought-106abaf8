import os
# One-word entry: the word below is the entire submission.
# Writes the word to /output/entry.txt.
LINE = "Serendipity"
os.makedirs("/output", exist_ok=True)
open("/output/entry.txt", "w", encoding="utf-8").write(LINE)
