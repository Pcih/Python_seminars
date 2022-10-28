import unittest
from lesson_9.script.numbers import products_of_numbers


class TestProductsOfNumbers(unittest.TestCase):

    def test_passed(self):
        self.assertEqual(products_of_numbers(5), [1, 2, 6, 24, 120])

    def test_fail(self):
        with self.assertRaises(Exception):
            products_of_numbers('5')


if __name__ == '__main__':
    unittest.main()