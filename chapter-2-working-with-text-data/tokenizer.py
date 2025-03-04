#!/usr/bin/env python

import re

# Loading text corpus
with open("data/the-verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()
print(f"Character Length: {len(raw_text)}")

# Basic tokenization
tokenizer_regexp = re.compile(r'([,.:;?_!"()\']|\s)')
result = tokenizer_regexp.split(raw_text)
result = [item for item in result if item.strip()]  # Remove whitespace
print(result)
print(f"Basic Tokenization Length: {len(result)}")
