from abc import ABC, abstractmethod
from math import pi


class Figure(ABC):
    @abstractmethod
    def get_area(self):
        pass

class Rectangle(Figure):
    def __init__(self, height: float, width: float):
        self._height = height
        self._width = width

    def get_area(self):
        return self._height * self._width

class Circle(Figure):
    def __init__(self, radius: float):
        self._radius = radius

    def get_area(self):
        return pi * self._radius ** 2

class Triangle(Figure):
    def __init__(self, height: float, base: float):
        self._height = height
        self._base = base

    def get_area(self):
        return self._height * self._base / 2
