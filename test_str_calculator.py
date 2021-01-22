import unittest
from str_calculator import str_calculator


class TestStringCalculator(unittest.TestCase):
    def test_concat(self):
        r = str_calculator("a", "b", 'concat')
        self.assertEqual(r, 'ab')

    def test_contain(self):
        r = str_calculator('a', 'bbbaaa', 'contain')
        self.assertEqual(r, True)

    def test_endsWith(self):
        r = str_calculator('a', 'ba', 'endsWith')
        #self.assertEqual(r, True)
        self.assertTrue(r)

    def test_startsWith(self):
        r = str_calculator('xyz', 'xyzzzzzz', 'endsWith')
        self.assertEqual(r, True)
