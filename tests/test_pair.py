import pytest
from pair import Pair, Long


class TestPair:
    def test_pair_creation(self):
        """Тест создания объекта Pair"""
        p = Pair(10, 20)
        assert p.first == 10
        assert p.second == 20
    
    def test_pair_addition(self):
        """Тест сложения пар"""
        p1 = Pair(10, 20)
        p2 = Pair(5, 15)
        result = p1 + p2
        assert result.first == 15
        assert result.second == 35
    
    def test_pair_setters(self):
        """Тест сеттеров Pair"""
        p = Pair()
        p.first = 100
        p.second = 200
        assert p.first == 100
        assert p.second == 200
    
    def test_pair_string_representation(self):
        """Тест строкового представления Pair"""
        p = Pair(7, 13)
        assert str(p) == "(7, 13)"
    
    def test_pair_add_with_invalid_type(self):
        """Тест сложения с неверным типом"""
        p = Pair(1, 2)
        with pytest.raises(ValueError):
            p + "invalid"


class TestLong:
    def test_long_creation(self):
        """Тест создания объекта Long"""
        l = Long(2, 500)
        assert l.high == 2
        assert l.low == 500
    
    def test_long_inheritance(self):
        """Тест наследования Long от Pair"""
        l = Long(1, 500)
        assert isinstance(l, Pair)
    
    def test_long_addition_no_overflow(self):
        """Тест сложения Long чисел без переполнения"""
        l1 = Long(1, 200)
        l2 = Long(1, 300)
        result = l1 + l2
        assert result.high == 2
        assert result.low == 500
    
    def test_long_addition_with_overflow(self):
        """Тест сложения Long чисел с переполнением"""
        l1 = Long(1, 800)
        l2 = Long(1, 300)
        result = l1 + l2
        assert result.high == 3
        assert result.low == 100
    
    def test_long_multiplication(self):
        """Тест умножения Long чисел"""
        l1 = Long(2, 100)
        l2 = Long(1, 200)
        result = l1 * l2
        assert result.high == 22  # 2 + 20
        assert result.low == 0
    
    def test_long_subtraction(self):
        """Тест вычитания Long чисел"""
        l1 = Long(3, 200)
        l2 = Long(1, 500)
        result = l1 - l2
        assert result.high == 1
        assert result.low == 700
    
    def test_long_subtraction_with_borrow(self):
        """Тест вычитания Long чисел с заимствованием"""
        l1 = Long(2, 300)
        l2 = Long(1, 500)
        result = l1 - l2
        assert result.high == 0
        assert result.low == 800
    
    def test_long_add_with_invalid_type(self):
        """Тест сложения Long с неверным типом"""
        l = Long(1, 2)
        with pytest.raises(ValueError):
            l + "invalid"
    
    def test_long_multiply_with_invalid_type(self):
        """Тест умножения Long с неверным типом"""
        l = Long(1, 2)
        with pytest.raises(ValueError):
            l * "invalid"
    
    def test_long_subtract_with_invalid_type(self):
        """Тест вычитания Long с неверным типом"""
        l = Long(1, 2)
        with pytest.raises(ValueError):
            l - "invalid"


def test_gcd_function():
    """Тест импортированной функции gcd"""
    from math import gcd
    assert gcd(12, 18) == 6
    assert gcd(17, 13) == 1
    assert gcd(100, 25) == 25


if __name__ == '__main__':
    pytest.main([__file__, "-v"])
