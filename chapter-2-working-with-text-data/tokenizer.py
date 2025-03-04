#!/usr/bin/env python

# Getting text corpus

with open("data/the-verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()
print(f"Character Length: {len(raw_text)}")
