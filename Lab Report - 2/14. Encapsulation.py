class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
            else:
                print("Insufficient funds!")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        return self.__balance


account = BankAccount(100)

account.deposit(50)
print(f"Balance after deposit: {account.check_balance()}")

account.withdraw(200)
print(f"Balance after withdrawal attempt: {account.check_balance()}")

account.withdraw(120)
print(f"Balance after successful withdrawal: {account.check_balance()}")
