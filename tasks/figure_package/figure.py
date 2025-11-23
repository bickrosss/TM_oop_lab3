#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from math import pi

class Reader:
    @staticmethod
    def read_float(prompt):
        return float(input(prompt))
    
    @staticmethod
    def read_int(prompt):
        return int(input(prompt))

class Figure(ABC):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
    def __str__(self):
        return f"{self.name}: площадь = {self.area():.2f}, периметр = {self.perimeter():.2f}"
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.name})"

class Rectangle(Figure):
    def __init__(self, width, height, name="Прямоугольник"):
        super().__init__(name)
        self.width = width
        self.height = height
    
    @classmethod
    def create_from_input(cls):
        print("Создание прямоугольника:")
        width = Reader.read_float("Введите ширину: ")
        height = Reader.read_float("Введите высоту: ")
        name = input("Введите название (опционально): ") or "Прямоугольник"
        return cls(width, height, name)
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def __str__(self):
        return f"{self.name}: {self.width}×{self.height}, площадь = {self.area():.2f}, периметр = {self.perimeter():.2f}"

class Circle(Figure):
    def __init__(self, radius, name="Круг"):
        super().__init__(name)
        self.radius = radius
    
    @classmethod
    def create_from_input(cls):
        print("Создание круга:")
        radius = Reader.read_float("Введите радиус: ")
        name = input("Введите название (опционально): ") or "Круг"
        return cls(radius, name)
    
    def area(self):
        return pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * pi * self.radius
    
    def __str__(self):
        return f"{self.name}: радиус = {self.radius}, площадь = {self.area():.2f}, периметр = {self.perimeter():.2f}"

class Trapezium(Figure):
    def __init__(self, base1, base2, height, side1, side2, name="Трапеция"):
        super().__init__(name)
        self.base1 = base1
        self.base2 = base2
        self.height = height
        self.side1 = side1
        self.side2 = side2
    
    @classmethod
    def create_from_input(cls):
        print("Создание трапеции:")
        base1 = Reader.read_float("Введите длину первого основания: ")
        base2 = Reader.read_float("Введите длину второго основания: ")
        height = Reader.read_float("Введите высоту: ")
        side1 = Reader.read_float("Введите длину первой боковой стороны: ")
        side2 = Reader.read_float("Введите длину второй боковой стороны: ")
        name = input("Введите название (опционально): ") or "Трапеция"
        return cls(base1, base2, height, side1, side2, name)
    
    def area(self):
        return (self.base1 + self.base2) * self.height / 2
    
    def perimeter(self):
        return self.base1 + self.base2 + self.side1 + self.side2
    
    def __str__(self):
        return f"{self.name}: основания = {self.base1}, {self.base2}, высота = {self.height}, площадь = {self.area():.2f}, периметр = {self.perimeter():.2f}"

def demonstrate_virtual_call(figure: Figure):
    """Функция, демонстрирующая виртуальный вызов методов базового класса"""
    print(f"Виртуальный вызов для {figure.name}:")
    print(f"  Площадь: {figure.area():.2f}")
    print(f"  Периметр: {figure.perimeter():.2f}")
    print(f"  __str__: {figure}")
    print()

if __name__ == '__main__':
    print("=== ДЕМОНСТРАЦИЯ АБСТРАКТНЫХ КЛАССОВ ФИГУР ===\n")
    
    # Создание фигур напрямую
    figures = [
        Rectangle(5, 3, "Прямоугольник A"),
        Circle(4, "Круг B"),
        Trapezium(6, 4, 3, 3, 3, "Трапеция C")
    ]
    
    print("1. СОЗДАННЫЕ ФИГУРЫ:")
    print("-" * 50)
    for figure in figures:
        print(figure)
    print()
    
    # Демонстрация виртуальных вызовов
    print("2. ВИРТУАЛЬНЫЕ ВЫЗОВЫ:")
    print("-" * 50)
    for figure in figures:
        demonstrate_virtual_call(figure)
    
    # Создание фигур через ввод данных
    print("3. СОЗДАНИЕ ФИГУР ЧЕРЕЗ ВВОД:")
    print("-" * 50)
    
    user_figures = []
    
    print("Создадим прямоугольник:")
    rect = Rectangle.create_from_input()
    user_figures.append(rect)
    print()
    
    print("Создадим круг:")
    circle = Circle.create_from_input()
    user_figures.append(circle)
    print()
    
    print("Создадим трапецию:")
    trapezium = Trapezium.create_from_input()
    user_figures.append(trapezium)
    print()
    
    print("4. ПОЛЬЗОВАТЕЛЬСКИЕ ФИГУРЫ:")
    print("-" * 50)
    for figure in user_figures:
        print(figure)
    print()
    
    # Демонстрация полиморфизма
    print("5. ПОЛИМОРФИЗМ В ДЕЙСТВИИ:")
    print("-" * 50)
    all_figures = figures + user_figures
    
    total_area = sum(fig.area() for fig in all_figures)
    total_perimeter = sum(fig.perimeter() for fig in all_figures)
    
    print(f"Общая площадь всех фигур: {total_area:.2f}")
    print(f"Общий периметр всех фигур: {total_perimeter:.2f}")
    print()
    
    # Использование repr
    print("6. ПРЕДСТАВЛЕНИЕ ЧЕРЕЗ __repr__:")
    print("-" * 50)
    for figure in all_figures:
        print(repr(figure))
