#!/usr/bin/python3
"""Module that defines matrix_divided, which divides all matrix elements."""


def matrix_divided(matrix, div):
    """Return a new matrix with every element divided by div.

    Results are rounded to 2 decimal places.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg)
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(msg)
        for el in row:
            if type(el) not in (int, float):
                raise TypeError(msg)
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(el / div, 2) for el in row] for row in matrix]
