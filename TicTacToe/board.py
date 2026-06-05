from cell import Cell
from typing import List
from enumerations import Symbol

class Board:
    def __init__(self, size: int = 3) -> None:
        self.size = size 
        self.grid: List[List[Cell]] = [[Cell() for _ in range(size)] for _ in range(size)]

    def is_full(self) -> bool:
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j].is_empty():
                    return False
        return True

    def print_board(self) -> None:
        for i, row in enumerate(self.grid):
            print(" | ".join(cell.symbol.value for cell in row))

            if i < self.size - 1:
                print("-" * (self.size * 4 - 3))

        print()

    def place_symbol(self, row: int, col: int, symbol: Symbol) -> None:
        if not (0 <= row < self.size and 0 <= col < self.size):
            raise ValueError(f"Row {row} and Col {col} must be between 0 and {self.size - 1}!")

        if symbol == Symbol.EMPTY:
            raise ValueError("Empty symbol cannot be placed on the board!")
        
        cell = self.grid[row][col]
        if cell.is_empty():
            cell.symbol = symbol
            print(f"Symbol {symbol} placed on Cell ({row}, {col}) successfully.")
        else: 
            raise ValueError(f"Cell ({row}, {col}) is already occupied!")

    