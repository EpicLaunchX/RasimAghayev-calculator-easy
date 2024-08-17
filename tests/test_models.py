import pytest

from src.pytemplate.domain.models import Operands


def test_operands_creation():
    operands = Operands(first_operand=5, second_operand=10)
    assert operands.first_operand == 5
    assert operands.second_operand == 10


def test_operands_type():
    operands = Operands(first_operand=5, second_operand=10)
    assert isinstance(operands.first_operand, int)
    assert isinstance(operands.second_operand, int)


def test_operands_invalid_type():
    with pytest.raises(TypeError):
        Operands(first_operand="5", second_operand="10")
