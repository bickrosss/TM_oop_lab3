#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from figure_package import Figure, Rectangle, Circle, Trapezium, demonstrate_virtual_call

def main():
    print("=== ПРОГРАММА ДЛЯ РАБОТЫ С ГЕОМЕТРИЧЕСКИМИ ФИГУРАМИ ===\n")
    
    figures = []
    
    # Создание фигур через ввод с клавиатуры
    print("Создание фигур через ввод данных:")
    print("-" * 40)
    
    # Прямоугольник
    print("Создание прямоугольника:")
    rect = Rectangle.create_from_input()
    figures.append(rect)
    print()
    
    # Круг
    print("Создание круга:")
    circle = Circle.create_from_input()
    figures.append(circle)
    print()
    
    # Трапеция
    print("Создание трапеции:")
    trapezium = Trapezium.create_from_input()
    figures.append(trapezium)
    print()
    
    # Вывод созданных фигур
    print("СОЗДАННЫЕ ФИГУРЫ:")
    print("=" * 50)
    for i, figure in enumerate(figures, 1):
        valid_status = "✓ Корректна" if figure.is_valid() else "✗ Некорректна"
        print(f"{i}. {figure} [{valid_status}]")
    print()
    
    # Демонстрация виртуальных вызовов
    print("ВИРТУАЛЬНЫЕ ВЫЗОВЫ:")
    print("=" * 50)
    for figure in figures:
        demonstrate_virtual_call(figure)
    
    # Статистика только по корректным фигурам
    print("СТАТИСТИКА (только корректные фигуры):")
    print("=" * 50)
    
    valid_figures = [f for f in figures if f.is_valid()]
    
    if valid_figures:
        max_area_figure = max(valid_figures, key=lambda f: f.area())
        min_area_figure = min(valid_figures, key=lambda f: f.area())
        
        max_perimeter_figure = max(valid_figures, key=lambda f: f.perimeter())
        min_perimeter_figure = min(valid_figures, key=lambda f: f.perimeter())
        
        print(f"Фигура с максимальной площадью: {max_area_figure.name} ({max_area_figure.area():.2f})")
        print(f"Фигура с минимальной площадью: {min_area_figure.name} ({min_area_figure.area():.2f})")
        print(f"Фигура с максимальным периметром: {max_perimeter_figure.name} ({max_perimeter_figure.perimeter():.2f})")
        print(f"Фигура с минимальным периметром: {min_perimeter_figure.name} ({min_perimeter_figure.perimeter():.2f})")
        
        total_area = sum(fig.area() for fig in valid_figures)
        print(f"Общая площадь всех корректных фигур: {total_area:.2f}")
    else:
        print("Нет корректных фигур для статистики")

if __name__ == '__main__':
    main()