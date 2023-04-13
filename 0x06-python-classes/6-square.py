#!/usr/bin/python3
"""Defines a Square"""


class Square:
    """Square class with size"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the data"""
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Retrieves the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the Square"""
        if type(value) is not tuple or len(value) != 2 or type(value[0] is not int or value[0] < 0 or type(value[1]) is not int orvalue[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Prints the Square"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            sqr = "#" * self.__size
            pos = " " * self.__position[0]
            for i in range(self.__size):
                print(pos, sqr, sep="")
