import pickle


def pickle_write(items: list):
    try:
        with open('./data.pickle', 'wb') as fd:
            pickle.dump(items, fd)
            print(pickle.dumps(items))
    except (IOError, Exception) as e:
        print(f'Exception while writing pickle format: {e.args}')


def pickle_read():
    string_list = []
    try:
        with open('./data.pickle', 'rb') as fd:
            string_list = pickle.load(fd)
    except (IOError, Exception) as e:
        print(f'Exception while writing pickle format: {e.args}')
    return string_list


