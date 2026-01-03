class ExpenseManager:
    def __init__(self):
        self.expenses = []
    def add(self, expense):
        self.expenses.append(expense)
    def all(self):
        return self.expenses
    def search(self, keyword):
        return [
            e for e in self.expenses
            if keyword.lower() in e.category.lower()
            or keyword.lower() in e.description.lower()
        ]
