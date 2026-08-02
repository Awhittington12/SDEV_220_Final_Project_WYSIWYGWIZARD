"""
expense_manager.py

Responsible for storing and manipulating expenses.
"""

from expense import Expense


class ExpenseManager:

    def __init__(self):

        # Collection #1
        self.expenses = []

    def add_expense(self, name, amount, category):

        expense = Expense(name, amount, category)
        self.expenses.append(expense)

    def delete_expense(self, index):

        if 0 <= index < len(self.expenses):
            del self.expenses[index]

    def edit_expense(self, index, name, amount, category):

        if 0 <= index < len(self.expenses):

            self.expenses[index].name = name
            self.expenses[index].amount = float(amount)
            self.expenses[index].category = category

    def total_spent(self):

        return sum(exp.amount for exp in self.expenses)

    def category_totals(self):

        # Collection #2
        totals = {}

        for exp in self.expenses:

            if exp.category not in totals:
                totals[exp.category] = 0

            totals[exp.category] += exp.amount

        return totals