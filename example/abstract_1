#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from abc import ABC, abstractmethod


class Polygon(ABC):

    @abstractmethod
    def noofsides(self) -> None:
        pass


class Triangle(Polygon):

    def noofsides(self) -> None:
        print("I have 3 sides")


class Pentagon(Polygon):

    def noofsides(self) -> None:
        print("I have 5 sides")


class Hexagon(Polygon):

    def noofsides(self) -> None:
        print("I have 6 sides")


class Quadrilateral(Polygon):

    def noofsides(self) -> None:
        print("I have 4 sides")


R = Triangle()
R.noofsides()

K = Quadrilateral()
K.noofsides()

P = Pentagon()
P.noofsides()

H = Hexagon()
H.noofsides()
