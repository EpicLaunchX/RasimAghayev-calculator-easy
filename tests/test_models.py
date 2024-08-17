import pytest

from src.pytemplate.domain.models import Operands, operands_factory


def test_operands_factory():
    # Test creating Operands object with valid integers
    result = operands_factory(3, 5)
    assert isinstance(result, Operands)
    assert result.first_operand == 3
    assert result.second_operand == 5

    # Test creating Operands object with negative integers
    result = operands_factory(-10, 20)
    assert isinstance(result, Operands)
    assert result.first_operand == -10
    assert result.second_operand == 20

    # Test creating Operands object with zero values
    result = operands_factory(0, 0)
    assert isinstance(result, Operands)
    assert result.first_operand == 0
    assert result.second_operand == 0


def test_operands_repr():
    # Test the __repr__ method of Operands
    obj = Operands(7, 8)
    assert repr(obj) == "Operands(first_operand=7, second_operand=8)"
