#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from figure_package.figure import Figure, Rectangle, Circle, Trapezium, Reader, demonstrate_virtual_call

def main():
    print("ДЕМОНСТРАЦИЯ НАСЛЕДОВАНИЯ И ПОЛИМОРФИЗМА") 
    reader = Reader()
    
    print("1. СОЗДАНИЕ ОБЪЕКТОВ:")
    
    print("\nСоздание прямоугольника")
    width = reader.read_float("Введите ширину прямоугольника: ")
    height = reader.read_float("Введите высоту прямоугольника: ")
    rect = Rectangle(width, height)
    print(rect)
    
    print("\nСоздание круга")
    radius = reader.read_float("Введите радиус круга: ")
    circle = Circle(radius)
    print(circle)
    
    print("\n-Создание трапеции")
    base1 = reader.read_float("Введите верхнее основание трапеции: ")
    base2 = reader.read_float("Введите нижнее основание трапеции: ")
    side1 = reader.read_float("Введите левую боковую сторону: ")
    side2 = reader.read_float("Введите правую боковую сторону: ")
    height_trap = reader.read_float("Введите высоту трапеции: ")
    trap = Trapezium(base1, base2, side1, side2, height_trap)
    print(trap)
    
    # 2. ВЫЗОВ АБСТРАКТНЫХ МЕТОДОВ
    print("\n2. ВЫЗОВ АБСТРАКТНЫХ МЕТОДОВ:")    
    figures = [rect, circle, trap]
    
    for i, figure in enumerate(figures, 1):
        print(f"\nФигура #{i} ({type(figure).__name__})")
        print(f"Площадь: {figure.area():.2f}")
        print(f"Периметр: {figure.perimeter():.2f}")
    print("\n3. ДЕМОНСТРАЦИЯ ВИРТУАЛЬНЫХ ВЫЗОВОВ:")
    
    for figure in figures:
        demonstrate_virtual_call(figure)

    print("\n4. РАБОТА СО СВОЙСТВАМИ:")
    
    print("\nИзменение свойств прямоугольника")
    print(f"Текущие значения: ширина={rect.width}, высота={rect.height}")
    
    new_width = reader.read_float("Введите новую ширину: ")
    new_height = reader.read_float("Введите новую высоту: ")
    
    rect.width = new_width
    rect.height = new_height
    
    print(f"\nПосле изменения:")
    print(f"Ширина: {rect.width}")
    print(f"Высота: {rect.height}")
    print(f"Площадь: {rect.area():.2f}")
    print(f"Периметр: {rect.perimeter():.2f}")
    
    print("\n5. РАБОТА ЧЕРЕЗ БАЗОВЫЙ КЛАСС FIGURE:")
    
    for i, figure in enumerate(figures, 1):
        print(f"\nФигура {i} через базовый класс Figure:")
        print(f"Тип: {type(figure).__name__}")
        print(f"Площадь (вызов area()): {figure.area():.2f}")
        print(f"Периметр (вызов perimeter()): {figure.perimeter():.2f}")

if __name__ == '__main__':
    main()
