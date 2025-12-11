#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import pytest

from figure_package.figure import Figure, Rectangle, Circle, Trapezium, Reader


class TestRectangle:

    def test_create_rectangle(self):
        rect = Rectangle(2.0, 3.0)
        assert rect.width == 2.0
        assert rect.height == 3.0

    def test_area(self):
        rect = Rectangle(4.0, 5.0)
        assert rect.area() == 20.0

    def test_perimeter(self):
        rect = Rectangle(3.0, 4.0)
        assert rect.perimeter() == 14.0

    def test_setter_validation(self):
        rect = Rectangle(1.0, 1.0)
        
        rect.width = 2.0
        rect.height = 3.0
        
        with pytest.raises(ValueError, match="Ширина должна быть положительной"):
            rect.width = 0
        
        with pytest.raises(ValueError, match="Высота должна быть положительной"):
            rect.height = -1.0

    def test_str_representation(self):
        rect = Rectangle(2.0, 3.0)
        result = str(rect)
        assert "Прямоугольник" in result
        assert "Ширина: 2.0" in result
        assert "Высота: 3.0" in result
        assert "Площадь: 6.00" in result
        assert "Периметр: 10.00" in result


class TestCircle:

    def test_create_circle(self):

        circle = Circle(5.0)
        assert circle.radius == 5.0

    def test_area(self):
        circle = Circle(3.0)
        expected_area = math.pi * 9.0
        assert circle.area() == expected_area

    def test_perimeter(self):
        circle = Circle(2.0)
        expected_perimeter = 2 * math.pi * 2.0
        assert circle.perimeter() == expected_perimeter

    def test_setter_validation(self):

        circle = Circle(1.0)
        
        circle.radius = 2.0
        
        with pytest.raises(ValueError, match="Радиус должен быть положительным"):
            circle.radius = 0

    def test_str_representation(self):

        circle = Circle(2.0)
        result = str(circle)
        assert "Круг" in result
        assert "Радиус: 2.0" in result
        assert f"Площадь: {math.pi * 4:.2f}" in result
        assert f"Периметр (длина окружности): {2 * math.pi * 2:.2f}" in result


class TestTrapezium:

    def test_create_trapezium(self):

        trap = Trapezium(6.0, 4.0, 3.0, 5.0, 2.0)
        assert trap.base1 == 6.0
        assert trap.base2 == 4.0
        assert trap.side1 == 3.0
        assert trap.side2 == 5.0
        assert trap.height == 2.0

    def test_area(self):
        trap = Trapezium(5.0, 3.0, 4.0, 4.0, 4.0)
        expected_area = (5.0 + 3.0) * 4.0 / 2
        assert trap.area() == expected_area

    def test_perimeter(self):
        trap = Trapezium(5.0, 3.0, 2.0, 2.0, 4.0)
        expected_perimeter = 5.0 + 3.0 + 2.0 + 2.0
        assert trap.perimeter() == expected_perimeter

    def test_setter_validation(self):

        trap = Trapezium(3.0, 2.0, 2.0, 2.0, 1.0)
   
        trap.base1 = 4.0
        trap.base2 = 3.0
        trap.side1 = 2.5
        trap.side2 = 2.5
        trap.height = 2.0
        
        with pytest.raises(ValueError, match="Основание должно быть положительным"):
            trap.base1 = 0
        
        with pytest.raises(ValueError, match="Основание должно быть положительным"):
            trap.base2 = -1.0
            
        with pytest.raises(ValueError, match="Боковая сторона должна быть положительной"):
            trap.side1 = 0
            
        with pytest.raises(ValueError, match="Боковая сторона должна быть положительной"):
            trap.side2 = -1.0
            
        with pytest.raises(ValueError, match="Высота должна быть положительной"):
            trap.height = 0

    def test_str_representation(self):
        trap = Trapezium(5.0, 3.0, 4.0, 4.0, 4.0)
        result = str(trap)
        assert "Трапеция" in result
        assert "Верхнее основание: 5.0" in result
        assert "Нижнее основание: 3.0" in result
        assert "Боковая сторона 1: 4.0" in result
        assert "Боковая сторона 2: 4.0" in result
        assert "Высота: 4.0" in result
        assert "Площадь: 16.00" in result
        assert "Периметр: 16.00" in result


class TestReader:

    def test_read_float_valid(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "3.14")
        result = Reader.read_float("Введите число: ")
        assert result == 3.14

    def test_read_float_decimal(self, monkeypatch):
        """Тест чтения float с десятичной запятой"""
        monkeypatch.setattr('builtins.input', lambda _: "2.5")
        result = Reader.read_float("Введите число: ")
        assert result == 2.5

    def test_read_float_integer(self, monkeypatch):

        monkeypatch.setattr('builtins.input', lambda _: "42")
        result = Reader.read_float("Введите число: ")
        assert result == 42.0


class TestInheritanceAndAbstract:

    def test_inheritance(self):
        rect = Rectangle(1.0, 1.0)
        circle = Circle(1.0)
        trap = Trapezium(3.0, 2.0, 2.0, 2.0, 1.0)

        assert isinstance(rect, Figure)
        assert isinstance(circle, Figure)
        assert isinstance(trap, Figure)

    def test_abstract_methods_implementation(self):
        """Тест реализации абстрактных методов"""
        rect = Rectangle(1.0, 1.0)
        circle = Circle(1.0)
        trap = Trapezium(3.0, 2.0, 2.0, 2.0, 1.0)

        assert isinstance(rect.area(), (int, float))
        assert isinstance(rect.perimeter(), (int, float))
        assert isinstance(str(rect), str)
        
        assert isinstance(circle.area(), (int, float))
        assert isinstance(circle.perimeter(), (int, float))
        assert isinstance(str(circle), str)
        
        assert isinstance(trap.area(), (int, float))
        assert isinstance(trap.perimeter(), (int, float))
        assert isinstance(str(trap), str)


def test_multiple_objects():
    """Тест работы с несколькими объектами"""
    rect1 = Rectangle(2.0, 3.0)
    rect2 = Rectangle(4.0, 5.0)

    circle1 = Circle(2.0)
    circle2 = Circle(3.0)

    trap1 = Trapezium(5.0, 3.0, 2.0, 2.0, 4.0)
    trap2 = Trapezium(6.0, 4.0, 2.0, 2.0, 3.0)

    assert rect1.area() == 6.0
    assert rect2.area() == 20.0

    assert circle1.area() == math.pi * 4.0
    assert circle2.area() == math.pi * 9.0

    assert trap1.area() == 16.0
    assert trap2.area() == 15.0


def test_edge_cases():
    rect_small = Rectangle(0.1, 0.1)
    assert rect_small.area() > 0

    rect_square = Rectangle(2.0, 2.0)
    assert rect_square.perimeter() == 8.0

    circle = Circle(0.0001)
    assert circle.area() > 0


def test_calculation_accuracy():
    rect = Rectangle(2.0, 3.0)
    assert rect.area() == 6.0
    assert rect.perimeter() == 10.0

    circle = Circle(1.0)
    assert abs(circle.area() - math.pi) < 0.001
    assert abs(circle.perimeter() - 2 * math.pi) < 0.001

    trap = Trapezium(4.0, 2.0, 3.0, 3.0, 3.0)
    assert trap.area() == 9.0


@pytest.fixture
def sample_rectangle():
    return Rectangle(3.0, 4.0)


@pytest.fixture
def sample_circle():
    return Circle(2.0)


@pytest.fixture
def sample_trapezium():
    return Trapezium(5.0, 3.0, 3.0, 3.0, 4.0)


def test_with_fixtures(sample_rectangle, sample_circle, sample_trapezium):

    assert sample_rectangle.area() == 12.0
    assert sample_circle.area() == math.pi * 4.0
    assert sample_trapezium.area() == 16.0


def test_property_access():
    rect = Rectangle(2.0, 3.0)
    assert rect.width == 2.0
    assert rect.height == 3.0
    
    circle = Circle(5.0)
    assert circle.radius == 5.0
    
    trap = Trapezium(6.0, 4.0, 3.0, 5.0, 2.0)
    assert trap.base1 == 6.0
    assert trap.base2 == 4.0
    assert trap.side1 == 3.0
    assert trap.side2 == 5.0
    assert trap.height == 2.0