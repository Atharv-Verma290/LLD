from datetime import datetime
from typing import List
from show import Show
from movie import Movie

class Screen:
    def __init__(self, id: int) -> None:
        self.id = id 
        self.shows: List[Show] = []

    def add_show(self, movie: Movie, start_time: datetime) -> None:
        if movie is None:
            raise ValueError("Movie cannot be None!")

        if start_time is None:
            raise ValueError("Start time cannot be None!")
        
        for existing_show in self.shows:
            if (start_time < existing_show.end_time and start_time + movie.duration > existing_show.start_time):
                raise ValueError(f"Show timing conflicts with Show {existing_show.id}.")

        if len(self.shows) == 0:
            show_id = 1
        else:
            show_id = self.shows[-1].id + 1

        show = Show(show_id, movie, start_time)
        self.shows.append(show)

        print(f"Show {show_id} for '{movie.name}' added successfully to Screen {self.id}.")

    def remove_show(self, show_id: int) -> None:
        for show in self.shows:
            if show.id == show_id:
                self.shows.remove(show)
                print(f"Show {show_id} removed successfully from Screen {self.id}.")
                return

        raise ValueError(f"Show {show_id} does not exist!")

    def list_shows(self) -> List[Show]:
        if len(self.shows) == 0:
            print(f"No shows found in Screen {self.id}.")
        else:
            print(f"{len(self.shows)} show(s) found in Screen {self.id}.")

        return self.shows
