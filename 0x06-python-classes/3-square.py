#!/usr/bin/python3
"""Defines a square"""


class Square:
    """Square class with size"""
    def __init__(self, size=0):
        """Initializes the data"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the area of the Square"""
        return self.__size * self.__size
