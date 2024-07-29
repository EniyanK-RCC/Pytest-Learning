import pytest

@pytest.mark.addition
def test_addition(calc, num1, num2):
    assert calc.add(num1, num2) == num1 + num2

@pytest.mark.subtraction
def test_subtraction(calc, num1, num2):
    assert calc.sub(num1, num2) == num1 - num2

@pytest.mark.multiplication
def test_multiplication(calc, num1, num2):
    assert calc.mul(num1, num2) == num1 * num2

@pytest.mark.division
def test_division(calc, num1, num2):
    if num2 == 0:
        with pytest.raises(ValueError, match="Value cannot be divided by zero"):
            calc.div(num1, num2)
    assert calc.div(num1, num2) == num1 / num2