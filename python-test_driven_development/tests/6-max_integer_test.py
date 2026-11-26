#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_ordered_list(self):
        """Test a list sorted in ascending order."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test an unordered list."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test a list with the max at the beginning."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_empty_list(self):
        """Test an empty list returns None."""
        self.assertIsNone(max_integer([]))

    def test_no_argument(self):
        """Test calling with no argument returns None."""
        self.assertIsNone(max_integer())

    def test_one_element(self):
        """Test a list with one element."""
        self.assertEqual(max_integer([7]), 7)

    def test_negative_numbers(self):
        """Test a list of negative numbers."""
        self.assertEqual(max_integer([-5, -2, -9]), -2)

    def test_mixed_numbers(self):
        """Test a list of positive and negative numbers."""
        self.assertEqual(max_integer([-1, 0, 5, -10]), 5)

    def test_duplicates(self):
        """Test a list with duplicate max values."""
        self.assertEqual(max_integer([3, 3, 3]), 3)

    def test_floats(self):
        """Test a list of floats."""
        self.assertEqual(max_integer([1.5, 2.7, 0.3]), 2.7)

    def test_ints_and_floats(self):
        """Test a list of integers and floats."""
        self.assertEqual(max_integer([1, 2.5, 2]), 2.5)

    def test_string(self):
        """Test a string returns its largest character."""
        self.assertEqual(max_integer("Holberton"), "t")

    def test_list_of_strings(self):
        """Test a list of strings."""
        self.assertEqual(max_integer(["a", "c", "b"]), "c")

    def test_none(self):
        """Test None raises a TypeError."""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_mixed_types(self):
        """Test a list mixing numbers and strings raises a TypeError."""
        with self.assertRaises(TypeError):
            max_integer([1, "2", 3])


if __name__ == "__main__":
    unittest.main()
