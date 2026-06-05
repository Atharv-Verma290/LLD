from typing import List

from observer import GameObserver
from player import Player
from board import Board
from winning_strategy import WinningStrategy
from enumerations import GameStatus, Symbol

class Game():
    def __init__(self, p1: Player, p2: Player, board_size: int, strategies: List[WinningStrategy]) -> None:
        self.players: List[Player] = [p1, p2]
        self.board = Board(size=board_size)
        self.status: GameStatus = GameStatus.IN_PROGRESS
        self.strategies: List[WinningStrategy] = strategies
        self.current_player_idx: int = 0
        self.observers: List[GameObserver] = []

    def make_move(self, row: int, col: int) -> None:
        if self.status != GameStatus.IN_PROGRESS:
            raise RuntimeError("Game has already ended!")
        
        symbol = self.players[self.current_player_idx].assigned_symbol
        self.board.place_symbol(row, col, symbol)

        for strategy in self.strategies:
            if strategy.check_win(self.board, row, col, symbol):
                if symbol == Symbol.O:
                    self.status = GameStatus.WINNER_O
                else:
                    self.status = GameStatus.WINNER_X
                print(f"Player {self.players[self.current_player_idx].name}, Symbol {symbol} has won the game.")
                self.notify()
                break
        
        if self.status == GameStatus.IN_PROGRESS and self.board.is_full():
            self.status = GameStatus.DRAW
            print("The game has ended in a DRAW!")
            return
        
        if self.status == GameStatus.IN_PROGRESS:
            self.current_player_idx = (self.current_player_idx + 1) % len(self.players)

        self.board.print_board()

    def subscribe(self, observer: GameObserver) -> None:
        if observer in self.observers:
            raise ValueError("Observer already subscribed!")
        self.observers.append(observer)

    def unsubscribe(self, observer: GameObserver) -> None:
        if observer not in self.observers:
            raise ValueError("Observer already unsubscribed!")
        self.observers.remove(observer)


    def notify(self) -> None:
        for observer in self.observers:
            observer.update(self)
        print("All observers have been notified.")