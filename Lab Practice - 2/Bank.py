class Bank:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        try:
            if amount > self.balance:
                raise ValueError("Insufficient funds!")
            self.balance -= amount
            print(f"Withdrawal successful! Remaining balance: {self.balance}")
        except ValueError as e:
            print(f"Error: {e}")


account = Bank(100)  
account.withdraw(50)  
account.withdraw(100)  