from sda_exercises_oop_1.cat import Cat


def main():
    pass

if __name__ == '__main__':

    cats_list = [Cat('Snow flake'), Cat('Salem'), Cat('Tiger'), Cat('Smokey')]
    for cat in cats_list:
        cat.make_sound()