#!/usr/bin/python3
"""Defines a Student class."""


class Student:
    """Class representing a student."""
    def __init__(self, first_name, last_name, age):
        """Initializes a student.

        Arguments:
            First_name (str): the first name of the student.
            Last_name (str): the last name of the student.
            Age (int): the age of the student.
            """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Function to return dictionary representation
        If attrs is a list of strings, returns only those attributes
        included in the list
        Arguments:
            attrs (list): (Optional) the attributes to represent
        """
        if (type(attrs) == list and
                all(type(element) == str for element in attrs)):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__

    def reload_from_json(self, json):
        """Function that replaces all attributes of the Student

        Arguments:
            json (dict): the key/value pairs to replace the atttributes with"""
        for k, val in json.items():
            setattr(self, k, val)
