
class Budget:
    def __init__(self, category):
        self.category = category
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount} into {self.category} budget.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount} from {self.category} budget.")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def transfer(self, other_category, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            other_category.balance += amount
            print(f"Transferred ${amount} from {self.category} to {other_category.category} budget.")
        else:
            print("Invalid transfer amount or insufficient funds.")

    def get_balance(self):
        return self.balance

    def __repr__(self):
        return f"{self.category} budget balance: ${self.balance:.2f}"


if __name__ == "__main__":
    food_budget = Budget("Food")
    clothing_budget = Budget("Clothing")
    entertainment_budget = Budget("Entertainment")

    food_budget.deposit(1000)
    clothing_budget.deposit(500)
    entertainment_budget.deposit(800)

    print(food_budget)
    print(clothing_budget)
    print(entertainment_budget)

    food_budget.withdraw(200)
    clothing_budget.withdraw(100)
    entertainment_budget.withdraw(300)

    print(food_budget)
    print(clothing_budget)
    print(entertainment_budget)

    food_budget.transfer(clothing_budget, 300)
    print(clothing_budget)


