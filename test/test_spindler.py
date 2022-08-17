from datetime import datetime
import unittest
from engine.spindler_battery import SpindlerBattery


class TestSpindler(unittest.TestCase):
    def test_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year-3)
        bat = SpindlerBattery(
            last_service_date=last_service_date, current_date=current_date)
        self.assertTrue(bat.needs_service())

    def test_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year-1)
        bat = SpindlerBattery(
            last_service_date=last_service_date, current_date=current_date)
        self.assertFalse(bat.needs_service())
