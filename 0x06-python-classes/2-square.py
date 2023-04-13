#!/usr/bin/python3
"""Defines a square"""


class Square:
    """A square class with size"""
    def __init__(self, size=0):
        """Initializes the data"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if type(size) < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
