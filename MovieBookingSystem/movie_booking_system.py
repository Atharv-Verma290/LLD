from typing import List, Optional

from city import City
from show import Show
from seat import Seat

class MovieBookingSystem:

    def __init__(self) -> None:
        self.cities: List[City] = []

    def add_city(self, name: str) -> None:
        for city in self.cities:
            if city.name == name:
                raise ValueError(f"City '{name}' already exists!")
            
        city = City(name)
        self.cities.append(city)
        print(f"City '{name}' added successfully.")

    def remove_city(self, name: str) -> None:
        for city in self.cities:
            if city.name == name:
                self.cities.remove(city)
                print(f"City '{name}' removed successfully.")
                return
        
        raise ValueError(f"City '{name}' does not exist!")

    def get_city(self, name: str) -> City:
        for city in self.cities:
            if city.name == name:
                return city 
        
        raise ValueError(f"City '{name}' not found!")
    
    def search_shows(self, city: Optional[str] = None, location: Optional[str] = None, movie_name: Optional[str] = None) -> List[Show]:
        shows = []
        for curr_city in self.cities:
            if city is not None and curr_city.name != city:
                continue

            for theatre in curr_city.list_theatres():
                if location is not None and theatre.location != location:
                    continue 

                for screen in theatre.list_screens():
                    for show in screen.list_shows():
                        if movie_name is not None and show.movie.name != movie_name:
                            continue 

                        shows.append(show)

        if len(shows) == 0:
            print("No shows found.")
        else:
            print(f"{len(shows)} show(s) found.")
        return shows
    

    def find_seats(self, show: Show) -> List[Seat]:
        if show is None:
            raise ValueError("Show must exist!")
        
        available_seats = show.find_available_seats()
        if len(available_seats) == 0:
            print("No seats available.")
        else:
            print(f"{len(available_seats)} seat(s) available.")
        return available_seats
    
    def book_seats(self, show: Show, seat_numbers: List[int]) -> List[Seat]:
        if show is None:
            raise ValueError("Show must exist!")
        
        if len(seat_numbers) == 0:
            raise ValueError("At least one seat must be selected.")
        
        booked_seats = []

        for seat_number in seat_numbers:
            if seat_number <= 0:
                raise ValueError(f"Invalid seat number: {seat_number}")
            booked_seat = show.book_seat(seat_number)
            booked_seats.append(booked_seat)
            
        print(f"Successfully booked {len(booked_seats)} seat(s).")
        return booked_seats
    

system = MovieBookingSystem()