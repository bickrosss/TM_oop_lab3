#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from abc import ABC, abstractmethod


class parent(ABC):

    @property
    @abstractmethod
    def geeks(self) -> str:
        pass


class child(parent):

    @property
    def geeks(self) -> str:
        return "child class"


try:
    r = parent()  # type: ignore[abstract]
    print(r.geeks)
except Exception as err:
    print(err)

r = child()
print(r.geeks)
