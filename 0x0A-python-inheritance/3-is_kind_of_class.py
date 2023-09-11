#!/usr/bin/python3
"""Defines a function that checks if the object is inherited"""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance in a given class.

    Arguments:
        obj: the object to check
        a_class: the class to check against
    Returns:
        True if the object is an inherited instance from a class,
        otherwise returns False
    """
    if isinstance(obj, a_class):
        return True
    return False
