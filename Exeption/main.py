from python_intermediate_traning.Exeption.exercise import case_1, case_2, case_4, case_6


def main():
    # print("Start app:")
    # try:
    #     case_2("")
    # except Exception as e:
    #     print(f'Exception caught {e.args}')
    # print("Finish")

    # dictionary = {
    #     "product": ['butter', 'bread', 'tomato']
    # }
    #
    # try:
    #     case_4(dictionary)
    # except KeyError as k:
    #     print(f'Exception caught {k.args}')

    try:
        case_6()
    except NotImplementedError as n:
        print(f'Exception caught {n.args}')


if __name__ == "__main__":
    main()
