from python_intermediate_traning.sda_exercises_oop_1.Animal import Animal
from python_intermediate_traning.sda_exercises_oop_1.cat import Cat
from python_intermediate_traning.sda_exercises_oop_1.dog import Dog


class Vet:
    def say_hello(self, patient: Animal):
        print(f"Hello {patient.name}")
