from enumerations import Symbol


class Player:
    def __init__(self, name) -> None:
        self.name = name 
        self.assigned_symbol = Symbol.EMPTY

    def assign_symbol(self, symbol: Symbol) -> None:
        if symbol == Symbol.EMPTY:
            raise ValueError(f"Cannot assign {symbol} to a Player!")
        if self.assigned_symbol == Symbol.EMPTY:
            self.assigned_symbol = symbol 
            print(f"Successfully assigned {self.assigned_symbol} to Player {self.name}!")
        else:
            raise ValueError(f"Player {self.name} have already been assigned symbol {self.assigned_symbol}!")