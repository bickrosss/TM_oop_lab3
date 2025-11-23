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
    
    @abstractmethod
    def is_valid(self):
        """Проверка корректности фигуры"""
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
        
        if not self.is_valid():
            raise ValueError("Некорректные параметры прямоугольника")
    
    def is_valid(self):
        """Проверка корректности прямоугольника"""
        return self.width > 0 and self.height > 0
    
    @classmethod
    def create_from_input(cls):
        while True:
            try:
                width = Reader.read_float("Введите ширину: ")
                height = Reader.read_float("Введите высоту: ")
                name = input("Введите название: ") or "Прямоугольник"
                
                # Попытка создания для проверки корректности
                rect = cls(width, height, name)
                print("✅ Прямоугольник создан успешно")
                return rect
            except ValueError as e:
                print(f"❌ Ошибка: {e}")
                print("Пожалуйста, введите корректные значения\n")
    
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
        
        if not self.is_valid():
            raise ValueError("Некорректный параметр круга")
    
    def is_valid(self):
        """Проверка корректности круга"""
        return self.radius > 0
    
    @classmethod
    def create_from_input(cls):
        while True:
            try:
                radius = Reader.read_float("Введите радиус: ")
                name = input("Введите название: ") or "Круг"
                
                circle = cls(radius, name)
                print("✅ Круг создан успешно")
                return circle
            except ValueError as e:
                print(f"❌ Ошибка: {e}")
                print("Пожалуйста, введите корректные значения\n")
    
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
        
        if not self.is_valid():
            raise ValueError("Некорректные параметры трапеции")
    
    def is_valid(self):
        """Проверка корректности трапеции"""
        # Все параметры должны быть положительными
        if self.base1 <= 0 or self.base2 <= 0 or self.height <= 0 or self.side1 <= 0 or self.side2 <= 0:
            return False
        
        # Проверка существования трапеции (сумма оснований должна быть больше разности боковых сторон)
        # и разность оснований должна быть меньше суммы боковых сторон
        bases_diff = abs(self.base1 - self.base2)
        sides_sum = self.side1 + self.side2
        
        return bases_diff < sides_sum
    
    @classmethod
    def create_from_input(cls):
        while True:
            try:
                base1 = Reader.read_float("Введите длину первого основания: ")
                base2 = Reader.read_float("Введите длину второго основания: ")
                height = Reader.read_float("Введите высоту: ")
                side1 = Reader.read_float("Введите длину первой боковой стороны: ")
                side2 = Reader.read_float("Введите длину второй боковой стороны: ")
                name = input("Введите название: ") or "Трапеция"
                
                trapezium = cls(base1, base2, height, side1, side2, name)
                print("✅ Трапеция создана успешно")
                return trapezium
            except ValueError as e:
                print(f"❌ Ошибка: {e}")
                print("Пожалуйста, введите корректные значения\n")
    
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
    print(f"  Корректность: {'Да' if figure.is_valid() else 'Нет'}")
    print(f"  __str__: {figure}")
    print()