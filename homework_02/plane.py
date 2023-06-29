"""
создайте класс `Plane`, наследник `Vehicle`
"""

from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    def __init__(self, weight=150, fuel=50, fuel_consumption=5, max_cargo=30):
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo = 0
        self.max_cargo = max_cargo
        self.weight = weight

    def load_cargo(self, numeric: int):
        if self.cargo + numeric <= self.max_cargo:
            self.cargo += numeric
        else:
            raise CargoOverload

    def remove_all_cargo(self):
        current_cargo = self.cargo
        self.cargo = 0

        return current_cargo
