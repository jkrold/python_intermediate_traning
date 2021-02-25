from decimal import Decimal


class BankAccount():
    def __init__(self, name: str, balance: Decimal):
        self.__name = name
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def __repr__(self):
        return f"Name: {self.__name}"


acc_1 = BankAccount("acc1", Decimal(1000))
acc_2 = BankAccount("acc2", Decimal(4000))
acc_3 = BankAccount("acc3", Decimal(5000))
acc_4 = BankAccount("acc4", Decimal(7500))
acc_5 = BankAccount("acc5", Decimal(10000))

acc_lst = [acc_1, acc_2, acc_3, acc_4, acc_5]

filtered_lst = list(filter(lambda acc: acc if acc.balance > Decimal(4500) else None, acc_lst))
print(filtered_lst)

max_acc = max(acc_lst, key=lambda acc: acc.balance)
print(max_acc)