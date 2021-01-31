from sda_exercises_oop_1.cat import Cat
from sda_exercises_oop_1.dog import Dog

if __name__ == '__main__':

    cats_list = [Cat('Snow flake'), Cat('Salem'), Cat('Tiger'), Cat('Smokey')]
    for cat in cats_list:
        sound: str = cat.make_sound()
        print(sound)

    for i in range(0, 4):
        cat1_num_of_eaten_mice = cats_list[0].eat_mouse()

    for i in range(0, 2):
        cat2_num_of_eaten_mice = cats_list[1].eat_mouse()

    for i in range(0, 5):
        cat3_num_of_eaten_mice = cats_list[2].eat_mouse()

    for i in range(0, 1):
        cat4_num_of_eaten_mice = cats_list[3].eat_mouse()

    print(cat1_num_of_eaten_mice)
    print(cat2_num_of_eaten_mice)
    print(cat3_num_of_eaten_mice)
    print(cat4_num_of_eaten_mice)

    dog1 = Dog("Rex")
    dog1_sound = dog1.make_sound()
    print(dog1_sound)