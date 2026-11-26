#!/usr/bin/python3
"""Module that defines add_integer, a function that adds two integers.

Floats are cast to integers before the addition.
"""


def add_integer(a, b=98):
    """Return the integer sum of a and b.

    Raises TypeError if a or b is not an integer or a float.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
