from abc import ABC


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
                raise Exception
