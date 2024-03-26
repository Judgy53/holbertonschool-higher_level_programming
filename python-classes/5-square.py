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

    def my_print(self):
        """Prints the square to stdout"""
        if self.__size == 0:
            print("")
            return

        line = "#" * self.__size
        for i in range(self.__size):
            print("{}".format(line))

    @property
    def size(self):
        """Property Getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Property Setter for size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value
