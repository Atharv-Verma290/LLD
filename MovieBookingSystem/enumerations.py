from enum import Enum

class SeatStatus(Enum):
    AVAILABLE = "available"
    BOOKED = "booked"

class SeatType(Enum):
    REGULAR = "regular"
    PREMIUM = "premium"