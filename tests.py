import pytest

from python_intermediate_traning.sda_exercises_oop_1_11_13.Figure import Circle, Triangle, Rectangle, enough_paint, \
    sum_area_of_figures


def test_check_area():
    # given
    circle1 = Circle(1)
    triangle1 = Triangle(2, 1)
    rectangle1 = Rectangle(2, 2)

    # when
    result = sum_area_of_figures([circle1, triangle1, rectangle1])
    print(result)

    assert result == 8.2

print(test_check_area())