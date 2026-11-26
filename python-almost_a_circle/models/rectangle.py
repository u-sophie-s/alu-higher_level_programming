#!/usr/bin/python3
"""Module that defines the Rectangle class, which inherits from Base."""
from models.base import Base


class Rectangle(Base):
    """A rectangle with a width, a height and an (x, y) position."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle with validated attributes."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @staticmethod
    def __validate(name, value, positive):
        """Validate that value is an integer, > 0 or >= 0."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if positive and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        if not positive and value < 0:
            raise ValueError("{} must be >= 0".format(name))

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        self.__validate("width", value, True)
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        self.__validate("height", value, True)
        self.__height = value

    @property
    def x(self):
        """Get the x position of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x position of the rectangle."""
        self.__validate("x", value, False)
        self.__x = value

    @property
    def y(self):
        """Get the y position of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y position of the rectangle."""
        self.__validate("y", value, False)
        self.__y = value

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Print the rectangle with the character #, taking care of x and y."""
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Return the string representation of the rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Assign attributes from *args in order, or else from **kwargs."""
        attrs = ("id", "width", "height", "x", "y")
        if args:
            for name, value in zip(attrs, args):
                setattr(self, name, value)
        else:
            for name, value in kwargs.items():
                if name in attrs:
                    setattr(self, name, value)

    def to_dictionary(self):
        """Return the dictionary representation of the rectangle."""
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
