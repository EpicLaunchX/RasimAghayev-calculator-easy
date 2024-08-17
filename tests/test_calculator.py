import pytest

from src.pytemplate.domain.models import operands_factory
from src.pytemplate.service.calculator import Calculator


def test_add():
    calc = Calculator()
    operands = operands_factory(45, 35)
    assert calc.add(operands) == 80


def test_subtract():
    calc = Calculator()
    operands = operands_factory(45, 35)
    assert calc.subtract(operands) == 10


def test_multiply():
    calc = Calculator()
    operands = operands_factory(45, 35)
    assert calc.multiply(operands) == 1575


def test_divide():
    calc = Calculator()
    operands = operands_factory(45, 15)
    assert calc.divide(operands) == 3


def test_divide_by_zero():
    calc = Calculator()
    operands = operands_factory(45, 0)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.divide(operands)
