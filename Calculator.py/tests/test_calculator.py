# Simple tests for all modules. Run from the project folder with:
#   python -m unittest discover tests -b
import unittest

from Arithmetic import add, subtract, multiply, divide
from scientific import sine, cosine, tangent, logarithm, square_root, cube_root
from extras import exponential, factorial


class TestArithmetic(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add([1, 2, 3]), 6)

    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)

    def test_multiply(self):
        self.assertEqual(multiply([2, 3, 4]), 24)

    def test_divide(self):
        self.assertEqual(divide(7, 2), (3, 1, 3.5))

    def test_divide_by_zero(self):
        self.assertIsNone(divide(5, 0))


class TestScientific(unittest.TestCase):
    def test_sine(self):
        self.assertAlmostEqual(sine(30), 0.5)

    def test_cosine(self):
        self.assertAlmostEqual(cosine(60), 0.5)

    def test_tangent(self):
        self.assertAlmostEqual(tangent(45), 1.0)

    def test_tangent_90_not_defined(self):
        self.assertIsNone(tangent(90))

    def test_logarithm(self):
        log10, ln, log2 = logarithm(100)
        self.assertAlmostEqual(log10, 2.0)

    def test_logarithm_negative(self):
        self.assertIsNone(logarithm(-5))

    def test_square_root(self):
        self.assertEqual(square_root(25), 5.0)

    def test_square_root_negative(self):
        self.assertIsNone(square_root(-4))

    def test_cube_root(self):
        self.assertAlmostEqual(cube_root(27), 3.0)


class TestExtras(unittest.TestCase):
    def test_exponential(self):
        self.assertEqual(exponential(2, 3), 8)

    def test_zero_to_negative_power(self):
        self.assertIsNone(exponential(0, -1))

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)

    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_negative(self):
        self.assertIsNone(factorial(-3))


if __name__ == "__main__":
    unittest.main()
