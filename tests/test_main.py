#!/usr/bin/env python
# -*- coding: utf-8 -*-
from simple_calculator.main import SimpleCalculator

def test_add_two_numbers():
    calculator = SimpleCalculator()

    result = calculator.add(2, 3)
    assert result == 5

def test_add_many_numbers():
    calculator = SimpleCalculator()

    numbers = range(100)
    result = calculator.add(*numbers)
    assert result == 4950




