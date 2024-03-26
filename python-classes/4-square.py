#!/usr/bin/python3
"""Defines a Square class"""


class Square():
    """Represents a square with a fixed size"""

    def __init__(self, size=0):
        """Initializes the square size"""
        self.size = size

    def area(self):
        """Returns the area of the square instance"""
        return self.__size * self.__size

    @property
    def size(self):
        """Property Getter for size"""
        return self.__size

    @size.setter
    def size(self, size):
        """Property Setter for size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
