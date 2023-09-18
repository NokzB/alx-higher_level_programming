#!/usr/bin/python3
"""Defines a function that appends text to a file."""


def append_write(filename="", text=""):
    """A function to append text to a UTF8 file.

    Arguments:
        Filename: the name of the file to append text to.
        Text: the text to append.

    Returns:
        The number of characters written to the file.
        """
    with open(filename, "a+", encoding="utf-8") as f:
        return f.write(text)
