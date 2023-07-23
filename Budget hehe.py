
class budgetplan:

    def __init__(self, category):
        self.category = category
        self.balance = 0

    def get_balance(self):
        return self.balance

    def __repr__(self):
        return f"{self.category} budget balance: ${self.balance:.2f}"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposited " + str(amount) + " into " + str(self.category) + " budget.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print("Withdrew " + str(amount) + " from " + str(self.category) + " budget.")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def transfer(self, other_category, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            other_category.balance += amount
            print("Transferred " + str(amount) + " from " + str(self.category) + " to " + str(other_category.category) + " budget.")
        else:
            print("Invalid transfer amount or insufficient funds.")
