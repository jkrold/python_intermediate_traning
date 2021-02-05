from python_intermediate_traning.sda_exercises_oop_1.cat import Cat
from python_intermediate_traning.sda_exercises_oop_1.dog import Dog


class Vet:
    def sayCatHello(self, feline_patient: Cat):
        print(f"Hello {feline_patient.name}")

    def sayDogHello(self, canine_patient: Dog):
        print(f"Hello {canine_patient.name}")