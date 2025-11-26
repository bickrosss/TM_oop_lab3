#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import gcd

class Pair:
    def __init__(self, first=0, second=0):
        self.__first = int(first)
        self.__second = int(second)
    
    @property
    def first(self):
        return self.__first
    
    @first.setter
    def first(self, value):
        self.__first = int(value)
    
    @property
    def second(self):
        return self.__second
    
    @second.setter
    def second(self, value):
        self.__second = int(value)
    
    def read(self):
        self.__first = int(input("Введите первое число: "))
        self.__second = int(input("Введите второе число: "))
    
    def display(self):
        print(f"({self.__first}, {self.__second})")
    
    def add(self, other):
        if isinstance(other, Pair):
            return Pair(self.__first + other.__first, self.__second + other.__second)
        else:
            raise ValueError("Операнд должен быть типа Pair")
    
    def __add__(self, other):
        return self.add(other)
    
    def __str__(self):
        return f"({self.__first}, {self.__second})"


class Long(Pair):
    def __init__(self, high=0, low=0):
        super().__init__(high, low)
    
    @property
    def high(self):
        return self.first
    
    @high.setter
    def high(self, value):
        self.first = value
    
    @property
    def low(self):
        return self.second
    
    @low.setter
    def low(self, value):
        self.second = value
    
    def read(self):
        self.high = int(input("Введите старшую часть числа: "))
        self.low = int(input("Введите младшую часть числа: "))
    
    def display(self):
        print(f"Старшая часть={self.high}, младшая часть={self.low}")
    
    def add(self, other):
        if isinstance(other, Long):
            new_high = self.high + other.high
            new_low = self.low + other.low
            
            # Обработка переполнения младшей части
            if new_low >= 1000:
                new_high += new_low // 1000
                new_low = new_low % 1000
            
            return Long(new_high, new_low)
        else:
            raise ValueError("Операнд должен быть типа Long")
    
    def multiply(self, other):
        if isinstance(other, Long):
            # Упрощенное умножение (для демонстрации)
            total_high = self.high * other.high
            total_low = self.low * other.low
            
            # Нормализация
            if total_low >= 1000:
                total_high += total_low // 1000
                total_low = total_low % 1000
            
            return Long(total_high, total_low)
        else:
            raise ValueError("Операнд должен быть типа Long")
    
    def subtract(self, other):
        if isinstance(other, Long):
            new_high = self.high - other.high
            new_low = self.low - other.low
            
            # Обработка отрицательной младшей части
            if new_low < 0:
                new_high -= 1
                new_low += 1000
            
            return Long(new_high, new_low)
        else:
            raise ValueError("Операнд должен быть типа Long")
    
    def __mul__(self, other):
        return self.multiply(other)
    
    def __sub__(self, other):
        return self.subtract(other)


if __name__ == '__main__':
    print("Демонстрация класса Pair")
    p1 = Pair(10, 20)
    p2 = Pair(5, 15)
    
    print("Пары чисел:")
    print(f"p1 = ", end="")
    p1.display()
    print(f"p2 = ", end="")
    p2.display()
    
    result_pair = p1 + p2
    print("Сложение пар: ", end="")
    result_pair.display()
    
    print("\nДемонстрация класса Long")
    l1 = Long(2, 500)
    l2 = Long(1, 600)
    
    print("Long числа:")
    l1.display()
    l2.display()
    
    result_add = l1 + l2
    print("Сложение Long: ", end="")
    result_add.display()
    
    result_mult = l1 * l2
    print("Умножение Long: ", end="")
    result_mult.display()
    
    result_sub = l1 - l2
    print("Вычитание Long: ", end="")
    result_sub.display()
    
    print("\nТестирование переполнения")
    l3 = Long(1, 800)
    l4 = Long(1, 300)
    
    print("Тест переполнения:")
    l3.display()
    l4.display()
    
    result_overflow = l3 + l4
    print("Результат (с обработкой переполнения): ", end="")
    result_overflow.display()
    
    print("Создадим новую пару через ввод:")
    p3 = Pair()
    p3.read()
    print("Введенная пара: ", end="")
    p3.display()
    
    print("Создадим новое Long число через ввод:")
    l5 = Long()
    l5.read()
    print("Введенное число: ", end="")
    l5.display()
