"""
создайте класс `Plane`, наследник `Vehicle`
"""

from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    def __init__(self, cargo, max_cargo):
        super().__init__()
        self.cargo = cargo
        self.max_cargo = max_cargo

    def load_cargo(self, numeric: int):
        if self.cargo + numeric < self.max_cargo:
            self.cargo += numeric
        else:
            raise CargoOverload
