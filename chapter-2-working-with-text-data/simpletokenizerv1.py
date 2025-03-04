#!/usr/bin/env python

import re
from typing import Optional

class SimpleTokenizerV1:
    def __init__(self, vocab: Optional[dict] = None):
        if vocab:
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

    @property
    def str_to_id(self)
        return self.str_to_id

    @property.setter
    def str_to_id(self, vocab):
        self._str_to_id = vocab
        self._id_to_str = {i:s for s,i in vocab.items()}


  if __name__ == "__main__":
      with open("data/the-verdict.txt", "r", encoding="utf-8") as f:
          raw_text = f.read()
      tokenizer = SimpleTokenizerV1(vocab=None)
      vocab = tokenizer.tokenizer_regexp.split(raw_text)
