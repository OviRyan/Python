class InsufficientFundsError(Exception):
    def __init__(self, message="Not enough cash, pal!"):
        super().__init__(message)

class BankAccount:
    def __init__(self, balance, min_balance):
        self.balance = balance
        self.min_balance = min_balance

    def withdraw(self, amount):
        if self.balance - amount < self.min_balance:
            raise InsufficientFundsError("Broke alert! Can't go below the limit.")
        self.balance -= amount
        print(f"Done! New balance: ${self.balance}")

# Example usage
account = BankAccount(balance=1000, min_balance=200)

try:
    account.withdraw(500)  # Valid withdrawal
    account.withdraw(400)  # This will raise an exception
except InsufficientFundsError as e:
    print(e)
