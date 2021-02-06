from abc import ABC, abstractmethod
from math import pi

from typing import Tuple


class Figure(ABC):
    @abstractmethod
    def get_area(self):
        pass


class Rectangle(Figure):
    def __init__(self, height: float, width: float):
        self._height = height
        self._width = width

    def get_area(self):
        return round(self._height * self._width, 2)


class Circle(Figure):
    def __init__(self, radius: float):
        self._radius = radius

    def get_area(self):
        return round(pi * self._radius ** 2, 2)


class Triangle(Figure):
    def __init__(self, height: float, base: float):
        self._height = height
        self._base = base

    def get_area(self):
        return round(self._height * self._base / 2, 2)


# def sum_area_of_figures(*args: Tuple[Figure]):
#     summed_area: float = 0
#     for figure in args:
#         summed_area += figure.get_area()
#     return round(summed_area, 2)

def sum_area_of_figures(figure_list: list) -> float:
    summed_area: float = 0
    for figure in figure_list:
        summed_area += figure.get_area()
    return round(summed_area, 2)


def enough_paint(amount_of_paint: float, figures_list: list) -> bool:
    if amount_of_paint >= sum_area_of_figures(figures_list):
        return True
    else:
        return False
