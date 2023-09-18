#!/usr/bin/python3
"""Defines an Object-JSON string function"""
import json


def from_json_string(my_str):
    """Function to return the object representation of a json string"""
    return json.loads(my_str)
