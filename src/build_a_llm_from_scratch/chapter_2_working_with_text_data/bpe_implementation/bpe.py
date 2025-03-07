#!/usr/bin/env python

"""Basic Implemention of BPE algorithm. For learning purposes."""

import json
from collections import Counter, deque
from functools import lru_cache


class BPETokenizerSimple:
    def __init__(self):
        pass

    def train(self, *args, **kwargs):
        pass

    def tokenize(self, token):
        pass

    def encode(self, text):
        pass

    def decode(self, token_ids):
        pass

    def save_vocab_and_merges(self, vocab_path, bpe_merges_path):
        pass

    def load_vocab_and_merges(self, vocab_path, bpe_merges_path):
        pass

    def find_freq_pair(token_ids, mode="most"):
        pass

    def replace_pair(token_ids, pair_id, new_id):
        pass

    def get_special_token_id(self, token):
        pass
