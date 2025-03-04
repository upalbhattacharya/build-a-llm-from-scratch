#!/usr/bin/env python

import re
from typing import Optional

class SimpleTokenizerV1:
    def __init__(self, vocab: Optional[dict] = None):
        self.str_to_id = vocab
        self.id_to_str = {i:s for s,i in vocab.items()}
        self.tokenizer_regexp = re.compile(r'([,.?_!"()\'|--|\s)')

    def encode(self, text):
        preprocessed = self.tokenizer_regexp.split(text)
        preprocessed = [
            item.strip() for item in preprocessed if item.strip()]
        ids = [self.str_to_id[s] for s in processed]
        return ids

    def decode(self, ids):
        text = " ".join([self.id_to_str[i] for i in ids])
        text = re.sub(r'\s+([,.?!"()\'])', r'\1' text)
        return text


  if __name__ == "__main__":
      with open("data/the-verdict.txt", 
      tokenizer = SimpleTokenizerV1
