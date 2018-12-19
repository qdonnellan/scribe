import unittest

from scribe.pixel_painter import get_pixel, generate_pixel_array, paint_pixel
from scribe.coordinates import Coordinates


class TestPixelPainter(unittest.TestCase):
    def test_get_top_left_pixel(self):
        topLeftPoint = Coordinates(0, 0)
        result = get_pixel(topLeftPoint, (10, 10))
        self.assertEqual((0, 0), result)

    def test_get_bottom_right_pixel(self):
        bottomRightPoint = Coordinates(1, 1)
        result = get_pixel(bottomRightPoint, (10, 10))
        self.assertEqual((9, 9), result)

    def test_paint_pixel(self):
        image = generate_pixel_array((10, 10))
        # Initially, there should be no pixels painted
        self.assertEqual(image.nnz, 0)

        bottomRightPoint = Coordinates(1, 1)
        paint_pixel(bottomRightPoint, image)
        self.assertEqual(image[9, 9], 1)

        # Finally, there should be 1 pixel painted
        self.assertEqual(image.nnz, 1)
