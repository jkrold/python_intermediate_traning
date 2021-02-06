class Dog:
    def __init__(self, name: str, sound: str = "Woof, woof"):
        self._name = name
        self._sound = sound

    def make_sound(self) -> str:
        return f"{self._name}: {self._sound}"

    @property
    def name(self):
        return self._name