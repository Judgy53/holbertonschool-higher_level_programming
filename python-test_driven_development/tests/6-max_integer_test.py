#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Defines all tests for max_integer([...])"""

    def test_empty_list(self):
        """Test for passing an empty list
        Expected Result: None"""

        self.assertEqual(max_integer([]), None)

    def test_valid_full_list(self):
        """Test for passing a list with many valid elements
        Expected Result: 9"""

        self.assertEqual(max_integer([8, 1, 6, 9]), 9)

    def test_single_element(self):
        """Test for passing a list with 1 element
        Expected Result: 3"""

        self.assertEqual(max_integer([3]), 3)

    def test_negative_list(self):
        """Test for passing a list with only negative elements
        Expected Result: -2"""

        self.assertEqual(max_integer([-2, -3, -4, -5, -6]), -2)

    def test_no_argument(self):
        """Test for passing nothing
        Expected Result: None"""

        self.assertEqual(max_integer(), None)

    def test_string(self):
        """Test for passing a string
        Expected Result: w"""

        self.assertEqual(max_integer("ankifbw"), "w")

    def test_int(self):
        """Test for passing an integer
        Expected Result: TypeError"""

        with self.assertRaises(TypeError):
            max_integer(42)
