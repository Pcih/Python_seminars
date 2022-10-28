import unittest
from lesson_9.script.sum_numbers import sum_numbers

"""
Тут проверил валидность с использованием словаря.
"""


class TestSumNumbers(unittest.TestCase):

    def test_get_sum_ok(self):
        list_res = {'234': 9, '2333': 11, '2,5': 7, '2.3': 5, '5a5': 10}
        for i, z in list_res.items():
            self.assertEqual(sum_numbers(i), z)

    def test_get_sum_int(self):
        with self.assertRaises(Exception):
            sum_numbers(123)


if __name__ == '__main__':
    unittest.main()