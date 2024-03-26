#!/usr/bin/python3
"""Defines a Square class"""


class Square():
    """Represents a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square size and position"""
        self.size = size
        self.position = position

    def area(self):
        """Returns the area of the square instance"""
        return self.size * self.size

    def my_print(self):
        """Prints the square to stdout"""
        if self.size == 0:
            print("")
            return

        for _ in range(self.position[1]):
            print("")

        line = " " * self.position[0] + "#" * self.size
        for _ in range(self.size):
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

    @property
    def position(self):
        """Property Getter for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Property Setter for position"""
        if (not isinstance(value, tuple)
                or len(value) != 2
                or any(not isinstance(x, int) or x < 0 for x in value)):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value
