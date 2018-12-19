import unittest

from scribe.coordinates import Coordinates


class TestCoordinates(unittest.TestCase):
    def test_initialization(self):
        c = Coordinates(0.5, 0.7)
        self.assertEqual(c.x, 0.5)
        self.assertEqual(c.y, 0.7)

    def test_invalid_coordinates_y_too_big(self):
        with self.assertRaises(Exception):
            Coordinates(0.5, 15)

    def test_invalid_coordinates_x_too_big(self):
        with self.assertRaises(Exception):
            Coordinates(15, 0.5)

    def test_invalid_coordinates_y_too_small(self):
        with self.assertRaises(Exception):
            Coordinates(0.5, -0.5)

    def test_invalid_coordinates_x_too_small(self):
        with self.assertRaises(Exception):
            Coordinates(-0.5, 0.5)
