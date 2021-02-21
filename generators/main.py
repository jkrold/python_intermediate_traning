from generators.exercise_3 import Iterable
from generators.exercise_4 import exercise_4


def iterator_ex_1():
    dictionary = {
        'a': 1,
        'b': 2,
        'c': 3
    }

    for key in dictionary.keys():
        print(key)

    for value in dictionary.values():
        print(value)

def numbers_creator(n):
    numbers_list = []
    for i in range(n):
        numbers_list.append(i)
    return numbers_list

def iterator_ex_2(n):
    print('Exercise_2')
    import sys
    numbers_list = numbers_creator(n)
    print(f'Size of list in bytes: {sys.getsizeof(numbers_list)}')
    result = sum(numbers_list)
    print(f'Size of list in bytes: {sys.getsizeof(result)}')
    print('End of Exercise_2')
    return result

def iterator_ex_3(n):
    print('Exercise_3')
    import sys
    my_iterator = Iterable(n)
    print(f'Size of list in bytes: {sys.getsizeof(my_iterator)}')
    result = sum(my_iterator)
    print(f'Size of list in bytes: {sys.getsizeof(my_iterator)}')
    print('End of Exercise_3')
    return result

def main():
    # print(iterator_ex_2(10000))
    # print(iterator_ex_3(10000))
    exercise_4()


if __name__ == '__main__':
    main()