class Bank:
    def __init__(self):
        self.__balance = 10000

    def show_balance(self):
        print("Balance:", self.__balance)

b1 = Bank()
b1.show_balance()
