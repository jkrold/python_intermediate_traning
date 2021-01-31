class Cat:
    def __init__(self, name: str):
        self._name = name

    def make_sound(self) -> str:
        print(f"{self._name}: Meow, meow")