from Recap.Generators.case_1 import Iterator

def main():
    suma = Iterator(15)
    print(suma.sum)

    for elem in suma:
        print(suma.sum)

    print(suma.sum)

if __name__ == '__main__':
    main()