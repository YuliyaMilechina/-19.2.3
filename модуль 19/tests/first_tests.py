import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculator_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_division_calculator_correctly(self):
        assert self.calc.division(self, 3, 3) == 1

    def test_subtraction_calculator_correctly(self):
        assert self.calc.subtraction(self, 5, 5) == 0

    def test_adding_calculator_correctly(self):
        assert self.calc.adding(self, 6, 6) == 12










