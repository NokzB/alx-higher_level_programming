#!/usr/bin/python3
"""Defines a function that reads the contents of a file."""


def read_file(filename=""):
    """ Prints the contents of a text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
