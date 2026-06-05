from typing import List
from parking_spot import ParkingSpot, SpotType
from vehicle import Vehicle


class Level:
    def __init__(self, level_nbr: int) -> None:
        self.level_nbr = level_nbr
        self.spots: List[ParkingSpot] = []


    def find_available_spot(self, vehicle: Vehicle) -> ParkingSpot:
        for spot in self.spots:
            if spot.can_fit(vehicle) and spot.check_availability():
                return spot
            
        raise RuntimeError(f"No available spots for {vehicle.vehicle_type.value} found on Level {self.level_nbr}!")


    def get_parked_spot(self, spot_id: int) -> ParkingSpot:
        for spot in self.spots:
            if spot.spot_id == spot_id:
                return spot 
            
        raise ValueError(f"No spot found for this id: {spot_id} on Level {self.level_nbr}!")


    def add_spot(self, spot_type: SpotType) -> None:
        spot_id = int(str(self.level_nbr) + str(len(self.spots) + 1))
        new_spot = ParkingSpot(spot_id, spot_type)
        self.spots.append(new_spot)
        

    def remove_spot(self, spot_id: int) -> None:
        for spot in self.spots:
            if spot.spot_id == spot_id:
                self.spots.remove(spot)
                return
        
        raise ValueError(f"Spot id {spot_id} doesn't exist!")


    def display_availability(self) -> int:
        count = 0
        for spot in self.spots:
            if spot.check_availability():
                count += 1
        
        print(f"For Level {self.level_nbr}: Out of {len(self.spots)} spots, {count} spots are free.")
        return count

