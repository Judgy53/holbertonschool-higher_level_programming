#!/usr/bin/python3
"""
This module provides one function, matrix_divided(matrix, div). Example:
    >>> matrix_divided([[1, 2, 3], [4, 5, 6]], 3)
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
"""


def matrix_divided(matrix, div):
    """Divides all elements of the matrix by div. Returns a new matrix.
    Matrix must be a list of lists of integers or floats.
    Each row of the matrix must be of the same size.
    Div must be a non 0 number (integer or float)."""

    if (not isinstance(matrix, list)
            or any(not isinstance(row, list) for row in matrix)
            or not all(isinstance(elem, (int, float))
                       for row in matrix for elem in row)):
        raise TypeError("""matrix must be a matrix
                             (list of lists) of integers/floats""")

    if len(matrix) == 0:
        return []

    row_length = len(matrix[0])
    if any(len(row) != row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    output = []
    for orig_row in matrix:
        out_row = []
        for orig_elem in orig_row:
            out_row.append(round(orig_elem / div, 2))
        output.append(out_row)

    return output
