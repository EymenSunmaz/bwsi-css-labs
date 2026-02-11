"""
tests_1b.py

This module contains unit tests for the simple_calculator function defined in lab_1b.py.
"""

import pytest
def simple_calculator(operation: str, num1: float, num2: float) -> float:
    """
    Function that takes in two numbers and an operation (add, subtract, multiply, divide),
    then performs the operation on the two numbers and returns the result.

    Args:
        operation (str): The operation to perform ("add", "subtract", "multiply", "divide").
        num1 (float): The first number.
        num2 (float): The second number.

    Returns:
        float: The result of the operation.
    """
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 != 0:
            return num1 / num2
        else:
            raise ValueError("Cannot divide by zero.")
    else:
        raise ValueError("Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide'.")


def test_addition():
    assert simple_calculator("add", 5, 3) == 8          # Test for positive numbers
    assert simple_calculator("add", -2, 2) == 0         # Test for negative and positive number
    assert simple_calculator("add", 0, 0) == 0          # Test for zero addition

def test_subtraction():
    assert simple_calculator("subtract", 5, 3) == 2     # Test for positive numbers
    assert simple_calculator("subtract", -2, -2) == 0   # Test for negative numbers
    assert simple_calculator("subtract", 0, 5) == -5    # Test for zero minuend

def test_multiplication():
    assert simple_calculator("multiply", 5, 3) == 15    # Test for positive numbers
    assert simple_calculator("multiply", -2, 2) == -4   # Test for negative and positive number
    assert simple_calculator("multiply", 0, 100) == 0   # Test for multiplication by zero

def test_division():
    assert simple_calculator("divide", 6, 3) == 2       # Test for positive numbers
    assert simple_calculator("divide", -4, 2) == -2     # Test for negative and positive number
    assert simple_calculator("divide", 5, 2) == 2.5     # Test for division resulting in float

def test_division_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        simple_calculator("divide", 5, 0)               # Test division by zero

def test_invalid_operation():
    with pytest.raises(ValueError, match="Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide'."):
        simple_calculator("modulus", 5, 3)              # Test for invalid operation
    with pytest.raises(ValueError, match="Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide'."):
        simple_calculator("", 5, 3)                     # Test for empty operation

if __name__ == "__main__":
    pytest.main()