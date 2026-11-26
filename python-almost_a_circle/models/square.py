#!/usr/bin/python3
"""Module that defines the Square class, which inherits from Rectangle."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A square, which is a rectangle with the same width and height."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square with a validated size and position."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square (width and height)."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return the string representation of the square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Assign attributes from *args in order, or else from **kwargs."""
        attrs = ("id", "size", "x", "y")
        if args:
            for name, value in zip(attrs, args):
                setattr(self, name, value)
        else:
            for name, value in kwargs.items():
                if name in attrs:
                    setattr(self, name, value)

    def to_dictionary(self):
        """Return the dictionary representation of the square."""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
