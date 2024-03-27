#!/usr/bin/python3
"""This module contains 1 function, text_indentation(text). Example:
    >>> text_indentation("Sentence1. Sentence2: Sentence3?")
    Sentence1.

    Sentence2:

    Sentence3?

"""


def text_indentation(text):
    """Prints text with 2 new lines after each '.', '?' and ':'
    text must be a string"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for split_char in ['.', '?', ':']:
        split = [s.strip() for s in text.split(split_char)]
        text = "{}\n\n".format(split_char).join(split)

    print(text, end="")
