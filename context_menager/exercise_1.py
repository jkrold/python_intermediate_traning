from contextlib import contextmanager


@contextmanager
def open_file(path: str, mode='a'):
    print("opening file")
    fd = open(path, mode)
    yield fd
    fd.close()
    print('closing file')

def exercise_1():
    try:
        with open_file('./test.txt') as fd:
            fd.write('Przykladowy tekst')
    except IOError as e:
        print(f"We have an error: {e.args}")
