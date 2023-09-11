#!/usr/bin/python3
"""Defines a function that checks the type of object"""


def is_same_class(obj, a_class):
    """Checks if an object is an instance in a given class.

    Arguments:
        obj: the object to check
        a_class: the class to match the object type to
    Returns:
        True if the object is exactly an instance
        otherwise returns False
    """
    if type(obj) == a_class:
        return True
    return False
