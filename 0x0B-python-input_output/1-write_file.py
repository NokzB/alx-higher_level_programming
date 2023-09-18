#!/usr/bin/python3
"""Defines a function to write  a string into a text file."""


def write_file(filename="", text=""):
    """function to write a string to a UTF-8 text file.

    Arguments:
        Filename: the name of the fileto write to.
        Text: the text to write to the file.

    Returns:
        The number of characters written to the file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
