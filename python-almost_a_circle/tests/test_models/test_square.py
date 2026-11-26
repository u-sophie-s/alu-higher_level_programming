#!/usr/bin/python3
"""Unittests for the Square class in models/square.py."""
import io
import unittest
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for the Square class."""

    def setUp(self):
        """Reset the object counter before each test."""
        Base._Base__nb_objects = 0

    def output(self, func):
        """Return what func prints to stdout."""
        buf = io.StringIO()
        with redirect_stdout(buf):
            func()
        return buf.getvalue()

    def test_is_rectangle(self):
        """Test Square inherits from Rectangle."""
        self.assertIsInstance(Square(1), Rectangle)

    def test_attributes(self):
        """Test the size, position and id."""
        s = Square(3, 1, 2, 4)
        self.assertEqual((s.size, s.width, s.height, s.x, s.y, s.id),
                         (3, 3, 3, 1, 2, 4))

    def test_auto_id(self):
        """Test ids are assigned automatically."""
        self.assertEqual(Square(1).id, 1)
        self.assertEqual(Square(1).id, 2)

    def test_str(self):
        """Test the string representation."""
        self.assertEqual(str(Square(5)), "[Square] (1) 0/0 - 5")
        self.assertEqual(str(Square(2, 2)), "[Square] (2) 2/0 - 2")
        self.assertEqual(str(Square(3, 1, 3)), "[Square] (3) 1/3 - 3")

    def test_area(self):
        """Test the area method."""
        self.assertEqual(Square(5).area(), 25)
        self.assertEqual(Square(3, 1, 3).area(), 9)

    def test_display(self):
        """Test display with and without offsets."""
        self.assertEqual(self.output(Square(2, 2).display),
                         "  ##\n  ##\n")
        self.assertEqual(self.output(Square(3, 1, 3).display),
                         "\n\n\n ###\n ###\n ###\n")

    def test_missing_size(self):
        """Test a missing size raises a TypeError."""
        with self.assertRaises(TypeError):
            Square()

    def test_validation(self):
        """Test the validation is inherited from Rectangle."""
        with self.assertRaises(TypeError) as cm:
            Square("1")
        self.assertEqual(str(cm.exception), "width must be an integer")
        with self.assertRaises(ValueError) as cm:
            Square(0)
        self.assertEqual(str(cm.exception), "width must be > 0")
        with self.assertRaises(TypeError) as cm:
            Square(1, "2")
        self.assertEqual(str(cm.exception), "x must be an integer")
        with self.assertRaises(ValueError) as cm:
            Square(1, 2, -3)
        self.assertEqual(str(cm.exception), "y must be >= 0")

    def test_size_setter(self):
        """Test the size setter updates width and height."""
        s = Square(5)
        s.size = 10
        self.assertEqual(str(s), "[Square] (1) 0/0 - 10")
        self.assertEqual((s.width, s.height), (10, 10))

    def test_size_setter_validation(self):
        """Test the size setter uses the width error messages."""
        s = Square(5)
        with self.assertRaises(TypeError) as cm:
            s.size = "9"
        self.assertEqual(str(cm.exception), "width must be an integer")
        with self.assertRaises(ValueError) as cm:
            s.size = -1
        self.assertEqual(str(cm.exception), "width must be > 0")

    def test_update_args(self):
        """Test update with positional arguments."""
        s = Square(5)
        s.update(10)
        self.assertEqual(str(s), "[Square] (10) 0/0 - 5")
        s.update(1, 2)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 2")
        s.update(1, 2, 3)
        self.assertEqual(str(s), "[Square] (1) 3/0 - 2")
        s.update(1, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (1) 3/4 - 2")

    def test_update_kwargs(self):
        """Test update with keyword arguments."""
        s = Square(2, 3, 4, 1)
        s.update(x=12)
        self.assertEqual(str(s), "[Square] (1) 12/4 - 2")
        s.update(size=7, y=1)
        self.assertEqual(str(s), "[Square] (1) 12/1 - 7")
        s.update(size=7, id=89, y=1)
        self.assertEqual(str(s), "[Square] (89) 12/1 - 7")

    def test_update_args_skip_kwargs(self):
        """Test kwargs are ignored when args are given."""
        s = Square(5)
        s.update(10, size=3)
        self.assertEqual(str(s), "[Square] (10) 0/0 - 5")

    def test_to_dictionary(self):
        """Test the dictionary representation."""
        s = Square(10, 2, 1)
        self.assertEqual(s.to_dictionary(),
                         {"id": 1, "x": 2, "size": 10, "y": 1})

    def test_to_dictionary_update(self):
        """Test a dictionary can update another square."""
        s1 = Square(10, 2, 1)
        s2 = Square(1, 1)
        s2.update(**s1.to_dictionary())
        self.assertEqual(str(s2), "[Square] (1) 2/1 - 10")
        self.assertNotEqual(s1, s2)


if __name__ == "__main__":
    unittest.main()
