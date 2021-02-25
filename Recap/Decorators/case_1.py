def start_end_messages(func):
    def wrapper(*args, **kwargs):
        print('Before message')
        result = func(*args, **kwargs)
        print('After message')
        return result
    return wrapper

@start_end_messages
def print_hello():
    print('hello')

@start_end_messages
def print_text(text):
    print(text)