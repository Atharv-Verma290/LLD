from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
from player import Player

if TYPE_CHECKING:
    from game import Game

class GameObserver(ABC):
    @abstractmethod
    def update(self, game: "Game") -> None:
        pass


class ScoreBoard(GameObserver):
    def __init__(self) -> None:
        self._scores = {}

    def record_win(self, player: Player) -> None:
        name = player.name 
        self._scores[name] = self._scores.get(name, 0) + 1

    def print_scoreboard(self) -> None:
        print("Scoreboard: ")
        for player, score in self._scores.items():
            print(f"{player}: {score}")

    def update(self, game: "Game") -> None:
        winner = game.players[game.current_player_idx] 
        self.record_win(winner)
