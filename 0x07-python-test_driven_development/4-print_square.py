#!/usr/bin/python3
"""Defines a function that prints a square"""


def print_square(size):
    """Prints a square with the # character
    Arguments:
        size: the length of the square
    Raises:
        TypeError: ifsize is not an integer
        ValueError: if size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
