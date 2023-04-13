#!/usr/bin/python3
"""Defines a square"""


class Square:
    """Square class with size"""
    def __init__(self, size=0):
        """Initializes the data"""
        self.__size = size

    def area(self):
        """Returns the area of the Square"""
        return self.__size * self.__size

    @property
    def size(self):
        """Retrieves the size of a square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of a square"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
