from decorators.case_2 import read_file


def main():
    # print_hello_world(1, 2)
    read_file(file_path='./abc.txt')

# def wrap_before_and_after(func):
#     def wrapper(*args, **kwargs):
#         print('Before')
#         result = func(*args, **kwargs)
#         print('After')
#         return result
#     return wrapper
#
# @wrap_before_and_after
# def print_hello_world(a, b):
#     print("Hello world!")
#     print(f'{a}, {b}')


if __name__ == '__main__':
    main()
