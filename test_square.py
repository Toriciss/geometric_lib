import unittest
from square import area
from square import perimeter

class SquareTestCase(unittest.TestCase):
    def test_square_area_positive(self):
        res = area(8)
        self.assertEqual(res, 64)

    def test_square_area_negative(self):
        with self.assertRaises(ValueError):
            area(-8)

    def test_square_area_real(self):
        res = area(8.8)
        self.assertEqual(res, 77.44000000000001)

    def test_square_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_square_perimeter_positive(self):
        res = perimeter(8)
        self.assertEqual(res, 32)

    def test_square_perimeter_negative(self):
        with self.assertRaises(ValueError):
            perimeter(-8)

    def test_square_perimeter_real(self):
        res = perimeter(8.8)
        self.assertEqual(res, 35.2)

    def test_square_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

