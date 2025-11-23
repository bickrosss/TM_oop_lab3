#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def move(self) -> None:
        pass


class Human(Animal):

    def move(self) -> None:
        print("I can walk and run")


class Snake(Animal):

    def move(self) -> None:
        print("I can crawl")


class Dog(Animal):

    def move(self) -> None:
        print("I can bark")


class Lion(Animal):

    def move(self) -> None:
        print("I can roar")


H = Human()
H.move()

S = Snake()
S.move()

D = Dog()
D.move()

K = Lion()
K.move()
