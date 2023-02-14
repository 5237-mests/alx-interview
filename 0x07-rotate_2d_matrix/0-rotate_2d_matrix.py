#!/usr/bin/env python3
"""Module for task0"""


def rotate_2d_matrix(matrix):
    """rotate matrix """
    if type(matrix) != list:
        return
    if len(matrix) <= 0:
        return
    if not all(map(lambda x: type(x) == list, matrix)):
        return
    rows = len(matrix)
    column = len(matrix[0])
    if not all(map(lambda x: len(x) == column, matrix)):
        return

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
