#!/usr/bin/python3
"""This module contains 1 function, print_square(size). Example:
    >>> print_square(3)
    ###
    ###
    ###
"""


def print_square(size):
    """Print a square of length 'size' to stout"""

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    line = "#" * size

    for _ in range(size):
        print("{}".format(line))
