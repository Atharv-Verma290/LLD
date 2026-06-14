from datetime import datetime
from typing import Optional, List

from movie import Movie 
from seat import Seat
from enumerations import SeatStatus, SeatType

class Show:
    def __init__(self, id: int, movie: Movie, start_time: datetime) -> None:
        self.id = id 
        self.movie = movie
        self.start_time = start_time
        self.seats: List[Seat] = []

    @property
    def end_time(self) -> datetime:
        return self.start_time + self.movie.duration

    def find_available_seats(self) -> List[Seat]: 
        available_seats = []
        for seat in self.seats:
            if seat.is_available:
                available_seats.append(seat)

        if len(available_seats) == 0:
            print(f"No available seats for Show {self.id}.")
        else:
            print(f"{len(available_seats)} seat(s) available for Show {self.id}.")
        
        return available_seats

    def book_seat(self, seat_nbr: int) -> Seat:
        if seat_nbr < 1 or seat_nbr > len(self.seats):
            raise ValueError(f"Seat {seat_nbr} does not exist!")
        
        seat = self.seats[seat_nbr-1]

        if not seat.is_available:
            raise ValueError(f"Seat {seat_nbr} is already booked!")
        
        seat.status = SeatStatus.BOOKED
        print(f"Seat {seat_nbr} booked successfully for Show {self.id}.")

        return seat
    
    def add_seat(self, type: SeatType) -> None:
        if type is None:
            raise ValueError("Seat type cannot be None!")
        
        if len(self.seats) == 0:
            seat_nbr = 1
        else:
            seat_nbr = self.seats[-1].id + 1

        seat = Seat(id=seat_nbr, type=type)
        self.seats.append(seat)

        print(f"Seat {seat_nbr} of type {type.name} added to Show {self.id}.")