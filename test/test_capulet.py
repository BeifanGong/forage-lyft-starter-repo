import unittest
from engine.capulet_engine import CapuletEngine


class TestCapulet(unittest.TestCase):
    def test_should_be_serviced(self):
        current_mileage = 40000
        last_service_mileage = 0
        eng = CapuletEngine(current_mileage=current_mileage,
                            last_service_mileage=last_service_mileage)
        self.assertTrue(eng.needs_service())

    def test_should_not_be_serviced(self):
        current_mileage = 20000
        last_service_mileage = 0
        eng = CapuletEngine(current_mileage=current_mileage,
                            last_service_mileage=last_service_mileage)
        self.assertFalse(eng.needs_service())
