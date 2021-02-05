from abc import ABC, abstractmethod


class Movable(ABC):
    @abstractmethod
    def move(self):
        print("I'm going")