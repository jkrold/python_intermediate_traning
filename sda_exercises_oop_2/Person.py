from datetime import date


class Person:
    def __init__(self, first_name: str, last_name: str, day_of_birth: date):
        self._first_name = first_name
        self._last_name = last_name
        self._day_of_birth = day_of_birth

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def day_of_birth(self):
        return self._day_of_birth

    @first_name.setter
    def first_name(self, first_name: str):
        self._first_name = first_name

    @last_name.setter
    def last_name(self, last_name: str):
        self._last_name = last_name

    @day_of_birth.setter
    def day_of_birth(self, day_of_birth: date):
        self._day_of_birth = day_of_birth

class Employee(Person):
    def __init__(self, first_name: str, last_name: str, day_of_birth: date, salary: int = 1000):
        day_of_birth = self.check_birthsday(day_of_birth)
        super().__init__(first_name, last_name, day_of_birth)
        self._salary = salary

    @staticmethod
    def check_birthsday(day_of_birth: date):
        if not 1900 <= day_of_birth.year <= 2020:
            day_of_birth = 0
        return day_of_birth

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def day_of_birth(self):
        return self._day_of_birth

    @property
    def salary(self):
        return self._salary

    @first_name.setter
    def first_name(self, first_name: str):
        self._first_name = first_name

    @last_name.setter
    def last_name(self, last_name: str):
        self._last_name = last_name

    @day_of_birth.setter
    def day_of_birth(self, day_of_birth: date):
        self._day_of_birth = self.check_birthsday(day_of_birth)

    def who_i_am(self):
        return f"I'm {self._first_name} {self._last_name} and I earn {self._salary}zl"
