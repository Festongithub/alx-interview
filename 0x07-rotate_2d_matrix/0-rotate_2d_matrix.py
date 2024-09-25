#!/usr/bin/python3

"""perform matrix rotation"""


def transpose(matrix, n):
    """matrix transpose"""
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def reverse_matrix(matrix):
    """
    perform matrix reversal
    """
    for i in matrix:
        i.reverse()


def rotate_2d_matrix(matrix):
    """
    rotate matrix
    n x n
    """
    n = len(matrix)
    transpose(matrix, n)
    reverse_matrix(matrix)
    return matrix
