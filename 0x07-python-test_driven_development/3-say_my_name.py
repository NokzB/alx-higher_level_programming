#!/usr/bin/python3
"""Defines a function that prints the first and last name"""


def say_my_name(first_name, last_name=""):
    """Prints a string
    Arguments:
        first_name: the first name to print
        last_name: the last name to print
    Raises:
        TypeError: if first_name and last_name are not strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
