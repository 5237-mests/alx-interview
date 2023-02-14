#!/usr/bin/env python3
"""Module for task0"""


def rotate_2d_matrix(matrix):
    """rotate matrix """
    deepcopied_matrix = matrix.copy()
    for k in range(len(deepcopied_matrix)):
        deepcopied_matrix[k] = deepcopied_matrix[k].copy()

    new_matrix = matrix
    y = len(deepcopied_matrix)
    for i in range(len(deepcopied_matrix)):
        y = y - 1
        x = 0
        for j in deepcopied_matrix[i]:
            new_matrix[x][y] = j
            x = x + 1
