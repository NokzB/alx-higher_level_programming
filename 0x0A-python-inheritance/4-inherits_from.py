#!/usr/bin/python3
"""Defines a function to check if an instance has been inherited"""


def inherits_from(obj, a_class):
    """Checks if the object is an instance that inherits from another class

    Arguments:
        obj: the object to check
        a_class: the class to check against
    Returns:
        True if the object is an inherited instance of a class
        otherwise returns False
    """
    if issubclass(obj, a_class) and obj != a_class:
        return True
    return False
