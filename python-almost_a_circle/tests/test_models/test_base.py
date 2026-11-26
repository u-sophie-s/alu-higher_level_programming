#!/usr/bin/python3
"""Unittests for the Base class in models/base.py."""
import json
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test cases for the Base class."""

    def setUp(self):
        """Reset the object counter before each test."""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Remove the JSON files created by the tests."""
        for name in ("Base.json", "Rectangle.json", "Square.json"):
            if os.path.exists(name):
                os.remove(name)

    def test_auto_id(self):
        """Test ids are assigned automatically in order."""
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)

    def test_given_id(self):
        """Test a given id is used and does not change the counter."""
        self.assertEqual(Base(12).id, 12)
        self.assertEqual(Base().id, 1)

    def test_mixed_ids(self):
        """Test the example sequence of ids."""
        ids = [Base().id, Base().id, Base().id, Base(12).id, Base().id]
        self.assertEqual(ids, [1, 2, 3, 12, 4])

    def test_id_other_types(self):
        """Test id accepts any value without type checking."""
        self.assertEqual(Base("hello").id, "hello")
        self.assertEqual(Base(-5).id, -5)

    def test_nb_objects_private(self):
        """Test the counter is a private class attribute."""
        with self.assertRaises(AttributeError):
            Base.__nb_objects

    def test_too_many_args(self):
        """Test passing two arguments raises a TypeError."""
        with self.assertRaises(TypeError):
            Base(1, 2)

    def test_to_json_string(self):
        """Test to_json_string with a list of dictionaries."""
        d = {"id": 1, "width": 10}
        self.assertEqual(Base.to_json_string([d]), json.dumps([d]))
        self.assertIsInstance(Base.to_json_string([d]), str)

    def test_to_json_string_none_empty(self):
        """Test to_json_string with None or an empty list."""
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_from_json_string(self):
        """Test from_json_string returns the matching list."""
        data = [{"id": 89, "width": 10}, {"id": 7}]
        self.assertEqual(Base.from_json_string(json.dumps(data)), data)

    def test_from_json_string_none_empty(self):
        """Test from_json_string with None or an empty string."""
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_save_to_file_rectangle(self):
        """Test save_to_file writes rectangles to Rectangle.json."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json") as f:
            self.assertEqual(json.loads(f.read()),
                             [r1.to_dictionary(), r2.to_dictionary()])

    def test_save_to_file_square(self):
        """Test save_to_file writes squares to Square.json."""
        s = Square(5, 1, 2, 3)
        Square.save_to_file([s])
        with open("Square.json") as f:
            self.assertEqual(json.loads(f.read()), [s.to_dictionary()])

    def test_save_to_file_none_empty(self):
        """Test save_to_file with None or an empty list saves []."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json") as f:
            self.assertEqual(f.read(), "[]")
        Square.save_to_file([])
        with open("Square.json") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_overwrites(self):
        """Test save_to_file overwrites an existing file."""
        Rectangle.save_to_file([Rectangle(1, 2), Rectangle(3, 4)])
        Rectangle.save_to_file([Rectangle(5, 6)])
        with open("Rectangle.json") as f:
            self.assertEqual(len(json.loads(f.read())), 1)

    def test_create_rectangle(self):
        """Test create returns a new equal Rectangle."""
        r1 = Rectangle(3, 5, 1)
        r2 = Rectangle.create(**r1.to_dictionary())
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)

    def test_create_square(self):
        """Test create returns a new equal Square."""
        s1 = Square(3, 1, 2)
        s2 = Square.create(**s1.to_dictionary())
        self.assertEqual(str(s1), str(s2))
        self.assertIsNot(s1, s2)

    def test_load_from_file_rectangle(self):
        """Test load_from_file returns the saved rectangles."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        out = Rectangle.load_from_file()
        self.assertEqual([str(r) for r in out], [str(r1), str(r2)])
        self.assertTrue(all(type(r) is Rectangle for r in out))

    def test_load_from_file_square(self):
        """Test load_from_file returns the saved squares."""
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        Square.save_to_file([s1, s2])
        out = Square.load_from_file()
        self.assertEqual([str(s) for s in out], [str(s1), str(s2)])
        self.assertTrue(all(type(s) is Square for s in out))

    def test_load_from_file_missing(self):
        """Test load_from_file returns [] when the file doesn't exist."""
        self.assertEqual(Rectangle.load_from_file(), [])
        self.assertEqual(Square.load_from_file(), [])


if __name__ == "__main__":
    unittest.main()
