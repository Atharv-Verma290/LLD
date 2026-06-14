from typing import List

from theatre import Theatre

class City:
    def __init__(self, name: str) -> None:
        self.name = name 
        self.theatres: List[Theatre] = []

    def add_theatre(self, location: str) -> None:
        if location.strip() == "":
            raise ValueError("Theatre location cannot be empty!")

        for theatre in self.theatres:
            if theatre.location == location:
                raise ValueError(
                    f"Theatre at '{location}' already exists!"
                )

        if len(self.theatres) == 0:
            theatre_id = 1
        else:
            theatre_id = self.theatres[-1].id + 1

        theatre = Theatre(theatre_id, location)
        self.theatres.append(theatre)

        print(f"Theatre {theatre_id} at '{location}' added successfully.")

    def list_theatres(self) -> List[Theatre]:
        if len(self.theatres) == 0:
            print(f"No theatres found in {self.name}.")
        return self.theatres
            