from abc import ABC

class BoardEntity(ABC):
    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end 


class Snake(BoardEntity):
    def __init__(self, start: int, end: int) -> None:
        if start <= end:
            raise ValueError("Head of Snake must be higher than the tail!")
        
        super().__init__(start, end)


class Ladder(BoardEntity):
    def __init__(self, start: int, end: int) -> None:
        if start >= end:
            raise ValueError("The bottom of the Ladder must be lower than the top!")
        
        super().__init__(start, end)

