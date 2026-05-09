
from homework_05.base import Vehicle
from homework_05 import exceptions

class Plane(Vehicle):
    def __init__(self, weight: float, fuel: float, fuel_consumption: float, max_cargo: float):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo
        self.cargo: float = 0

    def load_cargo(self, weight: float):
        if self.cargo + weight <= self.max_cargo:
            self.cargo += weight
        else:
            raise exceptions.CargoOverload("Cargo weight exceeds capacity")

    def remove_all_cargo(self) -> float:
        old_cargo = self.cargo
        self.cargo = 0
        return old_cargo
