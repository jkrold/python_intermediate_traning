def case_1():
    list_of_numbers = [1, 5, 8, 10, 21]
    print("Case_1 before")
    try:
        result = list_of_numbers[5]
    except IndexError as ie:
        print(f'Exception cought {ie.args}')
    except Exception as exp:
        print(f'Exception cought {exp.args}')
    print("Case_1 after")

    try:
        result = list_of_numbers[5]
    except (IndexError, Exception) as e:
        print(f'Exception cought {e.args}')

def case_2(name: str):
    if len(name) <= 0:
        raise ValueError('Sting is empty')
    print(f'Given name is: {name}')