#!/usr/bin/python3
"""Defines a function that returns a list of attributes and methods"""


def lookup(obj):
    """Returns a list of available attributes and methods of an object"""
    return (dir(obj))
