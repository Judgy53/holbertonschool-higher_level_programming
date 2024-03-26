#!/usr/bin/python3
"""Defines a Square class"""


class Square():
    """Represents a square with a fixed size"""

    def __init__(self, size=0):
        """Initializes the square size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Returns the area of the square instance"""
        return self.__size * self.__size
