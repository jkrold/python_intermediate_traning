from time import sleep


def lazy_read_generator(fd, text_size=1024):
    while True:
        data = fd.read(text_size)
        if not data:
            break
        yield data

def exercise_4():
    print("exercise 4")
    with open("./loren_ipsem.txt","r") as fd:
        for part_line in lazy_read_generator(fd):
            print(part_line)
            sleep(2)