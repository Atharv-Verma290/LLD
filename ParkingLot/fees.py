from abc import ABC, abstractmethod
from ticket import Ticket
from parking_types import SpotType, VehicleType

class FeeStrategy(ABC):
    @abstractmethod
    def calculate_fees(self, ticket: Ticket) -> float:
        pass


class SpotBasedFeeStrategy(FeeStrategy):
    spot_pricing = {
        SpotType.SMALL: 10.00,
        SpotType.MEDIUM: 20.00,
        SpotType.LARGE: 30.00
    }

    def calculate_fees(self, ticket: Ticket) -> float:
        pricing = self.spot_pricing[ticket.spot_type]
        fee  = round(float(pricing * ticket.get_duration_hourly()), 2) 
        return fee
            


class VehicleBasedFeeStrategy(FeeStrategy):
    vehicle_pricing = {
        VehicleType.BIKE: 10.00,
        VehicleType.CAR: 20.00,
        VehicleType.TRUCK: 30.00
    }

    def calculate_fees(self, ticket: Ticket) -> float:
        pricing = self.vehicle_pricing[ticket.vehicle_type]
        fee = round(float(pricing * ticket.get_duration_hourly()), 2) 
        return fee

class FeeManager:
    def __init__(self, strategy: FeeStrategy) -> None:
        self._strategy = strategy

    def set_strategy(self, strategy: FeeStrategy):
        self._strategy = strategy

    def calculate_fees(self, ticket: Ticket) -> float:
        return self._strategy.calculate_fees(ticket)