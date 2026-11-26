#!/usr/bin/python3
"""Unittests for the Rectangle class in models/rectangle.py."""
import io
import unittest
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    def setUp(self):
        """Reset the object counter before each test."""
        Base._Base__nb_objects = 0

    def output(self, func):
        """Return what func prints to stdout."""
        buf = io.StringIO()
        with redirect_stdout(buf):
            func()
        return buf.getvalue()

    def test_is_base(self):
        """Test Rectangle inherits from Base."""
        self.assertIsInstance(Rectangle(1, 2), Base)

    def test_ids(self):
        """Test automatic and given ids."""
        self.assertEqual(Rectangle(10, 2).id, 1)
        self.assertEqual(Rectangle(2, 10).id, 2)
        self.assertEqual(Rectangle(10, 2, 0, 0, 12).id, 12)

    def test_attributes(self):
        """Test the getters return the given values."""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual((r.width, r.height, r.x, r.y, r.id),
                         (1, 2, 3, 4, 5))

    def test_defaults(self):
        """Test x and y default to 0."""
        r = Rectangle(1, 2)
        self.assertEqual((r.x, r.y), (0, 0))

    def test_private_attributes(self):
        """Test the attributes are private."""
        r = Rectangle(1, 2)
        with self.assertRaises(AttributeError):
            r.__width
        with self.assertRaises(AttributeError):
            r.__height

    def test_setters(self):
        """Test the setters change the values."""
        r = Rectangle(1, 2)
        r.width, r.height, r.x, r.y = 10, 20, 30, 40
        self.assertEqual((r.width, r.height, r.x, r.y), (10, 20, 30, 40))

    def test_missing_args(self):
        """Test missing width or height raises a TypeError."""
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_type_errors(self):
        """Test non-integer values raise a TypeError."""
        cases = [((1.5, 2), "width"), (("1", 2), "width"),
                 ((1, "2"), "height"), ((1, None), "height"),
                 ((1, 2, [3]), "x"), ((1, 2, 3.0), "x"),
                 ((1, 2, 3, {}), "y"), ((1, 2, 3, True), "y")]
        for args, name in cases:
            with self.assertRaises(TypeError) as cm:
                Rectangle(*args)
            self.assertEqual(str(cm.exception),
                             "{} must be an integer".format(name))

    def test_value_errors(self):
        """Test out-of-range values raise a ValueError."""
        cases = [((0, 2), "width must be > 0"),
                 ((-1, 2), "width must be > 0"),
                 ((1, 0), "height must be > 0"),
                 ((1, -2), "height must be > 0"),
                 ((1, 2, -1), "x must be >= 0"),
                 ((1, 2, 3, -1), "y must be >= 0")]
        for args, msg in cases:
            with self.assertRaises(ValueError) as cm:
                Rectangle(*args)
            self.assertEqual(str(cm.exception), msg)

    def test_setter_validation(self):
        """Test the setters also validate values."""
        r = Rectangle(10, 2)
        with self.assertRaises(ValueError):
            r.width = -10
        with self.assertRaises(TypeError):
            r.x = {}
        with self.assertRaises(TypeError):
            r.height = "2"
        with self.assertRaises(ValueError):
            r.y = -1

    def test_validation_order(self):
        """Test width is validated before height."""
        with self.assertRaises(TypeError) as cm:
            Rectangle("1", "2")
        self.assertEqual(str(cm.exception), "width must be an integer")

    def test_x_y_zero(self):
        """Test x and y can be 0."""
        r = Rectangle(1, 1, 0, 0)
        self.assertEqual((r.x, r.y), (0, 0))

    def test_area(self):
        """Test the area method."""
        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(2, 10).area(), 20)
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)

    def test_display(self):
        """Test display without x and y."""
        self.assertEqual(self.output(Rectangle(4, 6).display),
                         "####\n" * 6)
        self.assertEqual(self.output(Rectangle(2, 2).display), "##\n##\n")

    def test_display_x_y(self):
        """Test display with x and y offsets."""
        self.assertEqual(self.output(Rectangle(2, 3, 2, 2).display),
                         "\n\n  ##\n  ##\n  ##\n")
        self.assertEqual(self.output(Rectangle(3, 2, 1, 0).display),
                         " ###\n ###\n")

    def test_str(self):
        """Test the string representation."""
        self.assertEqual(str(Rectangle(4, 6, 2, 1, 12)),
                         "[Rectangle] (12) 2/1 - 4/6")
        self.assertEqual(str(Rectangle(5, 5, 1)),
                         "[Rectangle] (1) 1/0 - 5/5")

    def test_update_args(self):
        """Test update with positional arguments."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 10/10")
        r.update(89, 2)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/10")
        r.update(89, 2, 3)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/3")
        r.update(89, 2, 3, 4)
        self.assertEqual(str(r), "[Rectangle] (89) 4/10 - 2/3")
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_kwargs(self):
        """Test update with keyword arguments."""
        r = Rectangle(10, 10, 10, 10)
        r.update(height=1)
        self.assertEqual(str(r), "[Rectangle] (1) 10/10 - 10/1")
        r.update(width=1, x=2)
        self.assertEqual(str(r), "[Rectangle] (1) 2/10 - 1/1")
        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r), "[Rectangle] (89) 3/1 - 2/1")
        r.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r), "[Rectangle] (89) 1/3 - 4/2")

    def test_update_args_skip_kwargs(self):
        """Test kwargs are ignored when args are given."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, width=5)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 10/10")

    def test_update_no_args(self):
        """Test update with no arguments changes nothing."""
        r = Rectangle(10, 10, 10, 10)
        r.update()
        self.assertEqual(str(r), "[Rectangle] (1) 10/10 - 10/10")

    def test_update_validation(self):
        """Test update validates the values."""
        r = Rectangle(10, 10)
        with self.assertRaises(TypeError):
            r.update(1, "2")
        with self.assertRaises(ValueError):
            r.update(width=-1)

    def test_to_dictionary(self):
        """Test the dictionary representation."""
        r = Rectangle(10, 2, 1, 9)
        self.assertEqual(r.to_dictionary(),
                         {"x": 1, "y": 9, "id": 1, "height": 2, "width": 10})

    def test_to_dictionary_update(self):
        """Test a dictionary can update another rectangle."""
        r1 = Rectangle(10, 2, 1, 9)
        r2 = Rectangle(1, 1)
        r2.update(**r1.to_dictionary())
        self.assertEqual(str(r2), "[Rectangle] (1) 1/9 - 10/2")
        self.assertNotEqual(r1, r2)


if __name__ == "__main__":
    unittest.main()
