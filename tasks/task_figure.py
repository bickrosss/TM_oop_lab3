#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from figure_package import Figure, Rectangle, Circle, Trapezium, demonstrate_virtual_call

def main():   
    # Создание коллекции различных фигур
    figures = [
        Rectangle(10, 5, "Большой прямоугольник"),
        Rectangle(3, 2, "Маленький прямоугольник"),
        Circle(7, "Большой круг"),
        Circle(2.5, "Маленький круг"),
        Trapezium(8, 5, 4, 3, 3, "Равнобедренная трапеция"),
        Trapezium(12, 6, 5, 4, 4, "Прямоугольная трапеция")
    ]
    
    print("1. ВСЕ ФИГУРЫ:")
    print("=" * 60)
    for i, figure in enumerate(figures, 1):
        print(f"{i}. {figure}")
    print()
    
    # Демонстрация виртуальных вызовов
    print("2. ДЕМОНСТРАЦИЯ ВИРТУАЛЬНЫХ ВЫЗОВОВ:")
    print("=" * 60)
    for figure in figures:
        demonstrate_virtual_call(figure)
    
    # Группировка по типам фигур
    print("3. СТАТИСТИКА ПО ТИПАМ ФИГУР:")
    print("=" * 60)
    
    rectangles = [f for f in figures if isinstance(f, Rectangle)]
    circles = [f for f in figures if isinstance(f, Circle)]
    trapeziums = [f for f in figures if isinstance(f, Trapezium)]
    
    print(f"Прямоугольников: {len(rectangles)}")
    for rect in rectangles:
        print(f"  - {rect.name}: {rect.width}×{rect.height}")
    
    print(f"\nКругов: {len(circles)}")
    for circle in circles:
        print(f"  - {circle.name}: радиус {circle.radius}")
    
    print(f"\nТрапеций: {len(trapeziums)}")
    for trap in trapeziums:
        print(f"  - {trap.name}: основания {trap.base1}, {trap.base2}")
    
    # Вычисление общих характеристик
    print("\n4. ОБЩИЕ ХАРАКТЕРИСТИКИ:")
    print("=" * 60)
    
    max_area_figure = max(figures, key=lambda f: f.area())
    min_area_figure = min(figures, key=lambda f: f.area())
    
    max_perimeter_figure = max(figures, key=lambda f: f.perimeter())
    min_perimeter_figure = min(figures, key=lambda f: f.perimeter())
    
    print(f"Фигура с максимальной площадью: {max_area_figure.name} ({max_area_figure.area():.2f})")
    print(f"Фигура с минимальной площадью: {min_area_figure.name} ({min_area_figure.area():.2f})")
    print(f"Фигура с максимальным периметром: {max_perimeter_figure.name} ({max_perimeter_figure.perimeter():.2f})")
    print(f"Фигура с минимальным периметром: {min_perimeter_figure.name} ({min_perimeter_figure.perimeter():.2f})")
    
    # Демонстрация работы с базовым классом
    print("\n5. РАБОТА С БАЗОВЫМ КЛАССОМ FIGURE:")
    print("=" * 60)
    
    def process_figures(figures_list):
        """Функция, работающая только с базовым классом Figure"""
        results = []
        for figure in figures_list:
            # Виртуальные вызовы - полиморфизм в действии
            area = figure.area()
            perimeter = figure.perimeter()
            results.append((figure.name, area, perimeter))
        return results
    
    results = process_figures(figures)
    for name, area, perimeter in results:
        print(f"{name}: площадь = {area:.2f}, периметр = {perimeter:.2f}")
    
    print("\n=== ПРОГРАММА ЗАВЕРШЕНА ===")

if __name__ == '__main__':
    main()
