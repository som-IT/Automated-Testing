import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5),
        self.assertEqual(self.calc.add(-3, -3), -6),
        self.assertEqual(self.calc.add(0, 0), 0),

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 5), 5),
        self.assertEqual(self.calc.subtract(0, 5), -5),
        self.assertEqual(self.calc.subtract(-5, -5), 0),

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 3), 9),
        self.assertEqual(self.calc.multiply(-1, 3), -3),
        self.assertEqual(self.calc.multiply(0, 3), 0),
    
    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertAlmostEqual(self.calc.divide(5, 3), 1.6667, places=4)
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)
if __name__ == "__main__":
    unittest.main()