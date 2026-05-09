
from abc import ABC
from homework_05 import exceptions

class Vehicle(ABC):
    def __init__(self, weight: float = 0, fuel: float = 0, fuel_consumption: float = 0):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started: bool = False

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise exceptions.LowFuelError("Not enough fuel to start")

    def move(self, distance: float):
        required_fuel = distance * self.fuel_consumption
        if self.fuel >= required_fuel:
            self.fuel -= required_fuel
        else:
            raise exceptions.NotEnoughFuel("Not enough fuel for this distance")
