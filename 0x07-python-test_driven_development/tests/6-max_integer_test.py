#!/usr/bin/python3
"""
max_integer([..]). Unittest
"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ Unittest cases fir max_integer function """

    def test_empty_list(self):
        list = []
        self.assertEqual(max_integer(list), None)
