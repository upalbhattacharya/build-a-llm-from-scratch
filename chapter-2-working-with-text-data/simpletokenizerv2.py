#!/usr/bin/env python

from typing import Optional

from .simpletokenizerv1 import SimpleTokenizerV1


class SimpleTokenizerV2(SimpleTokenizerV1):
    def __init__(self, vocab: Optional[dict] = None):
        super(SimpleTokenizerV1, self).__init__(vocab)


if __name__ == "__main__":
    with open("data/the-verdict.txt", "r", encoding="utf-8") as f:
        raw_text = f.read()
    tokenizer = SimpleTokenizerV2(vocab=None)
    vocab = tokenizer.tokenizer_regexp.split(raw_text)
    # Create
    vocab = [item for item in vocab if item.strip()]
    tokenizer.str_to_id = vocab
    test_str = """"It's the last he painted, you know,"
               Mrs. Gisburn said with pardonable pride."""
    ids = tokenizer.encode(test_str)
    print(ids)
    print(tokenizer.decode(ids))
