# from serialize.csv_training import csv_writer, csv_read
# from serialize.pickle_training import pickle_write, pickle_read

from serialize.json_training import json_to_file


def main():
    # abc = ['bread', 'butter', 'cola']
    # pickle_write(abc)
    # print(pickle_read())

    # users = [
    #     ('John', "Smith", 765438),
    #     ('Samuel', "Jackson", 668438)
    # ]
    #
    # # csv_writer(users)
    # print(csv_read())

    json_to_file()

if __name__ == "__main__":
    main()