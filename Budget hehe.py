class BudgetPlan:

    def __init__(self, category):
        self.category = category
        self.balance = 0
        self.transactions = []
        self.expenses = []
        self.savings_interest_rate = 0.02
        self.goals = {}

    def set_goals(self, goal):
        self.goals[self.category] = goal
        return self.goals

    def get_transactions(self):
        return self.transactions

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited {amount} into {self.category} budget.")
            print(f"Deposited {amount} into {self.category} budget.")
        else:
            print("Invalid deposit amount.")

    def transfer(self, other_category, amount):
        if self == other_category:
            print("Cannot transfer to the same category.")
            return

        if 0 < amount <= self.balance:
            self.balance -= amount
            other_category.balance += amount
            self.transactions.append(f"Transferred {amount} from {self.category} to {other_category.category} budget.")
            other_category.transactions.append(f"Transferred {amount} from {self.category} to {other_category.category} budget.")
            print(f"Transferred {amount} from {self.category} to {other_category.category} budget.")
        else:
            print("Invalid transfer amount or insufficient funds.")

    def add_expense(self, expense_name, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.expenses.append((expense_name, amount))
            print(f"Added expense '{expense_name}' of {amount} to {self.category} budget.")
        else:
            print("Invalid expense amount or insufficient funds.")

    def check_progress(self):
        goal_amount = self.goals.get(self.category, None)
        if goal_amount is not None:
            progress = (self.balance / goal_amount) * 100
            print(f"Progress for {self.category} goal: {progress:.2f}%")

    def apply_savings_interest(self):
        if self.category == 'savings':
            interest_earned = self.balance * self.savings_interest_rate
            self.balance += interest_earned
            self.transactions.append(f"Interest earned on savings: {interest_earned}")
            print(f"Interest earned on savings: {interest_earned}")
        else:
            print("Savings interest only applies to 'savings' category.")
