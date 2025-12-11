#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
from pair import Pair, Long


class TestPair:
    
    def test_create_pair(self):
        pair = Pair(10, 20)
        assert pair.get_first() == 10
        assert pair.get_second() == 20
    
    def test_setters_getters(self):
        pair = Pair()
        pair.set_first(5)
        pair.set_second(15)
        assert pair.get_first() == 5
        assert pair.get_second() == 15
    
    def test_add_method(self):
        pair1 = Pair(10, 20)
        pair2 = Pair(30, 40)
        result = pair1.add(pair2)
        assert result.get_first() == 30
        assert result.get_second() == 70
    
    def test_add_operator(self):
        pair1 = Pair(10, 20)
        pair2 = Pair(30, 40)
        result = pair1 + pair2
        assert result.get_first() == 30
        assert result.get_second() == 70
    
    def test_str_representation(self):
        pair = Pair(10, 20)
        assert str(pair) == "(10, 20)"
    
    def test_default_values(self):
        pair = Pair()
        assert pair.get_first() == 0
        assert pair.get_second() == 0


class TestLong:
    
    def test_create_long(self):
        long_num = Long(1, 500)
        assert long_num.high == 1
        assert long_num.low == 500
    
    def test_properties(self):
        long_num = Long()
        long_num.high = 2
        long_num.low = 750
        assert long_num.high == 2
        assert long_num.low == 750
        assert long_num.first == 2
        assert long_num.second == 750
    
    def test_add_without_carry(self):
        num1 = Long(1, 200)
        num2 = Long(2, 300)
        result = num1.add(num2)
        assert result.high == 3
        assert result.low == 500
    
    def test_add_with_carry(self):
        num1 = Long(1, 800)
        num2 = Long(2, 400)
        result = num1.add(num2)
        assert result.high == 4
        assert result.low == 200
    
    def test_add_with_large_carry(self):
        num1 = Long(0, 900)
        num2 = Long(0, 900)
        result = num1.add(num2)
        assert result.high == 1
        assert result.low == 800
    
    def test_add_operator(self):
        num1 = Long(1, 500)
        num2 = Long(2, 600)
        result = num1 + num2
        assert result.high == 4
        assert result.low == 100
    
    def test_multiply_small_numbers(self):
        num1 = Long(0, 5)
        num2 = Long(0, 4)
        result = num1.multiply(num2)
        assert result.high == 0
        assert result.low == 20
    
    def test_multiply_with_carry(self):
        num1 = Long(0, 500)
        num2 = Long(0, 3)
        result = num1.multiply(num2)
        assert result.high == 1
        assert result.low == 500
    
    def test_multiply_large_numbers(self):
        num1 = Long(2, 500)
        num2 = Long(1, 200)
        result = num1.multiply(num2)
        assert result.high == 3000
        assert result.low == 0
    
    def test_multiply_operator(self):
        num1 = Long(1, 100)
        num2 = Long(0, 5)
        result = num1 * num2
        assert result.high == 5
        assert result.low == 500
    
    def test_subtract_simple(self):
        num1 = Long(3, 500)
        num2 = Long(1, 200)
        result = num1.subtract(num2)
        assert result.high == 2
        assert result.low == 300
    
    def test_subtract_with_borrow(self):
        num1 = Long(2, 300)
        num2 = Long(1, 500)
        result = num1.subtract(num2)
        assert result.high == 0
        assert result.low == 800
    
    def test_subtract_negative_result(self):
        num1 = Long(1, 200)
        num2 = Long(2, 500)
        with pytest.raises(ValueError, match="Результат не может быть отрицательным"):
            num1.subtract(num2)
    
    def test_subtract_operator(self):
        num1 = Long(5, 700)
        num2 = Long(2, 300)
        result = num1 - num2
        assert result.high == 3
        assert result.low == 400
    
    def test_str_representation(self):
        num1 = Long(1, 23)
        assert str(num1) == "1.023"
        num2 = Long(0, 500)
        assert str(num2) == "0.500"
        num3 = Long(10, 5)
        assert str(num3) == "10.005"
    
    def test_inheritance(self):
        long_num = Long(1, 500)
        assert isinstance(long_num, Pair)
        long_num.set_first(2)
        long_num.set_second(700)
        assert long_num.get_first() == 2
        assert long_num.get_second() == 700


def test_edge_cases():
    num1 = Long(0, 999)
    num2 = Long(0, 1)
    result = num1 + num2
    assert result.high == 1
    assert result.low == 0
    
    num1 = Long(5, 500)
    num2 = Long(0, 0)
    result = num1 * num2
    assert result.high == 0
    assert result.low == 0
    
    num1 = Long(3, 200)
    num2 = Long(3, 200)
    result = num1 - num2
    assert result.high == 0
    assert result.low == 0


@pytest.fixture
def sample_long_small():
    return Long(0, 100)


@pytest.fixture
def sample_long_medium():
    return Long(1, 500)


@pytest.fixture
def sample_long_large():
    return Long(5, 750)


def test_with_fixtures(sample_long_small, sample_long_medium, sample_long_large):
    result1 = sample_long_small + sample_long_medium
    assert result1.high == 1
    assert result1.low == 600
    
    result2 = sample_long_medium * sample_long_small
    assert result2.high == 150
    assert result2.low == 0
    
    result3 = sample_long_large - sample_long_medium
    assert result3.high == 4
    assert result3.low == 250


def test_base_property():
    assert Long.BASE == 1000
    assert Pair.BASE == 1000
    
    num1 = Long(0, Long.BASE - 1)
    num2 = Long(0, 1)
    result = num1 + num2
    assert result.high == 1
    assert result.low == 0