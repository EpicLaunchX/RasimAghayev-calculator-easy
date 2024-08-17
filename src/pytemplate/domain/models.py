from dataclasses import dataclass


@dataclass
class Operands:
    def __init__(self, first_operand: int, second_operand: int):
        self.first_operand = first_operand
        self.second_operand = second_operand

    def __repr__(self):
        return f"Operands({self.first_operand}, {self.second_operand})"


def operands_factory(first_operand: int, second_operand: int) -> Operands:
    return Operands(first_operand, second_operand)
