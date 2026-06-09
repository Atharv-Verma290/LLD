from board_entity import Snake, Ladder
from game import GameBuilder, Game

def main():
    board_entities = [
        Snake(17, 7),
        Snake(54, 34),
        Snake(62, 19),
        Snake(98, 79),
        Ladder(3, 38),
        Ladder(24, 33),
        Ladder(42, 93),
        Ladder(72, 84)
    ]

    player_names = ["Alice", "Bob", "Charlie"]

    builder = GameBuilder()
    game = builder.set_board(100, board_enitites=board_entities).set_dice(1, 6).set_players(player_names=player_names).build()

    game.play()

if __name__ == "__main__":
    main()