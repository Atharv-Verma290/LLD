from tic_tac_toe import TicTacToeSystem
from player import Player
from enumerations import Symbol


def create_players():
    p1 = Player("Atharv")
    p2 = Player("Rahul")

    p1.assign_symbol(Symbol.X)
    p2.assign_symbol(Symbol.O)

    return p1, p2


def run_scenario(name: str, func):
    print("\n" + "=" * 60)
    print(f"SCENARIO: {name}")
    print("=" * 60)

    try:
        func()
        print(f"\n✅ {name} PASSED")

    except Exception as e:
        print(f"\n❌ {name} FAILED")
        print(f"Reason: {e}")


# --------------------------------------------------
# Scenario 1: Row Win
# --------------------------------------------------
def test_row_win():
    system = TicTacToeSystem()

    p1, p2 = create_players()

    system.create_game(p1, p2)

    system.make_move(0, 0, p1)
    system.make_move(1, 0, p2)

    system.make_move(0, 1, p1)
    system.make_move(1, 1, p2)

    system.make_move(0, 2, p1)

    system.print_scoreboard()


# --------------------------------------------------
# Scenario 2: Column Win
# --------------------------------------------------
def test_column_win():
    system = TicTacToeSystem()

    p1, p2 = create_players()

    system.create_game(p1, p2)

    system.make_move(0, 0, p1)
    system.make_move(0, 1, p2)

    system.make_move(1, 0, p1)
    system.make_move(1, 1, p2)

    system.make_move(2, 0, p1)

    system.print_scoreboard()


# --------------------------------------------------
# Scenario 3: Diagonal Win
# --------------------------------------------------
def test_diagonal_win():
    system = TicTacToeSystem()

    p1, p2 = create_players()

    system.create_game(p1, p2)

    system.make_move(0, 0, p1)
    system.make_move(0, 1, p2)

    system.make_move(1, 1, p1)
    system.make_move(0, 2, p2)

    system.make_move(2, 2, p1)

    system.print_scoreboard()


# --------------------------------------------------
# Scenario 4: Invalid Turn
# --------------------------------------------------
def test_invalid_turn():
    system = TicTacToeSystem()

    p1, p2 = create_players()

    system.create_game(p1, p2)

    system.make_move(0, 0, p1)

    # Rahul's turn but Atharv tries again
    system.make_move(0, 1, p1)


# --------------------------------------------------
# Scenario 5: Occupied Cell
# --------------------------------------------------
def test_occupied_cell():
    system = TicTacToeSystem()

    p1, p2 = create_players()

    system.create_game(p1, p2)

    system.make_move(0, 0, p1)

    # Same cell
    system.make_move(0, 0, p2)


# --------------------------------------------------
# Scenario 6: Out Of Bounds
# --------------------------------------------------
def test_out_of_bounds():
    system = TicTacToeSystem()

    p1, p2 = create_players()

    system.create_game(p1, p2)

    system.make_move(10, 10, p1)


# --------------------------------------------------
# Scenario 7: Move After Game Ends
# --------------------------------------------------
def test_move_after_game_end():
    system = TicTacToeSystem()

    p1, p2 = create_players()

    system.create_game(p1, p2)

    system.make_move(0, 0, p1)
    system.make_move(1, 0, p2)

    system.make_move(0, 1, p1)
    system.make_move(1, 1, p2)

    system.make_move(0, 2, p1)

    # Game already won
    system.make_move(2, 2, p2)


# --------------------------------------------------
# Scenario 8: Draw
# --------------------------------------------------
def test_draw():
    system = TicTacToeSystem()

    p1, p2 = create_players()

    system.create_game(p1, p2)

    system.make_move(0, 0, p1)
    system.make_move(0, 1, p2)

    system.make_move(0, 2, p1)
    system.make_move(1, 1, p2)

    system.make_move(1, 0, p1)
    system.make_move(1, 2, p2)

    system.make_move(2, 1, p1)
    system.make_move(2, 0, p2)

    system.make_move(2, 2, p1)

    system.print_scoreboard()


def main():

    run_scenario("ROW WIN", test_row_win)

    run_scenario("COLUMN WIN", test_column_win)

    run_scenario("DIAGONAL WIN", test_diagonal_win)

    run_scenario("INVALID TURN", test_invalid_turn)

    run_scenario("OCCUPIED CELL", test_occupied_cell)

    run_scenario("OUT OF BOUNDS", test_out_of_bounds)

    run_scenario("MOVE AFTER GAME END", test_move_after_game_end)

    run_scenario("DRAW GAME", test_draw)


if __name__ == "__main__":
    main()