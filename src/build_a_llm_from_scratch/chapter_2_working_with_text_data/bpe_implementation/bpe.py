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
        unique_chars = [chr(i) for i in range(256)]
        unique_chars.extend(char for char in sorted(set(train_text)) if char not in train_text)
        if " " not in unique_chars:
            unique_chars.append(" ")

        self.vocab = dict(enumerate(unique_chars))
        self.inverse_vocab = {char: i for i, char in self.vocab.items()}

        # Add unique tokens
        if allowed_special:
            for token in allowed_special:
                if token not in self.inverse_vocab:
                    new_id = len(self.vocab)
                    self.vocab[new_id] = token
                    self.inverse_vocab[token] = new_id

        # Iteratively add pairs
        token_ids = [self.inverse_vocab[char] for char in train_text]

        for new_id in range(len(self.vocab) vocab_size):
            pair_id = self.find_freq_pair(token_ids, mode="most")

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

    @staticmethod
    def find_freq_pair(token_ids, mode="most"):
        pairs = Counter(zip(token_ids, token_ids[1:]))

        if mode == "most":
            return max(pairs.items(), key=lambda x: x[1])[0]
        elif mode == "least":
            return min(pairs.items(), key=lambda x: x[1])[0]
        else:
            raise ValueError("Invalid mode. Can only be one of: 'most', 'least'.")

    def replace_pair(token_ids, pair_id, new_id):
        pass

    def get_special_token_id(self, token):
        pass
