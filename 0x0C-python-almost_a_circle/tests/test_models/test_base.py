#!/usr/bin/python3
""" Unittest for Base Class """


import unittest
from models import base
Base = base.Base

class TestBase(unittest.TestCase):
    """ Unittest for Base Class """
    def _set_id(self):
        b = Base(74)
        self.assertEqual(b.id, 74)
