#!/usr/bin/python3
"""Module that defines a Student class with filtered JSON output."""


class Student:
    """A student defined by first name, last name and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a student with first name, last name and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the dictionary representation of the student.

        If attrs is a list of strings, only those attributes are returned.
        """
        if (isinstance(attrs, list) and
                all(isinstance(a, str) for a in attrs)):
            return {a: self.__dict__[a] for a in attrs if a in self.__dict__}
        return self.__dict__
