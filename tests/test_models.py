import pytest

from src.pytemplate.domain.models import Operands, operands_factory


def test_operands_factory():
    # Test creating Operands object with positive integers
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


def test_operands_factory_type_error():
    # Test creating Operands object with invalid types
    with pytest.raises(TypeError, match="Both arguments must be integers."):
        operands_factory("string", 5)

    with pytest.raises(TypeError, match="Both arguments must be integers."):
        operands_factory(3, "string")

    with pytest.raises(TypeError, match="Both arguments must be integers."):
        operands_factory("string", "string")

    with pytest.raises(TypeError):
        operands_factory(3, 5.5)

    with pytest.raises(TypeError):
        operands_factory(3.5, 5)

    with pytest.raises(TypeError):
        operands_factory(3.5, 5.5)
