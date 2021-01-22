import unittest
from calculator import calculate

class TestCalculator(unittest.TestCase):
    def test_dodawanie(self):
        r = calculate(1, 2, '+')
        self.assertEqual(r, 3)

    def test_odejmowanie(self):
        r = calculate(4, 2, '-')
        self.assertEqual(r, 2)

    def test_mnozenie(self):
        r = calculate(2, 3, '*')
        self.assertEqual(r, 6)

    def test_dzielenie(self):
        r = calculate(4, 2, '/')
        self.assertEqual(r, 2)
