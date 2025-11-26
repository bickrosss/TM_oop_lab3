#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from figure_package.figure import Figure, Rectangle, Circle, Trapezium, Reader, demonstrate_virtual_call

def create_figures_with_reader():
    """Создание фигур с использованием класса Reader"""
    reader = Reader()
    figures = []
    
    print("Создание прямоугольника:")
    width = reader.read_float("Введите ширину: ")
    height = reader.read_float("Введите высоту: ")
    figures.append(Rectangle(width, height))
    
    print("\nСоздание круга:")
    radius = reader.read_float("Введите радиус: ")
    figures.append(Circle(radius))
    
    print("\nСоздание трапеции:")
    base1 = reader.read_float("Введите первое основание: ")
    base2 = reader.read_float("Введите второе основание: ")
    height = reader.read_float("Введите высоту: ")
    figures.append(Trapezium(base1, base2, height))
    
    return figures

def main():
    print("Демонстарция наследования и полиморфизма\n")
    
    # Создание фигур
    figures = create_figures_with_reader()
    
    print("\n" + "="*50)
    print("Демонстрация виртуальных вызовов:")
    print("="*50)
    
    # Демонстрация полиморфизма
    for figure in figures:
        demonstrate_virtual_call(figure)
        print(f"Вызов __str__: {figure}")
        print("-" * 30)

if __name__ == '__main__':
    main()