from datetime import date

from python_intermediate_traning.sda_exercises_oop_2.Person import Person, Employee

if __name__ == "__main__":
    person = Person("Jan", "Kowalski", date(1990, 10, 2))
    print(person)

    print(person.first_name)
    person.first_name = 'Tomasz'
    print(person.first_name)

    employee = Employee("Jan", "Kowalski", date(1890, 10, 2))
    print(employee.day_of_birth)
    print(employee.who_i_am())
