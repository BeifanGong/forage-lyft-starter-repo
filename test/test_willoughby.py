import unittest
from engine.willoughby_engine import WilloughbyEngine


class TestWilloughby(unittest.TestCase):
    def test_should_be_serviced(self):
        eng = WilloughbyEngine(90000, 20000)
        self.assertTrue(eng.needs_service())

    def test_should_not_be_serviced(self):
        eng = WilloughbyEngine(90000, 60000)
        self.assertFalse(eng.needs_service())
