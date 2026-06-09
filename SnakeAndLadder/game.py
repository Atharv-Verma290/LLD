from collections import deque
from typing import Deque, List, Self, Optional

from game_status import GameStatus
from board import Board, BoardEntity
from dice import Dice
from player import Player

class Game:
    def __init__(self, builder: GameBuilder) -> None:
        assert builder.players is not None
        assert builder.board is not None 
        assert builder.dice is not None

        self.board = builder.board
        self.dice = builder.dice
        self.players = builder.players
        self.status = GameStatus.NOT_STARTED
        self.winner: Optional[Player] = None

    def play(self):
        if len(self.players) < 2:
            print("Cannot start the game. Atleast 2 players are required.")
            return 
    
        self.status = GameStatus.IN_PROGRESS
        print("Game Started!")

        while self.status == GameStatus.IN_PROGRESS:
            current_player = self.players.popleft()
            self.take_turn(current_player)

            if self.status == GameStatus.IN_PROGRESS:
                self.players.append(current_player)

        print("Game Finished!")
        if self.winner:
            print(f"The winner is {self.winner.name}")

    def take_turn(self, player: Player):
        curr_position = player.position
        roll = self.dice.roll()
        new_position = curr_position + roll
        final_position = self.board.get_final_position(new_position)

        # check for win
        if new_position == self.board.size:
            player.position = new_position
            self.winner = player 
            self.status = GameStatus.FINISHED
            print(f"{player.name} reached the final square {self.board.size} and won!")
            return 
        
        # check for overshoot
        if new_position > self.board.size:
            print(f"{player.name} needs to land exactly on {self.board.size}. Turn skipped.")
            return 
        
        # apply snake or ladder logic
        final_position = self.board.get_final_position(new_position)

        if final_position > new_position:
            print(f"{player.name} found a ladder at {new_position} and climbed to {final_position}.")
        elif final_position < new_position:
            print(f"{player.name} was eaten by a snake at {new_position} and slid down to {final_position}.")
        else:
            print(f"{player.name} moved from {curr_position} to {final_position}.")
            
        player.position = final_position

        # extra turn for rolling 6
        if roll == 6:
            print(f"{player.name} rolled a 6 and gets another turn!")
            self.take_turn(player)


class GameBuilder:
    def __init__(self) -> None:
        self.board: Optional[Board] = None 
        self.dice: Optional[Dice] = None 
        self.players: Optional[Deque[Player]] = None 

    def set_board(self, size: int, board_enitites: List[BoardEntity]) -> Self:
        self.board = Board(size=size, entities=board_enitites)
        return self
    
    def set_dice(self, min_value: int, max_value: int) -> Self:
        self.dice = Dice(min_value, max_value)
        return self
    
    def set_players(self, player_names: List[str]) -> Self:
        self.players = deque()
        for name in player_names:
            self.players.append(Player(name))
        return self
    
    def build(self) -> Game:
        if (self.board is None) or (self.players is None) or (self.dice is None):
            raise ValueError("Board, Players, and Dice must be set!")
        return Game(self)