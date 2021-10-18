#!/usr/bin/python3
""" Test set for Square Class """
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """ Test cases for class Squaree """
    def test_id_default(self):
        s = Square(7, 4)
        self.assertEqual(s.id, 6)

    def test_size(self):
        s_size = Square(7)
        self.assertEqual(s_size.size, 7)

    def test_width_height_x(self):
        s_cero = Square(7, 4)
        self.assertEqual(s_cero.size, 7)
        self.assertEqual(s_cero.x, 4)

    def test_x_y_default(self):
        s_one = Square(28, 7, 4)
        self.assertEqual(s_one.x, 7)
        self.assertEqual(s_one.y, 4)

    def test_value_error_size(self):
        with self.assertRaises(ValueError):
            s_negative = Square(-7)
        
    def test_value_error_x(self):
        with self.assertRaises(ValueError):
            s_negative_x = Square(7, -4)

    def test_type_error_string_size(self):
        with self.assertRaises(TypeError):
            s_string = Square("seven")

    def test_type_error_string_x(self):
        with self.assertRaises(TypeError):
            s_string = Square(7, "four")

    def test_type_error_list(self):
        with self.assertRaises(TypeError):
            s_list = Square([7, 4], 2, 8)

    def test_area_success(self):
        s_area = Square(7, 0, 0)
        self.assertEqual(s_area.area(), 49)

    def test_area_fail(self):
        s_area = Square(7, 0, 0)
        self.assertNotEqual(s_area.area(), 28)
