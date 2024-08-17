import pytest

from src.pytemplate.domain.models import Operands, operands_factory


def test_operands_factory():
    # Test that the function returns an Operands object with correct values
    result = operands_factory(3, 5)
    assert isinstance(result, Operands)
    assert result.first_operand == 3
    assert result.second_operand == 5

    # Test with different integer values
    result = operands_factory(-10, 20)
    assert isinstance(result, Operands)
    assert result.first_operand == -10
    assert result.second_operand == 20

    # Test with zero values
    result = operands_factory(0, 0)
    assert isinstance(result, Operands)
    assert result.first_operand == 0
    assert result.second_operand == 0
