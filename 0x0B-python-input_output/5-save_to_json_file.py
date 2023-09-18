#!/usr/bin/python3
"""Defines a function that writes an object to text file"""
import json


def save_to_json_file(my_obj, flename):
    """ Function to save an object to a text file using json."""
    with open(filename, "w") as f:
        json.dumps(my_obj, f)
