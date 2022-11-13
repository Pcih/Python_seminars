import unittest
from lesson_9.script.stationery import Stationery, Pen
"""
Тут я попробовал проверить классы.
"""


class TestStationery(unittest.TestCase):

    def test_class(self):
        self.assertNotIsInstance(Stationery, Pen)