#!/usr/bin/python3
"""This module defines a Square class with position properties."""


class Square:
    """Represent a square with a customizable position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square with a size and position."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size after validating its value."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the current position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position after validating its values."""
        if type(value) is not tuple or len(value) != 2:
            raise TypeError(
                "position must be a tuple of 2 positive integers"
            )
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError(
                "position must be a tuple of 2 positive integers"
            )
        if value[0] < 0 or value[1] < 0:
            raise TypeError(
                "position must be a tuple of 2 positive integers"
            )
        self.__position = value

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square at its specified position."""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[0]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[1] + "#" * self.__size)
