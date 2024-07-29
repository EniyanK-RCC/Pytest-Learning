import pytest
from app import Calculator

calc = Calculator()

@pytest.mark.addition
def test_addition(num1, num2):
    assert calc.add(num1, num2) == num1 + num2

@pytest.mark.subtraction
def test_subtraction(num1, num2):
    assert calc.sub(num1, num2) == num1 - num2

@pytest.mark.multiplication
def test_multiplication(num1, num2):
    assert calc.mul(num1, num2) == num1 * num2

@pytest.mark.division
def test_division(num1, num2):
    if num2 == 0:
        with pytest.raises(ValueError, match="Value cannot be divided by zero"):
            calc.div(num1, num2)
    assert calc.div(num1, num2) == num1 / num2