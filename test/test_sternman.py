import unittest
from engine.sternman_engine import SternmanEngine


class TestSternman(unittest.TestCase):
    def test_should_be_serviced(self):
        eng = SternmanEngine(True)
        self.assertTrue(eng.needs_service())

    def test_should_not_be_serviced(self):
        eng = SternmanEngine(False)
        self.assertFalse(eng.needs_service())
