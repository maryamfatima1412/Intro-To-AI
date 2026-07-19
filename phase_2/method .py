class Wallet:
    def __init__(self, balance):
        self.__balance = balance

    def add_money(self, amount):
        self.__balance += amount

    def spend_money(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def show_balance(self):
        print(self.__balance)

w = Wallet(1000)

w.add_money(500)
w.show_balance()

w.spend_money(300)
w.show_balance()

w.spend_money(2000)