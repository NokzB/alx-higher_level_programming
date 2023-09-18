#!/usr/bin/python3
"""Defines a class to json function"""


def class_to_json(obj):
    """Function that returns a dictionary description of a data structure"""
    return obj.__dict__
