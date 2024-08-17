from dataclasses import dataclass


@dataclass
class Operands:
    first_operand: int
    second_operand: int

    def __repr__(self):
        return f"Operands(first_operand={self.first_operand}, second_operand={self.second_operand})"


def operands_factory(first_operand: int, second_operand: int) -> Operands:
    return Operands(first_operand, second_operand)
