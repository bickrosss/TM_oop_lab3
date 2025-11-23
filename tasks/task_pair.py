from pair import Pair, Long


def main():

    # Демонстрация базового класса Pair
    print("1. ДЕМОНСТРАЦИЯ КЛАССА PAIR")
    print("-" * 40)
    
    # Создание пар
    pair1 = Pair(15, 25)
    pair2 = Pair(7, 13)
    
    print("Созданы пары чисел:")
    print(f"Пара 1: {pair1}")
    print(f"Пара 2: {pair2}")
    
    # Операции с парами
    sum_pair = pair1 + pair2
    print(f"\nРезультат сложения пар: {sum_pair}")
    
    # Изменение полей
    print("\nИзменение полей пары 1:")
    pair1.first = 100
    pair1.second = 200
    print(f"После изменения: {pair1}")
    
    # Демонстрация класса-наследника Long
    print("\n2. ДЕМОНСТРАЦИЯ КЛАССА LONG")
    print("-" * 40)
    
    # Создание Long чисел
    long1 = Long(3, 750)
    long2 = Long(2, 450)
    
    print("Созданы Long числа:")
    long1.display()
    long2.display()
    
    # Арифметические операции с Long числами
    print("\nАрифметические операции:")
    
    sum_long = long1 + long2
    print("Сложение: ", end="")
    sum_long.display()
    
    mult_long = long1 * long2
    print("Умножение: ", end="")
    mult_long.display()
    
    sub_long = long1 - long2
    print("Вычитание: ", end="")
    sub_long.display()
    
    # Демонстрация обработки переполнения
    print("\n3. ДЕМОНСТРАЦИЯ ОБРАБОТКИ ПЕРЕПОЛНЕНИЯ")
    print("-" * 40)
    
    long3 = Long(1, 800)
    long4 = Long(1, 500)
    
    print("Числа для теста переполнения:")
    long3.display()
    long4.display()
    
    result = long3 + long4
    print("Результат сложения (с обработкой переполнения): ", end="")
    result.display()
    
    # Работа с пользовательским вводом
    print("\n4. РАБОТА С ПОЛЬЗОВАТЕЛЬСКИМ ВВОДОМ")
    print("-" * 40)
    
    print("Создание пары через ввод:")
    user_pair = Pair()
    user_pair.read()
    print(f"Вы ввели пару: {user_pair}")
    
    print("\nСоздание Long числа через ввод:")
    user_long = Long()
    user_long.read()
    print("Вы ввели: ", end="")
    user_long.display()
    
    print("\n=== ПРОГРАММА ЗАВЕРШЕНА ===")


if __name__ == '__main__':
    main()
