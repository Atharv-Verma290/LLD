from typing import List, Optional
from parking_level import Level
from ticket import Ticket
from vehicle import Vehicle, Bike, Car, Truck
from parking_types import SpotType
from fees import FeeManager, SpotBasedFeeStrategy, VehicleBasedFeeStrategy
import threading

class ParkingLot:
    def __init__(self) -> None:
        self._lock = threading.Lock()
        self.levels: List[Level] = []
        self.fee_manager = FeeManager(SpotBasedFeeStrategy())


    def add_level(self) -> Level:
        with self._lock:
            new_level = Level(level_nbr=len(self.levels))
            self.levels.append(new_level)
            return new_level


    def remove_level(self) -> None:
        with self._lock:
            if len(self.levels) > 0:
                removed_level = self.levels.pop()
                print(f"Level {removed_level.level_nbr} removed from the lot")
            else:
                print("There are No levels in the parking lot!")


    def park_vehicle(self, vehicle: Vehicle) -> Optional[Ticket]:
        with self._lock:
            for level in self.levels:
                if level.display_availability() == 0:
                    print(f"Level {level.level_nbr} is Full!")
                    continue 
                    
                try:
                    valid_spot = level.find_available_spot(vehicle)
                    valid_spot.park_vehicle(vehicle)
                    parked_level = level 
                    print(f"[{threading.current_thread().name}] Generating Ticket...")
                    ticket = Ticket(level_nbr=parked_level.level_nbr, spot_id=valid_spot.spot_id, spot_type=valid_spot.spot_type, vehicle_nbr=vehicle.registration_nbr, vehicle_type=vehicle.vehicle_type)
                    return ticket

                except Exception as e: 
                    print(e)
            
            print("No Spot available in the Parking Lot")
            return None


    def unpark_vehicle(self, ticket: Ticket) -> Optional[float]:
        self.fee_manager.set_strategy(strategy=SpotBasedFeeStrategy())

        with self._lock:
            try: 
                for level in self.levels:
                    if level.level_nbr == ticket.level_nbr:
                        parked_spot = level.get_parked_spot(ticket.spot_id)
                        parked_spot.unpark_vehicle()
                        ticket.mark_exit()
                        fees = self.fee_manager.calculate_fees(ticket)
                                
                        print(f"[{threading.current_thread().name}] Vehicle unparked. Fees: {fees}")
                        return fees
                
            except Exception as e:
                print(e)
                return None


parking_lot = ParkingLot()
    