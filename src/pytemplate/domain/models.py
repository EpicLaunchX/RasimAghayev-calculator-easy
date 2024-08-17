from dataclasses import dataclass


@dataclass
class Operands:
    first_operand: int
    second_operand: int

    def __post_init__(self):
        if not isinstance(self.first_operand, int) or not isinstance(self.second_operand, int):
            raise TypeError("Both operands must be of type int")
