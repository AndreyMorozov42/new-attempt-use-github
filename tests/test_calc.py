import unittest
import sys

sys.path.insert(0, "..")
from calc.calc import Calc


class TestCalc(unittest.TestCase):
    def setUp(self):
        self.a = 1
        self.b = 1

    def test_plus(self):
        self.assertEqual(Calc(self.a, self.b, "+").result, 2)

    def test_minus(self):
        self.assertEqual(Calc(self.a, self.b, "-").result, 0)

    def test_mult(self):
        self.assertEqual(Calc(self.a, self.b, "*").result, 1)

    def test_dev(self):
        self.assertEqual(Calc(self.a, self.b, "/").result, 1.0)


if __name__ == "__main__":
    unittest.main()