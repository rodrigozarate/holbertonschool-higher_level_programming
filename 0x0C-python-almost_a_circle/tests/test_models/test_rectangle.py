#!/usr/bin/python3
""" Test set for rectangle Class """
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ Test cases for class rectangle """
    def test_id_default(self):
        r = Rectangle(7, 4)
        self.assertEqual(r.id, 1)

    def test_width_height(self):
        r_cero = Rectangle(7, 4)
        self.assertEqual(r_cero.width, 7)
        self.assertEqual(r_cero.height, 4)

    def test_x_y_default(self):
        r_one = Rectangle(7, 4)
        self.assertEqual(r_one.x, 0)
        self.assertEqual(r_one.y, 0)

    def test_value_error_width(self):
        with self.assertRaises(ValueError):
            r_negative_w = Rectangle(-7, 4)
        
    def test_value_error_height(self):
        with self.assertRaises(ValueError):
            r_negative_h = Rectangle(7, -4)

    def test_type_error_string_width(self):
        with self.assertRaises(TypeError):
            r_string = Rectangle("seven", 4)

    def test_type_error_string_heigth(self):
        with self.assertRaises(TypeError):
            r_string = Rectangle(7, "four")

    def test_area_success(self):
        r_area = Rectangle(7, 4, 0, 0, 28)
        self.assertEqual(r_area.area(), 28)

    def test_area_fail(self):
        r_area = Rectangle(7, 7, 0, 0, 28)
        self.assertNotEqual(r_area.area(), 28)
