import re
from copy import deepcopy
from random import shuffle

from .exceptions import NotEncoderFormatError


def encode(text):
    t = re.compile(r'(\w+)', re.U)
    output_list = []
    raw_words = []

    for word in text.split():
        r = re.search(t, word)
        matched = r.group()

        if len(matched) > 3:
            shuffled = shuffle_word(matched)
            word = word[0:r.start()] + shuffled + word[r.end():]

            if matched != shuffled:
                raw_words.append(matched)

        output_list.append(word)

    raw_words.sort(key=str.lower)
    result = "\n-weird-\n{}\n-weird-\n{}".format(" ".join(output_list), " ".join(raw_words))

    return result.encode("utf-8").decode("unicode_escape")


def shuffle_word(word):
    """
    inp: string
    """
    trimmed = list(word[1:-1])
    shuffled = deepcopy(trimmed)

    if len(set(trimmed)) > 1:
        while shuffled == trimmed:
            shuffle(shuffled)

    return word[0] + ''.join(shuffled) + word[-1]


def decode(text):
    encoded_text, original_words = process_decoder_input(text)
    result = []

    t = re.compile(r'(\w+)', re.U)

    for word in encoded_text:
        r = re.search(t, word)
        matched = r.group()

        if len(matched) > 3:
            for original_word in original_words:
                if are_anagrams(matched, original_word):
                    word = word[0:r.start()] + original_word + word[r.end():]

        result.append(word)

    return ' '.join(result).encode("utf-8").decode("unicode_escape")


def process_decoder_input(text):
    text_split = text.split("\\n-weird-\\n")
    if len(text_split) != 3:
        raise NotEncoderFormatError("String doesn't have a proper Encoder output format")

    encoded = text_split[1].split()
    original = text_split[2].split()
    return encoded, original


def are_anagrams(word, original):
    if sorted(word) == sorted(original):
        return True
    return False
