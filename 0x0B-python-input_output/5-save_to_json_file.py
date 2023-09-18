#!/usr/bin/python3
"""Defines a function that writes an object to text file"""
import json


def save_to_json_file(my_obj, flename):
    """ Function to save an object to a text file using json

    Arguments:
        my_obj: object serialize and to save to file.
        filename: the file to save to.
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
