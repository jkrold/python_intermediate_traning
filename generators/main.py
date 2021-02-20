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
    return result

def main():
    print(iterator_ex_2(1000000))


if __name__ == '__main__':
    main()