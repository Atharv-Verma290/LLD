from enumerations import Symbol

class Cell:
    def __init__(self, symbol: Symbol = Symbol.EMPTY) -> None:
        self.symbol = symbol

    def is_empty(self) -> bool:
        return self.symbol == Symbol.EMPTY 