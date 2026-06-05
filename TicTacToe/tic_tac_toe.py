from typing import List

from enumerations import Symbol, GameStatus
from game import Game 
from observer import ScoreBoard
from player import Player
from winning_strategy import WinningStrategy, RowStrategy, ColumnStrategy, DiagonalStrategy

class TicTacToeSystem:
    def __init__(self) -> None:
        self.score_board = ScoreBoard()
        self.current_game = None

    def create_game(self, p1: Player, p2: Player, size: int = 3, strategies: List[WinningStrategy] = [RowStrategy(), ColumnStrategy(), DiagonalStrategy()]) -> None:

        self.current_game = Game(p1, p2, size, strategies)
        self.current_game.subscribe(self.score_board)
    
    def make_move(self, row: int, col: int, player: Player) -> None:
        if self.current_game is None:
            raise RuntimeError("No active game!")
        
        if self.current_game.status != GameStatus.IN_PROGRESS:
            raise RuntimeError("Game has ended!")

        current_player = self.current_game.players[self.current_game.current_player_idx]
        if player != current_player:
            raise ValueError("Not your turn!")
    
        self.current_game.make_move(row, col)

    def print_scoreboard(self) -> None:
        self.score_board.print_scoreboard()

tic_tac_toe_system = TicTacToeSystem()
