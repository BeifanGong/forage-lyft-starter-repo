from abc import ABC, abstractmethod
from ast import Pass


class Tire(ABC):
    @abstractmethod
    def need_service(self):
        Pass
