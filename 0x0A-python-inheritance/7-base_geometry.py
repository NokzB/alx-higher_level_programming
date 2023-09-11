#!/usr/bin/python3
"""Defines an Base Geometry Class"""


class BaseGeometry():
    """A Base Geometry Class"""
    def area(self):
        """Function that raises an exception when area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Function to validate a value

        Arguments:
            name (str): a string
            value (int): the value to validate
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than or equal to 0
        """
        if type(value) != int:
            raise TypeError("<name> must be an integer".format(name))
        if value <= 0:
            raise ValueError("<name> must be greater than 0".format(name))
