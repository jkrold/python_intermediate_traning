from abc import ABC, abstractmethod


class Movable(ABC):
    @abstractmethod
    def move(self):
        return "I'm going"
