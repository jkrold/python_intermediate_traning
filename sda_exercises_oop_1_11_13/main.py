from python_intermediate_traning.sda_exercises_oop_1_11_13.Figure import Rectangle, Circle, Triangle

if __name__ == "__main__":

    a = 10.2
    b = 3.1

    print(Rectangle(a, b).get_area())
    print(Circle(5).get_area())
    print(Triangle(a, b).get_area())