import pickle


def pickle_write(items: list):
    try:
        with open('./data.pickle', 'wb') as fd:
            pickle.dump(items, fd)
            print(pickle.dumps(items))
    except (IOError, Exception) as e:
        print(f'Exception while writing pickle format: {e.args}')