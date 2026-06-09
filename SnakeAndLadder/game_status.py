from enum import Enum 

class GameStatus(Enum):
    NOT_STARTED = 'not_started'
    IN_PROGRESS = 'in_progress'
    FINISHED = 'finished'