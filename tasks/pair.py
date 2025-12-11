#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Pair:
    BASE = 1000
    
    def __init__(self, first=0, second=0):
        self.first = first
        self.second = second
    
    def set_first(self, value):
        self.first = value
    
    def set_second(self, value):
        self.second = value
    
    def get_first(self):
        return self.first
    
    def get_second(self):
        return self.second
    
    def add(self, other):
        return Pair(self.first + self.second, other.first + other.second)
    
    def __add__(self, other):
        return self.add(other)
    
    def __str__(self):
        return f"({self.first}, {self.second})"


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
    
    def add(self, other):

        new_low = self.low + other.low
        new_high = self.high + other.high
        
        if new_low >= self.BASE:
            new_high += new_low // self.BASE
            new_low = new_low % self.BASE
        
        return Long(new_high, new_low)
    
    def multiply(self, other):

        num1 = self.high * self.BASE + self.low
        num2 = other.high * self.BASE + other.low
        result = num1 * num2
        
        new_high = result // self.BASE
        new_low = result % self.BASE
    
        if new_low >= self.BASE:
            new_high += new_low // self.BASE
            new_low = new_low % self.BASE
        
        return Long(new_high, new_low)
    
    def subtract(self, other):
        num1 = self.high * self.BASE + self.low
        num2 = other.high * self.BASE + other.low
        
        if num1 < num2:
            raise ValueError("Результат не может быть отрицательным")
        
        result = num1 - num2
        return Long(result // self.BASE, result % self.BASE)
    
    def __mul__(self, other):
        return self.multiply(other)
    
    def __sub__(self, other):
        return self.subtract(other)
    
    def __str__(self):
        return f"{self.high}.{self.low:03d}"


