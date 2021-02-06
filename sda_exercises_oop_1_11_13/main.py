from python_intermediate_traning.sda_exercises_oop_1_11_13.Figure import Rectangle, Circle, Triangle, sum_area_of_figures, enough_paint
# from python_intermediate_traning.sda_exercises_oop_1_11_13.sum_area_of_figures import sum_area_of_figures

if __name__ == "__main__":

    a = 10.2
    b = 3.1

    Figure1 = Rectangle(a, b)
    Figure2 = Circle(5)
    Figure3 = Triangle(a, b)

    figures = (Figure1, Figure2, Figure3)
    print(sum_area_of_figures(figures))

    paint = 120

    print(enough_paint(paint, figures))