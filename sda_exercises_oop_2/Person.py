from datetime import date

class Person:
    def __init__(self, first_name: str, last_name: str, birthsday: date):
        self._first_name = first_name
        self._last_name = last_name
        self._birthsday = birthsday