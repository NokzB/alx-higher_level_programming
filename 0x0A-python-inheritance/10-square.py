#!/usr/bin/python3
"""Defines a Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square subclass of Rectangle"""
    def __init__(self, size):
        """Initializes a square

        Arguments:
            Size (int): the size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
