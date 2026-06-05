from typing import Optional 
from vehicle import Vehicle
from parking_types import SpotType


class ParkingSpot:
    def __init__(self, spot_id: int, spot_type: SpotType, vehicle: Optional[Vehicle] = None) -> None:
        self.spot_id = spot_id
        self.spot_type = spot_type
        self.is_free = True
        self.vehicle = vehicle


    def check_availability(self) -> bool:
        return self.is_free
    

    def check_type(self):
        return self.spot_type
    

    def can_fit(self, vehicle: Vehicle) -> bool:
        return self.spot_type == vehicle.required_spot_type


    def park_vehicle(self, vehicle: Vehicle) -> None:
        if self.is_free:
            self.vehicle = vehicle
            self.is_free = False 
        else:
            raise RuntimeError("Spot is already occupied!")


    def unpark_vehicle(self) -> None:
        if self.vehicle:
            self.vehicle = None 
            self.is_free = True 
        else:
            raise RuntimeError("Spot is already free!")