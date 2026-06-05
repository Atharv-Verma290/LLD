from enum import Enum

class Symbol(Enum):
    X = 'X'
    O = 'O'
    EMPTY = '_'

class GameStatus(Enum):
    IN_PROGRESS = 'in_progress'
    WINNER_X = 'winner_x'
    WINNER_O = 'winner_o'
    DRAW = 'draw'