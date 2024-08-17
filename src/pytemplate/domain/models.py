from dataclasses import dataclass


@dataclass
class Operands:
    first_operand: int
    second_operand: int


def operands_factory(first_operand: int, second_operand: int) -> Operands:
    """
    Factory function to create an instance of Operands.

    Parameters:
    first_operand (int): The first operand.
    second_operand (int): The second operand.

    Returns:
    Operands: An instance of the Operands class.
    """
    if not isinstance(first_operand, int) or not isinstance(second_operand, int):
        raise TypeError("Both arguments must be integers.")

    return Operands(first_operand, second_operand)
