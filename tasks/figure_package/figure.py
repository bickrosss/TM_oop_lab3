#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from math import pi


class Reader:
    @staticmethod
    def read_float(prompt: str) -> float:
        return float(input(prompt))


class Figure(ABC):
    @abstractmethod
    def area(self) -> float:
        pass
    
    @abstractmethod
    def perimeter(self) -> float:
        pass
    
    @abstractmethod
    def __str__(self) -> str:
        pass


class Rectangle(Figure):
    def __init__(self, width: float = 0, height: float = 0):
        self.__width = width
        self.__height = height
    
    @property
    def width(self) -> float:
        return self.__width
    
    @property
    def height(self) -> float:
        return self.__height
    
    @width.setter
    def width(self, value: float) -> None:
        if value <= 0:
            raise ValueError("Ширина должна быть положительной")
        self.__width = value
    
    @height.setter
    def height(self, value: float) -> None:
        if value <= 0:
            raise ValueError("Высота должна быть положительной")
        self.__height = value
    
    def area(self) -> float:
        return self.__width * self.__height
    
    def perimeter(self) -> float:
        return 2 * (self.__width + self.__height)
    
    def __str__(self) -> str:
        return (
            f"Прямоугольник:\n"
            f"  Ширина: {self.__width}\n"
            f"  Высота: {self.__height}\n"
            f"  Площадь: {self.area():.2f}\n"
            f"  Периметр: {self.perimeter():.2f}"
        )


class Circle(Figure):
    def __init__(self, radius: float = 0):
        self.__radius = radius
    
    @property
    def radius(self) -> float:
        return self.__radius
    
    @radius.setter
    def radius(self, value: float) -> None:
        if value <= 0:
            raise ValueError("Радиус должен быть положительным")
        self.__radius = value
    
    def area(self) -> float:
        return pi * self.__radius ** 2
    
    def perimeter(self) -> float:
        return 2 * pi * self.__radius
    
    def __str__(self) -> str:
        return (
            f"Круг:\n"
            f"  Радиус: {self.__radius}\n"
            f"  Площадь: {self.area():.2f}\n"
            f"  Периметр (длина окружности): {self.perimeter():.2f}"
        )


class Trapezium(Figure):
    def __init__(self, base1: float = 0, base2: float = 0, 
                 side1: float = 0, side2: float = 0, height: float = 0):
        self.__base1 = base1
        self.__base2 = base2
        self.__side1 = side1
        self.__side2 = side2
        self.__height = height
    
    @property
    def base1(self) -> float:
        return self.__base1
    
    @property
    def base2(self) -> float:
        return self.__base2
    
    @property
    def side1(self) -> float:
        return self.__side1
    
    @property
    def side2(self) -> float:
        return self.__side2
    
    @property
    def height(self) -> float:
        return self.__height
    
    @base1.setter
    def base1(self, value: float) -> None:
        if value <= 0:
            raise ValueError("Основание должно быть положительным")
        self.__base1 = value
    
    @base2.setter
    def base2(self, value: float) -> None:
        if value <= 0:
            raise ValueError("Основание должно быть положительным")
        self.__base2 = value
    
    @side1.setter
    def side1(self, value: float) -> None:
        if value <= 0:
            raise ValueError("Боковая сторона должна быть положительной")
        self.__side1 = value
    
    @side2.setter
    def side2(self, value: float) -> None:
        if value <= 0:
            raise ValueError("Боковая сторона должна быть положительной")
        self.__side2 = value
    
    @height.setter
    def height(self, value: float) -> None:
        if value <= 0:
            raise ValueError("Высота должна быть положительной")
        self.__height = value
    
    def area(self) -> float:
        return (self.__base1 + self.__base2) * self.__height / 2
    
    def perimeter(self) -> float:
        return self.__base1 + self.__base2 + self.__side1 + self.__side2
    
    def __str__(self) -> str:
        return (
            f"Трапеция:\n"
            f"  Верхнее основание: {self.__base1}\n"
            f"  Нижнее основание: {self.__base2}\n"
            f"  Боковая сторона 1: {self.__side1}\n"
            f"  Боковая сторона 2: {self.__side2}\n"
            f"  Высота: {self.__height}\n"
            f"  Площадь: {self.area():.2f}\n"
            f"  Периметр: {self.perimeter():.2f}"
        )
