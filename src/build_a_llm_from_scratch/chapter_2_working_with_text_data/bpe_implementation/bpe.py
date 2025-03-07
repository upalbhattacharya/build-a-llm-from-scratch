#!/usr/bin/env python

"""Basic Implemention of BPE algorithm. For learning purposes."""

import json
from collections import Counter, deque
from functools import lru_cache


class BPETokenizerSimple:
    def __init__(self):
        self.vocab: dict = {}
        self.inverse_vocab: dict = {}
        self.bpe_merges: dict = {}

    def train(
        self,
        train_text: str,
        vocab_size: int,
        allowed_special: set(str) = {"<|endoftext|>"},
    ):

        # Create initial dictionary
        # First 256 ASCII characters
        unique_chars = [chr(i) for i in range(256)]
        if " " not in unique_chars:
            unique_chars.append(" ")

        self.vocab = {i: char for i, char in enumerate(unique_chars)}
        self.inverse_vocab = {char: i for i, char in self.vocab.items()}

        # Iteratively add pairs

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
