from abc import ABC


class Vehicle(ABC):
    def __init__(self, weight=None, started=False, fuel=None, fuel_consumption=None):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    @classmethod
    def start():
        pass

