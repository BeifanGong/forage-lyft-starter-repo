from serviceable import Serviceable
from abc import abstractmethod
from engine.carengine import Engine
from engine.battery import Battery
from engine.tire import Tire


class Car(Serviceable):
    def __init__(self, engine, battery, tire):
        self.engine = engine
        self.battery = battery
        self.tire = tire

    def needs_service(self):
        if self.engine.needs_service() or self.battery.needs_service() or self.tire.needs_service():
            return True
        return False
