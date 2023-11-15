import unittest
from circle import area,perimeter

class CircleTestCase(unittest.TestCase):
    def test_circle_area_positive(self):
        res = area(3)
        self.assertEqual(res, 28.274333882308138)

    def test_circle_area_negative(self):
        res = area(-3)
        self.assertEqual(res, "The radius cannot be negative")

    def test_circle_area_real(self):
        res = area(3.3)
        self.assertEqual(res, 34.21194399759285)

    def test_circle_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_circle_perimeter_positive(self):
        res = perimeter(3)
        self.assertEqual(res, 18.84955592153876)

    def test_circle_perimeter_negative(self):
        res = perimeter(-3)
        self.assertEqual(res, "The radius cannot be negative")

    def test_circle_perimeter_real(self):
        res = perimeter(3.3)
        self.assertEqual(res, 20.734511513692635)

    def test_circle_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
if __name__ == '__main__':
    unittest.main()