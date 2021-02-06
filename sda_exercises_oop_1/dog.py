from python_intermediate_traning.sda_exercises_oop_1.Animal import Animal


class Dog(Animal):
    def __init__(self, name: str, sound: str = "Woof, woof"):
        super().__init__(name, sound)

    def make_sound(self) -> str:
        return f"{self._name}: {self._sound}"

    @property
    def name(self):
        return self._name