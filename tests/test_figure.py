#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import pytest

from figure_package.figure import Figure, Rectangle, Circle, Trapezium, Reader, demonstrate_virtual_call


class TestRectangle:

    def test_create_rectangle(self):
        """Тест создания прямоугольника"""
        rect = Rectangle(2.0, 3.0)
        assert rect.width == 2.0
        assert rect.height == 3.0

    def test_area(self):
        """Тест вычисления площади прямоугольника"""
        rect = Rectangle(4.0, 5.0)
        assert rect.area() == 20.0

    def test_perimeter(self):
        """Тест вычисления периметра прямоугольника"""
        rect = Rectangle(3.0, 4.0)
        assert rect.perimeter() == 14.0

    def test_validation_valid(self):
        """Тест валидации корректного прямоугольника"""
        rect = Rectangle(1.0, 1.0)
        assert rect.is_valid() == True

    def test_validation_invalid(self):
        """Тест валидации некорректного прямоугольника"""
        with pytest.raises(ValueError):
            Rectangle(0, 5.0)
        
        with pytest.raises(ValueError):
            Rectangle(-1.0, 5.0)

    def test_str_representation(self):
        """Тест строкового представления"""
        rect = Rectangle(2.0, 3.0)
        result = str(rect)
        assert "Rectangle" in result
        assert "6.00" in result
        assert "10.00" in result


class TestCircle:

    def test_create_circle(self):
        """Тест создания круга"""
        circle = Circle(5.0)
        assert circle.radius == 5.0

    def test_area(self):
        """Тест вычисления площади круга"""
        circle = Circle(3.0)
        expected_area = math.pi * 9.0
        assert circle.area() == expected_area

    def test_perimeter(self):
        """Тест вычисления периметра круга"""
        circle = Circle(2.0)
        expected_perimeter = 2 * math.pi * 2.0
        assert circle.perimeter() == expected_perimeter

    def test_validation_valid(self):
        """Тест валидации корректного круга"""
        circle = Circle(1.0)
        assert circle.is_valid() == True

    def test_validation_invalid(self):
        """Тест валидации некорректного круга"""
        with pytest.raises(ValueError):
            Circle(0)
        
        with pytest.raises(ValueError):
            Circle(-1.0)

    def test_str_representation(self):
        """Тест строкового представления"""
        circle = Circle(2.0)
        result = str(circle)
        assert "Circle" in result
        assert "12.57" in result
        assert "12.57" in result

class TestTrapezium:

    def test_create_trapezium(self):
        """Тест создания трапеции"""
        trap = Trapezium(6.0, 4.0, 3.0)
        assert trap.base1 == 6.0
        assert trap.base2 == 4.0
        assert trap.height == 3.0

    def test_area(self):
        """Тест вычисления площади трапеции"""
        trap = Trapezium(5.0, 3.0, 4.0)
        expected_area = (5.0 + 3.0) * 4.0 / 2
        assert trap.area() == expected_area

    def test_perimeter(self):
        """Тест вычисления периметра трапеции"""
        trap = Trapezium(5.0, 3.0, 4.0)
        expected_side = math.sqrt(((5.0 - 3.0) / 2) ** 2 + 4.0 ** 2)
        expected_perimeter = 5.0 + 3.0 + 2 * expected_side
        assert trap.perimeter() == expected_perimeter

    def test_validation_valid(self):
        """Тест валидации корректной трапеции"""
        trap = Trapezium(6.0, 4.0, 3.0)
        assert trap.is_valid() == True

    def test_validation_invalid(self):
        """Тест валидации некорректной трапеции"""
        with pytest.raises(ValueError):
            Trapezium(-1.0, 4.0, 3.0)
        
        with pytest.raises(ValueError):
            Trapezium(5.0, 5.0, 3.0)

    def test_str_representation(self):
        """Тест строкового представления"""
        trap = Trapezium(5.0, 3.0, 4.0)
        result = str(trap)
        assert "Trapezium" in result
        assert "16.00" in result
        assert "16.25" in result

class TestReader:

    def test_read_float_valid(self, monkeypatch):
        """Тест чтения float с корректным вводом"""
        monkeypatch.setattr('builtins.input', lambda _: "3.14")
        result = Reader.read_float("Введите число: ")
        assert result == 3.14

    def test_read_float_invalid_then_valid(self, monkeypatch):
        """Тест чтения float с исправлением ошибки"""
        inputs = ["abc", "2.5"]
        input_iter = iter(inputs)
        monkeypatch.setattr('builtins.input', lambda _: next(input_iter))
        
        result = Reader.read_float("Введите число: ")
        assert result == 2.5

    def test_read_int_valid(self, monkeypatch):
        """Тест чтения int с корректным вводом"""
        monkeypatch.setattr('builtins.input', lambda _: "42")
        result = Reader.read_int("Введите целое число: ")
        assert result == 42


class TestInheritanceAndAbstract:

    def test_inheritance(self):
        """Тест наследования"""
        rect = Rectangle(1.0, 1.0)
        circle = Circle(1.0)
        trap = Trapezium(3.0, 2.0, 1.0)

        assert isinstance(rect, Figure)
        assert isinstance(circle, Figure)
        assert isinstance(trap, Figure)

    def test_abstract_methods_implementation(self):
        """Тест реализации абстрактных методов"""
        rect = Rectangle(1.0, 1.0)
        circle = Circle(1.0)
        trap = Trapezium(3.0, 2.0, 1.0)

        assert rect.area() > 0
        assert rect.perimeter() > 0
        assert isinstance(rect.is_valid(), bool)

        assert circle.area() > 0
        assert circle.perimeter() > 0
        assert isinstance(circle.is_valid(), bool)

        assert trap.area() > 0
        assert trap.perimeter() > 0
        assert isinstance(trap.is_valid(), bool)


class TestVirtualCall:

    def test_demonstrate_virtual_call(self, capsys):
        """Тест функции демонстрации виртуальных вызовов"""
        rect = Rectangle(2.0, 3.0)
        demonstrate_virtual_call(rect)
        
        captured = capsys.readouterr()
        assert "Виртуальный вызов" in captured.out
        assert "Площадь" in captured.out
        assert "Периметр" in captured.out
        assert "Корректность" in captured.out


def test_multiple_objects():
    """Тест работы с несколькими объектами"""
    rect1 = Rectangle(2.0, 3.0)
    rect2 = Rectangle(4.0, 5.0)

    circle1 = Circle(2.0)
    circle2 = Circle(3.0)

    trap1 = Trapezium(5.0, 3.0, 4.0)
    trap2 = Trapezium(6.0, 4.0, 3.0)

    assert rect1.area() == 6.0
    assert rect2.area() == 20.0

    assert circle1.area() == math.pi * 4.0
    assert circle2.area() == math.pi * 9.0

    assert trap1.area() == 16.0
    assert trap2.area() == 15.0


def test_edge_cases():
    """Тест граничных случаев"""
    rect_small = Rectangle(0.1, 0.1)
    assert rect_small.area() > 0

    rect_square = Rectangle(2.0, 2.0)
    assert rect_square.perimeter() == 8.0

def test_calculation_accuracy():
    """Тест точности вычислений"""
    rect = Rectangle(2.0, 3.0)
    assert rect.area() == 6.0
    assert rect.perimeter() == 10.0

    circle = Circle(1.0)
    assert abs(circle.area() - math.pi) < 0.001
    assert abs(circle.perimeter() - 2 * math.pi) < 0.001

    trap = Trapezium(4.0, 2.0, 3.0)
    assert trap.area() == 9.0

@pytest.fixture
def sample_rectangle():
    return Rectangle(3.0, 4.0)

@pytest.fixture
def sample_circle():
    return Circle(2.0)

@pytest.fixture
def sample_trapezium():
    return Trapezium(5.0, 3.0, 4.0)

def test_with_fixtures(sample_rectangle, sample_circle, sample_trapezium):
    """Тест с использованием фикстур"""
    assert sample_rectangle.area() == 12.0
    assert sample_circle.area() == math.pi * 4.0
    assert sample_trapezium.area() == 16.0