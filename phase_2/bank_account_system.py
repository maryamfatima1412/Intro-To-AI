from abc import ABC

class Account(ABC):
    bank_name = "ABC Bank"

    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid balance")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited successfully.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn successfully.")
        else:
            print("Insufficient Balance")

    def calculate_interest(self):
        return 0

    def __str__(self):
        return f"""
Bank: {self.bank_name}
Account Number: {self.account_number}
Holder: {self.holder_name}
Balance: {self.balance}
"""

class SavingsAccount(Account):

    def calculate_interest(self):
        return self.balance * 0.05

    def withdraw(self, amount):
        super().withdraw(amount)

class CurrentAccount(Account):

    def calculate_interest(self):
        return self.balance * 0.02

    def withdraw(self, amount):
        if amount <= self.balance + 1000:
            self.balance -= amount
            print(f"{amount} withdrawn successfully.")
        else:
            print("Overdraft Limit Exceeded")

account1 = SavingsAccount("S101", "Maryam", 5000)
account2 = CurrentAccount("C201", "Ali", 3000)

print(account1)
account1.deposit(1000)
account1.withdraw(2000)
print("Interest:", account1.calculate_interest())
print(account1)

print(account2)
account2.deposit(500)
account2.withdraw(3500)
print("Interest:", account2.calculate_interest())
print(account2)