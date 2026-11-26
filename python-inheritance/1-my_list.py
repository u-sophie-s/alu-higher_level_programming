#!/usr/bin/python3
"""Module that defines the MyList class, a subclass of list."""


class MyList(list):
    """A list subclass that can print itself in sorted order."""

    def print_sorted(self):
        """Print the list sorted in ascending order."""
        print(sorted(self))
