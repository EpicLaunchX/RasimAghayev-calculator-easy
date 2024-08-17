from dataclasses import dataclass


@dataclass
class Operands:
    first_operand: int
    second_operand: int

    def __post_init__(self):
        if not isinstance(self.first_operand, int) or not isinstance(self.second_operand, int):
            raise TypeError("Both arguments must be integers.")


def operands_factory(first_operand: int, second_operand: int) -> Operands:
    """
    Factory function to create an instance of Operands.

    Parameters:
    first_operand (int): The first operand.
    second_operand (int): The second operand.

    Returns:
    Operands: An instance of the Operands class.
    """
    return Operands(first_operand, second_operand)
