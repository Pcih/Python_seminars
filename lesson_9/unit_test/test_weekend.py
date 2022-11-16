import unittest
from lesson_9.script.weekend import get_is_weekend


class TestWeeks(unittest.TestCase):

    def test_get_is_weekend_ok(self):
        weekend = [6, 7]
        for i in weekend:
            self.assertEqual(get_is_weekend(i), 'Да это выходной!!!')

    def test_get_is_working_days_ok(self):
        working_days = [1, 2, 3, 4, 5]
        for i in working_days:
            self.assertEqual(get_is_weekend(i), 'Нет увы это рабочий день')

    def test_get_err_days(self):
        err_day = [9, 11]
        for i in err_day:
            self.assertEqual(get_is_weekend(i), 'Увы вы ввели не то число!')

    def test_get_err_str(self):
        err_str = ['выходной', ' ']
        for i in err_str:
            with self.assertRaises(Exception):
                get_is_weekend(i)


if __name__ == '__main__':
    unittest.main()
