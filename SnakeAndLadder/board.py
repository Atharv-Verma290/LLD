from typing import Dict, List, Optional

from board_entity import BoardEntity

class Board:
    def __init__(self, size: int, entities: List[BoardEntity]) -> None:
        self.size = size 
        self.snake_and_ladders: Dict[int, int] = {}

        for entity in entities:
            if not (1 <= entity.start <= size) or not (1 <= entity.end <= size):
                raise ValueError(f"Entity positions must be within 1 and {size}!")
            
            if entity.start in self.snake_and_ladders:
                raise ValueError(f"Two entities cannot share the same start position: {entity.start}!")
            
            self.snake_and_ladders[entity.start] = entity.end 

    def get_final_position(self, position: int) -> int:
        return self.snake_and_ladders.get(position, position)
    

