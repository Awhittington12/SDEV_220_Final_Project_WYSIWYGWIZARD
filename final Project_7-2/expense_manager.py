from expense import Expense


class ExpenseManager:


    def __init__(self):

        self.expenses = []

    def add_expense(self, name, amount, category):

        expense = Expense(name, amount, category)
        self.expenses.append(expense)

    def get_expenses(self):

        return self.expenses

    def total_spent(self):

        total = 0

        for expense in self.expenses:
            total += expense.amount

        return total