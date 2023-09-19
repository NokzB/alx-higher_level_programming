#!/usr/bin/python3
"""Defines a function to return a list representation of pascal's triangle"""


def pascal_triangle(n):
    """function that represents Pascal's triangle.

    Return:
        A list of lists representing a triangle
    """
    if n <= 0:
        return []

    triangle = [[1]]
    row = 0

    while n > len(triangle):
        row = row + 1
        triangle.append([1] * (row + 1))
        for i in range(1, row):
            triangle[row][i] = triangle[row - 1][i - 1] + triangle[row - 1][i]
    return triangle
