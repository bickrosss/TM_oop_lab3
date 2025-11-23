#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Figure:
    def __init__(self, color):
        self.__color = color

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, c):
        self.__color = c

    def info(self):
        print("Figure")
        print("Color: " + self.color)


class Rectangle(Figure):
    def __init__(self, width, height, color):
        super().__init__(color)
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, w):
        if w > 0:
            self.__width = w
        else:
            raise ValueError("Width must be positive")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, h):
        if h > 0:
            self.__height = h
        else:
            raise ValueError("Height must be positive")

    def area(self):
        return self.__width * self.__height

    def info(self):
        print("Rectangle")
        print("Color: " + self.color)
        print("Width: " + str(self.width))
        print("Height: " + str(self.height))
        print("Area: " + str(self.area()))


class Circle(Figure):
    def __init__(self, radius, color):
        super().__init__(color)
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, r):
        if r > 0:
            self.__radius = r
        else:
            raise ValueError("Radius must be positive")

    def area(self):
        return 3.14159 * self.__radius ** 2

    def info(self):
        print("Circle")
        print("Color: " + self.color)
        print("Radius: " + str(self.radius))
        print("Area: " + str(self.area()))


def demonstrate_inheritance():
    print("=== Демонстрация наследования ===")
    
    # Создание объектов
    fig = Figure("orange")
    rect = Rectangle(10, 20, "green")
    
    print("\nБазовый класс Figure:")
    fig.info()
    
    print("\nКласс-наследник Rectangle:")
    rect.info()
    
    # Доступ к свойствам
    print(f"\nСвойства Rectangle:")
    print(f"Width: {rect.width}")
    print(f"Height: {rect.height}")
    print(f"Color: {rect.color}")
    
    # Изменение свойств
    rect.color = "red"
    print(f"\nПосле изменения цвета: {rect.color}")


def demonstrate_polymorphism():
    print("\n=== Демонстрация полиморфизма ===")
    
    # Создание объектов разных классов
    figures = [
        Figure("blue"),
        Rectangle(5, 10, "green"),
        Circle(7, "red")
    ]
    
    # Полиморфный вызов метода info()
    for figure in figures:
        figure.info()
        print("-" * 20)


def demonstrate_setters():
    print("\n=== Демонстрация сеттеров с валидацией ===")
    
    rect = Rectangle(15, 25, "yellow")
    
    try:
        rect.width = -5  # Это вызовет ошибку
    except ValueError as e:
        print(f"Ошибка при установке ширины: {e}")
    
    try:
        rect.height = 30  # Это работает
        print(f"Новая высота: {rect.height}")
    except ValueError as e:
        print(f"Ошибка при установке высоты: {e}")


if __name__ == "__main__":
    demonstrate_inheritance()
    demonstrate_polymorphism()
    demonstrate_setters()
