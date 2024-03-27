#!/usr/bin/python3
"""This module contains one function, lazy_matrix_mul(m_a, m_b). Example:
    >>> matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]])
    [[7 10]
     [15, 22]]
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Returns the product of 2 matrices using numpy"""

    return np.matmul(m_a, m_b)
