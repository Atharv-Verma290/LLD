from abc import ABC, abstractmethod
from parking_types import VehicleType, SpotType


class Vehicle(ABC):
    def __init__(self, registration_nbr: str, vehicle_type: VehicleType) -> None:
        self.registration_nbr = registration_nbr
        self.vehicle_type = vehicle_type

    @property
    @abstractmethod
    def required_spot_type(self) -> SpotType:
        pass


class Bike(Vehicle):
    def __init__(self, registration_nbr: str) -> None:
        super().__init__(registration_nbr, VehicleType.BIKE)

    @property
    def required_spot_type(self) -> SpotType:
        return SpotType.SMALL
    

class Car(Vehicle):
    def __init__(self, registration_nbr: str) -> None:
        super().__init__(registration_nbr, VehicleType.CAR)

    @property
    def required_spot_type(self) -> SpotType:
        return SpotType.MEDIUM
    

class Truck(Vehicle):
    def __init__(self, registration_nbr: str) -> None:
        super().__init__(registration_nbr, VehicleType.TRUCK)

    @property
    def required_spot_type(self) -> SpotType:
        return SpotType.LARGE