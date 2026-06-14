from datetime import datetime, timedelta

class Movie:
    def __init__(self, name: str, duration: timedelta, genre: str) -> None:
        self.name = name 
        self.duration = duration 
        self.genre = genre