from os import times_result
from tire import Tire


class Octoprime(Tire):
    def __init__(self, tires) -> None:
        self.tires = tires

    def need_service(self):
        sum = 0
        for tire in self.tires:
            sum += tire

        if (sum >= 3):
            return True
        return False
