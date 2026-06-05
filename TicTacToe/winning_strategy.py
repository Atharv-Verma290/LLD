from abc import ABC, abstractmethod
from board import Board
from enumerations import Symbol

class WinningStrategy(ABC):
    @abstractmethod
    def check_win(self, board: Board, row: int, col: int, symbol: Symbol) -> bool:
        pass


class RowStrategy(WinningStrategy):
    def check_win(self, board: Board, row: int, col: int, symbol: Symbol) -> bool:
        row_in_question = board.grid[row]
        symbol_count = 0
        for cell in row_in_question:
            if cell.symbol == symbol:
                symbol_count += 1
        
        return symbol_count == board.size
        

class ColumnStrategy(WinningStrategy):
    def check_win(self, board: Board, row: int, col: int, symbol: Symbol) -> bool:
        col_in_question = [row[col] for row in board.grid]
        symbol_count = 0
        for cell in col_in_question:
            if cell.symbol == symbol:
                symbol_count += 1
        
        return symbol_count == board.size


class DiagonalStrategy(WinningStrategy):
    def check_win(self, board: Board, row: int, col: int, symbol: Symbol) -> bool:
        if row != col and row + col != board.size - 1:
            return False
        
        if row == col:
            main_diagonal = [board.grid[i][i] for i in range(board.size)]   
            symbol_count = 0
            for cell in main_diagonal:
                if cell.symbol == symbol:
                    symbol_count += 1
            
        else:
            anti_diagonal = [board.grid[i][board.size - 1 - i] for i in range(board.size)]
            symbol_count = 0
            for cell in anti_diagonal:
                if cell.symbol == symbol:
                    symbol_count += 1
        
        return symbol_count == board.size