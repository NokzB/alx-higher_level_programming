#!/usr/bin/python3
"""Defines a function that returns the JSON representation of an obejct"""


def to_json_string(my_obj):
    """Function that returns the JSON representation of an object

    Arguments:
        My_obj: The object to serialize
    """
    return json.dump(my_obj)
