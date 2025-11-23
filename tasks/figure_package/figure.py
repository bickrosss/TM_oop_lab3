#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from math import pi, sqrt

class Reader:
    @staticmethod
    def read_float(prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Ошибка: введите число")
    
    @staticmethod
    def read_int(prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Ошибка: введите целое число")

class Figure(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
    @abstractmethod
    def is_valid(self):
        pass
    
    def __str__(self):
        return f"{self.__class__.__name__}: площадь = {self.area():.2f}, периметр = {self.perimeter():.2f}"

class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        if not self.is_valid():
            raise ValueError("Некорректные параметры прямоугольника")
    
    def is_valid(self):
        return self.width > 0 and self.height > 0
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius
        if not self.is_valid():
            raise ValueError("Некорректный параметр круга")
    
    def is_valid(self):
        return self.radius > 0
    
    def area(self):
        return pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * pi * self.radius

class Trapezium(Figure):
    def __init__(self, base1, base2, height):
        self.base1 = base1
        self.base2 = base2
        self.height = height
        # Вычисляем боковые стороны (для упрощения считаем равнобедренной)
        self.side = sqrt(((base1 - base2) / 2) ** 2 + height ** 2)
        if not self.is_valid():
            raise ValueError("Некорректные параметры трапеции")
    
    def is_valid(self):
        # Все параметры положительные и основания разные
        return (self.base1 > 0 and self.base2 > 0 and 
                self.height > 0 and self.base1 != self.base2)
    
    def area(self):
        return (self.base1 + self.base2) * self.height / 2
    
    def perimeter(self):
        return self.base1 + self.base2 + 2 * self.side

def demonstrate_virtual_call(figure: Figure):
    """Функция, демонстрирующая виртуальный вызов"""
    print(f"Виртуальный вызов для {figure.__class__.__name__}:")
    print(f"  Площадь: {figure.area():.2f}")
    print(f"  Периметр: {figure.perimeter():.2f}")
    print(f"  Корректность: {'Да' if figure.is_valid() else 'Нет'}")
    print()