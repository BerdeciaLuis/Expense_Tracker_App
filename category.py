#This class will be handling the categories and expenses added to the category for the budget

class Category:

    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
        self.expenses = []

    
    def remaining_budget(self):
        return self.budget - self.total_expenses()
    
    def add_expense(self, amount, description=""):
        self.expenses.append((amount, description))

    def total_expenses(self):
        return sum(amount for amount, _ in self.expenses)
    
    def __str__(self):
        return f"Category: {self.name}, Budget: {self.budget}, Spent: {self.total_expenses()}, Remaining: {self.remaining_budget()}"
    
    
