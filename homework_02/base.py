from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    def __init__(self, weight=None, fuel=None, fuel_consumption=None):
        self.weight = weight
        self.started = False
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError

    def move(self, distance=1):
        required_fuel = self.fuel_consumption * distance
        if self.fuel >= required_fuel:
            self.fuel -= required_fuel
        else:
            raise NotEnoughFuel
