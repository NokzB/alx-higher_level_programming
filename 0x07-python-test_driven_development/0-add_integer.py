#!/usr/bin/python3
"""Defines and integer function that adds two integers"""


def add_integer(a, b=98):
    """Returns the sum of two integers

    Floating point arguments are typecasted into
    integers before addition is performed

    Raises a TypeError if either argument is neither a float nor a int
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
