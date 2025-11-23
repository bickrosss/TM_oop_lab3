#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
from math import pi
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'tasks'))

from figure_package import Figure, Rectangle, Circle, Trapezium

class TestValidation:
    def test_rectangle_validation(self):
        """Тест валидации прямоугольника"""
        # Корректный прямоугольник
        rect = Rectangle(5, 3)
        assert rect.is_valid() == True
        
        # Некорректный прямоугольник
        with pytest.raises(ValueError):
            Rectangle(-1, 5)
        
        with pytest.raises(ValueError):
            Rectangle(0, 5)
    
    def test_circle_validation(self):
        """Тест валидации круга"""
        # Корректный круг
        circle = Circle(5)
        assert circle.is_valid() == True
        
        # Некорректный круг
        with pytest.raises(ValueError):
            Circle(-1)
        
        with pytest.raises(ValueError):
            Circle(0)
    
    def test_trapezium_validation(self):
        """Тест валидации трапеции"""
        # Корректная трапеция
        trap = Trapezium(6, 4, 3, 2, 2)
        assert trap.is_valid() == True
        
        # Некорректная трапеция (отрицательные значения)
        with pytest.raises(ValueError):
            Trapezium(-1, 4, 3, 2, 2)
        
        # Некорректная трапеция (невозможная геометрия)
        with pytest.raises(ValueError):
            Trapezium(10, 1, 2, 1, 1)  # разность оснований 9 > суммы боковых 2
    
    def test_trapezium_edge_cases(self):
        """Тест граничных случаев для трапеции"""
        # Граничный случай - равнобедренная трапеция
        trap = Trapezium(5, 3, 4, 2.5, 2.5)
        assert trap.is_valid() == True
        
        # Невозможный случай
        with pytest.raises(ValueError):
            Trapezium(8, 2, 3, 2, 2)  # 6 > 4

def test_abstract_method_implementation():
    """Тест, что все классы реализуют абстрактные методы"""
    rect = Rectangle(1, 1)
    circle = Circle(1)
    trap = Trapezium(3, 2, 1, 1, 1)
    
    # Проверка, что все методы работают
    assert rect.area() == 1
    assert circle.area() == pi
    assert trap.area() == 2.5
    
    assert rect.perimeter() == 4
    assert abs(circle.perimeter() - 2 * pi) < 0.001
    assert trap.perimeter() == 7
    
    # Проверка валидации
    assert rect.is_valid() == True
    assert circle.is_valid() == True
    assert trap.is_valid() == True