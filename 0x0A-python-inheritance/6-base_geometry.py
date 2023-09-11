#!/usr/bin/python3
"""Defines an Base Geometry Class"""


class BaseGeometry():
    """A Base Geometry Class"""
    def area(self):
        """Function that raises an exception when area() is not implemented"""
        raise Exception("area() is not implemented")
