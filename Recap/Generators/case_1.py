class Iterator:
    def __init__(self, n: int):
        self.n = n
        self.suma = 0
        self.number = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.number += 1
        if self.number == self.n - 1:
            raise StopIteration
        self.suma += self.number
        return self.suma

    @property
    def sum(self):
        return self.suma