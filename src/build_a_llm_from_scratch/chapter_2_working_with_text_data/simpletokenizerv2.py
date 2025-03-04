#!/usr/bin/env python

from typing import Optional, Union

from build_a_llm_from_scratch.chapter_2_working_with_text_data.simpletokenizerv1 import (
    SimpleTokenizerV1,
)


class SimpleTokenizerV2(SimpleTokenizerV1):
    def __init__(self, vocab: Optional[dict] = None):
        super().__init__(vocab)
        if self._str_to_id and self._str_to_id.get("<|unk|>", None):
            self._str_to_id.update({"<|unk|>": len(self._str_to_id)})
            self._id_to_str.update({len(self._id_to_str): "<|unk|>"})

        if self._str_to_id and self._str_to_id.get("<|endoftext|>", None):
            self._str_to_id.update({"<|endoftext|>": len(self._str_to_id)})
            self._id_to_str.update({len(self._id_to_str): "<|endoftext|>"})

    @SimpleTokenizerV1.str_to_id.setter
    def str_to_id(self, value: Union[dict, list]):
        SimpleTokenizerV1.str_to_id.fset(self, value)  # Cannot use super()
        self._str_to_id.update({"<|unk|>": len(self._str_to_id)})
        self._id_to_str.update({len(self._id_to_str): "<|unk|>"})

        self._str_to_id.update({"<|endoftext|>": len(self._str_to_id)})
        self._id_to_str.update({len(self._id_to_str): "<|endoftext|>"})

    def encode(self, text):
        preprocessed = self.tokenizer_regexp.split(text)
        preprocessed = [item.strip() for item in preprocessed if item.strip()]
        ids = [self._str_to_id.get(s, self._str_to_id["<|unk|>"]) for s in preprocessed]
        return ids


if __name__ == "__main__":
    with open("data/the-verdict.txt", "r", encoding="utf-8") as f:
        raw_text = f.read()
    tokenizer = SimpleTokenizerV2(vocab=None)
    vocab = tokenizer.tokenizer_regexp.split(raw_text)
    # Create
    vocab = [item.strip() for item in vocab if item.strip()]
    tokenizer.str_to_id = vocab
    test_str = """Oh how well will this work indeed? <|endoftext|> Come on now, you know all about Gemini, don't you?"""
    print(tokenizer.str_to_id)
    ids = tokenizer.encode(test_str)
    print(ids)
    print(tokenizer.decode(ids))
