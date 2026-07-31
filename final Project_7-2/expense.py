class Expense:
    def __init__(self, name, amount, category):
        self.name = name
        self.amount = float(amount)
        self.category = category

    def __str__(self):
        return f"{self.name} - ${self.amount:.2f} ({self.category})"