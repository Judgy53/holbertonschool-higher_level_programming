#!/usr/bin/python3
"""
This module provides one function, add_integer(a, b). For example:
>>> add_integer(1, 2)
3
"""


def add_integer(a, b=98):
    """Returns the addition of a and b.
    a and b must be integers or floats.
    They will get casted to integers if they are floats"""

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b
