#!/usr/bin/env python

from .simpletokenizerv1 import SimpleTokenizerV1

from typing import Optional

class SimpleTokenizerV2(SimpleTokenizerV1):
    def __init__(self, vocab: Optional[dict] = None):
        super(SimpleTokenizerV1, self).__init__(vocab)


if __name__ == "__main__":
    
