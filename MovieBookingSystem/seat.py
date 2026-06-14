from enumerations import SeatType, SeatStatus

class Seat:
    def __init__(self, id: int, type: SeatType) -> None:
        self.id = id 
        self.type = type 
        self.status = SeatStatus.AVAILABLE

    @property
    def is_available(self) -> bool:
        return self.status == SeatStatus.AVAILABLE