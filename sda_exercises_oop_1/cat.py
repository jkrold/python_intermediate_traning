from python_intermediate_traning.sda_exercises_oop_1.Movable import Movable


class Cat(Movable):
    def move(self):
        print("I'm walking")

    def __init__(self, name: str):
        self._name = name
        self._number_of_eaten_mice = 0

    def make_sound(self) -> str:
        return f"{self._name}: Meow, meow"

    def eat_mouse(self) -> str:
        self._number_of_eaten_mice += 1
        return f'{self._name}: I ate {self._number_of_eaten_mice} mice'

    @property
    def name(self):
        return self._name
