#!/usr/bin/python3
"""This module contains one function, matrix_mul(m_a, m_b). Example:
    >>> matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]])
    [[7, 10], [15, 22]]
"""


def matrix_mul(m_a, m_b):
    """Returns the product of 2 matrices
    m_a and m_b must be list of lists
    m_a and m_b must only contain integers or floats"""

    assert_matrix_valid(m_a, "m_a")
    assert_matrix_valid(m_b, "m_b")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    output = []
    m = len(m_a)
    p = len(m_b[0])
    n = len(m_b)
    for i in range(m):
        row = []
        for j in range(p):
            sum = 0
            for k in range(n):
                sum += m_a[i][k] * m_b[k][j]
            row.append(sum)
        output.append(row)

    return output


def assert_matrix_valid(matrix, name):
    if not isinstance(matrix, list):
        raise TypeError(f"{name} must be a list")

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(f"{name} must be a list of lists")

    if len(matrix) == 0 or any(len(row) == 0 for row in matrix):
        raise ValueError(f"{name} can't be empty")

    if any(not isinstance(elem, (int, float))
            for row in matrix for elem in row):
        raise TypeError(f"{name} should contain only integers or floats")

    row_length = len(matrix[0])
    if any(len(row) != row_length for row in matrix):
        raise TypeError(f"each row of {name} must be of the same size")
