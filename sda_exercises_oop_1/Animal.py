from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name: str, sound: str):
        self._name = name
        self._sound = sound

    @abstractmethod
    def make_sound(self):
        pass