class Dog:
    def __init__(self, name: str):
        self._name = name

    def make_sound(self) -> str:
        return f"{self._name}: Woof, woof"

    @property
    def name(self):
        return self._name