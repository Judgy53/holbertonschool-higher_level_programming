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
    def size(self, value):
        """Property Setter for size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def __lt__(self, other):
        """Returns True if instance area is smaller than other area"""
        return self.area() < other.area()

    def ___le___(self, other):
        """Returns True if instance area is smaller or equal than other area"""
        return self.area() <= other.area()

    def __eq__(self, other):
        """Returns True if instance area is equal to other area"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Returns True if instance area is not equal to other area"""
        return self.area() != other.area()

    def __ge__(self, other):
        """Returns True if instance area is bigger or equal than other area"""
        return self.area() >= other.area()

    def __gt__(self, other):
        """Returns True instance area is bigger than other area"""
        return self.area() > other.area()
