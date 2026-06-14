from typing import List

from screen import Screen

class Theatre:
    def __init__(self, id: int, location: str) -> None:
        self.id = id 
        self.location = location
        self.screens: List[Screen] = []

    def add_screen(self) -> None:
        if len(self.screens) == 0:
            screen_id = 1
        else:
            screen_id = self.screens[-1].id + 1 

        screen = Screen(screen_id)
        self.screens.append(screen)

        print(f"Screen {screen_id} added successfully to Theatre {self.id} ({self.location}).")

    def list_screens(self) -> List[Screen]:
        if len(self.screens) == 0:
            print(f"No screens found in Theatre {self.id} ({self.location}).")
        else:
            print(f"{len(self.screens)} screen(s) found in Theatre {self.id} ({self.location}).")
        return self.screens