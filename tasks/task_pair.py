from pair import Pair, Long

if __name__ == "__main__":
    print("\n1. СОЗДАНИЕ ОБЪЕКТОВ:")

    print("\nОбъекты Pair")
    p1 = Pair(10, 20)
    p2 = Pair(5, 15)
    print(f"p1 = {p1}")
    print(f"p2 = {p2}")

    print("\nОбъекты Long")
    l1 = Long(3, 450)  # 3450
    l2 = Long(2, 600)  # 2600
    l3 = Long(0, 950)  # 950
    l4 = Long(0, 100)  # 100
    print(f"l1 = {l1}")
    print(f"l2 = {l2}")
    print(f"l3 = {l3}")
    print(f"l4 = {l4}")

    print("\n2. ВЫЗОВ МЕТОДОВ КЛАССА Pair:")

    print("\nМетоды изменения полей")
    print(f"Исходный p1: {p1}")
    p1.set_first(25)
    p1.set_second(35)
    print(f"После set_first(25) и set_second(35): {p1}")
    print(f"get_first(): {p1.get_first()}")
    print(f"get_second(): {p1.get_second()}")

    print("\nСложение пар")
    print(f"p1 = {p1}")
    print(f"p2 = {p2}")
    print(f"p1 + p2 = {p1 + p2}")
    print(f"По формуле: ({p1.get_first()}, {p1.get_second()}) + ({p2.get_first()}, {p2.get_second()}) = ")
    print(f"({p1.get_first()} + {p1.get_second()}, {p2.get_first()} + {p2.get_second()})")

    print("\n3. ВЫЗОВ МЕТОДОВ КЛАССА Long:")

    print("\nСложение Long (с учетом переноса)")
    print(f"l1 = {l1}")
    print(f"l2 = {l2}")
    result_add = l1 + l2
    print(f"l1 + l2 = {result_add}")
    print(f"Проверка: {l1.as_number()} + {l2.as_number()} = {l1.as_number() + l2.as_number()}")

    print("\nУмножение Long")
    result_mul = l1 * l2
    print(f"l1 * l2 = {result_mul}")
    print(f"Проверка: {l1.as_number()} × {l2.as_number()} = {l1.as_number() * l2.as_number()}")

    print("\nВычитание Long")
    result_sub = l1 - l2
    print(f"l1 - l2 = {result_sub}")
    print(f"Проверка: {l1.as_number()} - {l2.as_number()} = {l1.as_number() - l2.as_number()}")

    print("\nДемонстрация переноса при сложении")
    print(f"l3 = {l3} (число: {l3.as_number()})")
    print(f"l4 = {l4} (число: {l4.as_number()})")
    result_carry = l3 + l4
    print(f"l3 + l4 = {result_carry}")
    print(f"Младшая часть: {l3.low} + {l4.low} = {l3.low + l4.low}")
    print(f"Перенос: {l3.low + l4.low} >= {Long.BASE}, поэтому добавляем 1 к старшей части")

    print("\n4. РАБОТА ЧЕРЕЗ БАЗОВЫЙ КЛАСС Pair:")

    pairs = [p1, p2, l1, l2]

    for i, pair in enumerate(pairs, 1):
        print(f"\nОбъект #{i} ({type(pair).__name__})")
        print(f"__str__(): {pair}")
        print(f"first: {pair.get_first()}")
        print(f"second: {pair.get_second()}")
        
        if isinstance(pair, Long):
            print(f"Полное число: {pair.as_number()}")
            print(f"Представление: {pair.high}.{pair.low:03d}")

    print("\n5. РАБОТА СО СВОЙСТВАМИ Long:")

    print("\nИзменение свойств Long")
    test_long = Long(1, 500)  # 1500
    print(f"Исходный: {test_long}")
    print(f"high: {test_long.high}, low: {test_long.low}")
    
    test_long.high = 2
    test_long.low = 800
    print(f"\nПосле изменения: high={test_long.high}, low={test_long.low}")
    print(f"Результат: {test_long}")
    
    test_long.low = 1200
    print(f"\nПрисваиваем low=1200 (>=1000):")
    print(f"Фактическое значение low: {test_long.low}")
    print(f"Замечание: обычно такое значение корректировалось бы при операциях")

    print("\n6. ОБРАБОТКА ОШИБОК:")

    print("\nПопытка вычитания с отрицательным результатом")
    small = Long(0, 100)  # 100
    large = Long(0, 200)  # 200
    print(f"small = {small}")
    print(f"large = {large}")
    
    try:
        result = small - large
        print(f"small - large = {result}")
    except ValueError as e:
        print(f"Ошибка: {e}")
    
    print("\nКорректное вычитание")
    result = large - small
    print(f"large - small = {result}")
    print(f"big1 = {big1}")
    print(f"big2 = {big2}")
    print(f"big1 + big2 = {big1 + big2}")
    print(f"big1 * big2 = {big1 * big2}")
