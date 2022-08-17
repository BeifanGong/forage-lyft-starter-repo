from os import cpu_count
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.spindler_battery import SpindlerBattery
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from engine.nubbin_battery import NubbinBattery


class CarFactory():
    def __init__(self) -> None:
        pass

    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        capulet = CapuletEngine(
            current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        spindler = SpindlerBattery(
            last_service_date=last_service_date, current_date=current_date)

        return Car(capulet, spindler)

    @staticmethod
    def create_gilssade(current_date, last_service_date, current_mileage, last_service_mileage):
        willoughby = WilloughbyEngine(
            current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        spindler = SpindlerBattery(
            last_service_date=last_service_date, current_date=current_date)
        return Car(willoughby, spindler)

    @staticmethod
    def create_palindrome(current_date, last_service_date, waring_light_on):
        sternman = SternmanEngine(warning_light_is_on=waring_light_on)
        spindler = SpindlerBattery(
            last_service_date=last_service_date, current_date=current_date)
        return Car(sternman, spindler)

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        willoughby = WilloughbyEngine(
            current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        nubbin = NubbinBattery(
            last_service_date=last_service_date, current_date=current_date)
        return Car(willoughby, nubbin)

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        capulet = CapuletEngine(
            current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        nubbin = NubbinBattery(
            last_service_date=last_service_date, current_date=current_date)
        return Car(capulet, nubbin)
