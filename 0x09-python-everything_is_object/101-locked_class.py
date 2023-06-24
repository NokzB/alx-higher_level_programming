#!/usr/bin/python3
"""Defines a locked class new instance attributes"""


class LockedClass:
    """A class that prevents the user from
    creating new instance attributes except for first_name
    """

    __slots__ = ["first_name"]
