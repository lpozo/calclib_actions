"""
Unit tests for the calculator library
"""

import calclib.calclib as calc


class TestCalculator:

    def test_addition(self):
        assert 4 == calc.add(2, 2)

    def test_subtraction(self):
        assert 2 == calc.subtract(4, 2)

    def test_multiplication(self):
        assert 8 == calc.multiply(4, 2)

    def test_division(self):
        assert 2 == calc.divide(4, 2)
