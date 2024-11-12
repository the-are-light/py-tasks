class BankAccount:
    def __init__(self, balance=0): self.__balance = balance
    def get_balance(self): return self.__balance
    def deposit(self, amount): self.__balance += amount
    def withdraw(self, amount):
        if amount <= self.__balance: self.__balance -= amount
        else: raise ValueError("На счете недостаточно средств")

    def transfer(self, account, amount):
        if amount <= self.__balance:
            account.deposit(amount)
            self.__balance -= amount
        else: raise ValueError("На счете недостаточно средств")