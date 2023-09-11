#!/usr/bin/python3
"""Defines a Rectangle class that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initializes a new rectangle

        Arguements:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """returns the str() and print() representation of a rectangle"""
        rec_string = "[" + str(self.__class__.__name__) + "] "
        rec_string += str(self.__width) + "/" + str(self.__height)
        return rec_string
