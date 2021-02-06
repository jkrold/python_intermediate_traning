import pytest

from python_intermediate_traning.sda_exercises_oop_1_11_13.Figure import Circle, Triangle, Rectangle, enough_paint, \
    sum_area_of_figures


def test_check_sum_of_area():
    # given
    circle1 = Circle(1)
    triangle1 = Triangle(2, 1)
    rectangle1 = Rectangle(2, 2)

    # when
    result = sum_area_of_figures([circle1, triangle1, rectangle1])
    print(result)

    assert result == 8.14

def test_enough_paint_method():
    # given
    circle1 = Circle(1)
    triangle1 = Triangle(2, 1)
    rectangle1 = Rectangle(2, 2)

    can_of_paint = 9

    assert enough_paint(can_of_paint, [circle1, triangle1, rectangle1]) == True

def test_enough_paint_method_2():
    # given
    circle1 = Circle(1)
    triangle1 = Triangle(2, 1)
    rectangle1 = Rectangle(2, 2)

    can_of_paint = 3

    assert enough_paint(can_of_paint, [circle1, triangle1, rectangle1]) == False


print(test_check_sum_of_area())