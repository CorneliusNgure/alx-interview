#!/usr/bin/python3
from typing import List

"""
This module provides a function to rotate an n x n 2D matrix by 90 degrees
clockwise. The rotation is done in-place, meaning the input matrix is
modified directly without using extra space for another matrix.
"""


def rotate_2d_matrix(matrix: List[List[int]]) -> None:
    """
    Rotates a given n x n 2D matrix 90 degrees clockwise.

    The matrix is modified in-place and no value is returned.

    Steps:
    1. Transpose the matrix.
    2. Reverse each row of the transposed matrix.

    Args:
    matrix (List[List[int]]): A 2D list representing the matrix to be rotated.
    """
    n: int = len(matrix)

    # Step 1: Transpose the matrix (swap rows and columns)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()
