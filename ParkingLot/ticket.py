from datetime import datetime
import math
from parking_types import SpotType, VehicleType

class Ticket:
    def __init__(self, level_nbr: int, spot_id: int, spot_type: SpotType, vehicle_nbr: str, vehicle_type: VehicleType) -> None:
        self.level_nbr = level_nbr
        self.spot_id = spot_id
        self.spot_type = spot_type
        self.vehicle_nbr = vehicle_nbr
        self.vehicle_type = vehicle_type
        self.ticket_id = '_'.join([str(self.level_nbr), str(self.spot_id)])
        self.entry_at = datetime.now() 
        self.exit_at = None
        
    def mark_exit(self) -> None:
        self.exit_at = datetime.now()

    def get_duration_hourly(self) -> int:
        if self.exit_at is None:
            raise ValueError("Vehicle has not exited yet.")
        duration = math.ceil((self.exit_at - self.entry_at).total_seconds() / 3600)
        return duration