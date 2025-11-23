#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
from math import pi
from figure_package import Figure, Rectangle, Circle, Trapezium, Reader, demonstrate_virtual_call

class TestReader:
    def test_read_float(self, monkeypatch):
        """Тест чтения float через Reader"""
        monkeypatch.setattr('builtins.input', lambda _: "3.14")
        result = Reader.read_float("Введите число: ")
        assert result == 3.14
    
    def test_read_int(self, monkeypatch):
        """Тест чтения int через Reader"""
        monkeypatch.setattr('builtins.input', lambda _: "42")
        result = Reader.read_int("Введите число: ")
        assert result == 42

class TestRectangle:
    def test_rectangle_creation(self):
        """Тест создания прямоугольника"""
        rect = Rectangle(5, 3)
        assert rect.width == 5
        assert rect.height == 3
        assert rect.name == "Прямоугольник"
    
    def test_rectangle_area(self):
        """Тест вычисления площади прямоугольника"""
        rect = Rectangle(4, 6)
        assert rect.area() == 24
    
    def test_rectangle_perimeter(self):
        """Тест вычисления периметра прямоугольника"""
        rect = Rectangle(4, 6)
        assert rect.perimeter() == 20

class TestCircle:
    def test_circle_creation(self):
        """Тест создания круга"""
        circle = Circle(5)
        assert circle.radius == 5
        assert circle.name == "Круг"
    
    def test_circle_area(self):
        """Тест вычисления площади круга"""
        circle = Circle(2)
        assert abs(circle.area() - 4 * pi) < 0.001
    
    def test_circle_perimeter(self):
        """Тест вычисления периметра круга"""
        circle = Circle(3)
        assert abs(circle.perimeter() - 6 * pi) < 0.001

class TestTrapezium:
    def test_trapezium_creation(self):
        """Тест создания трапеции"""
        trap = Trapezium(6, 4, 3, 2, 2)
        assert trap.base1 == 6
        assert trap.base2 == 4
        assert trap.height == 3
        assert trap.side1 == 2
        assert trap.side2 == 2
    
    def test_trapezium_area(self):
        """Тест вычисления площади трапеции"""
        trap = Trapezium(8, 4, 3, 0, 0)
        assert trap.area() == 18  # (8+4)*3/2 = 18
    
    def test_trapezium_perimeter(self):
        """Тест вычисления периметра трапеции"""
        trap = Trapezium(8, 4, 3, 2, 2)
        assert trap.perimeter() == 16  # 8+4+2+2 = 16

def test_polymorphism():
    """Тест полиморфизма"""
    figures = [
        Rectangle(2, 3),
        Circle(1),
        Trapezium(4, 2, 3, 1, 1)
    ]
    
    # Все фигуры должны иметь методы area и perimeter
    areas = [fig.area() for fig in figures]
    perimeters = [fig.perimeter() for fig in figures]
    
    assert len(areas) == 3
    assert len(perimeters) == 3
    
    # Проверка конкретных значений
    assert areas[0] == 6  # прямоугольник
    assert abs(areas[1] - pi) < 0.001  # круг
    assert areas[2] == 9  # трапеция

if __name__ == '__main__':
    pytest.main([__file__, "-v"])
