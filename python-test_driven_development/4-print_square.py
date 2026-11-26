#!/usr/bin/python3
"""Module that defines print_square, which prints a square with #."""


def print_square(size):
    """Print a square of side size using the character #.

    Raises TypeError if size is not an integer,
    and ValueError if size is less than 0.
    """
    if not isinstance(size, int) or isinstance(size, bool):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
