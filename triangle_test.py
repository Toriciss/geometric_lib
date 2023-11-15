import unittest
from triangle import area, perimeter
class TriangleTestCase(unittest.TestCase):
    def test_triangle_area_positive(self):
        res = area(3, 8)
        self.assertEqual(res, 12)

    def test_triangle_area_negative(self):
        res = area(10, -8)
        self.assertEqual(res, "The base and height cannot be negative")

    def test_triangle_area_real(self):
        res = area(8.8, 6.6)
        self.assertEqual(res, 29.04)

    def test_triangle_area_zero(self):
        res = area(8, 0)
        self.assertEqual(res, 0)

    def test_triangle_perimeter_positive(self):
        res = perimeter(6, 7, 8)
        self.assertEqual(res,21)

    def test_triangle_perimeter_negative(self):
        res = perimeter(8, -3, 4)
        self.assertEqual(res, "The base and height cannot be negative")

    def test_triangle_perimeter_real(self):
        res = perimeter(7.7, 2.5, 9)
        self.assertEqual(res, 19.2)

    def test_triangle_perimeter_zero(self):
        res = perimeter(6, 4, 6.6)
        self.assertEqual(res, 16.6)


if __name__ == '__main__':
    unittest.main()