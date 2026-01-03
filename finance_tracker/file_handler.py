import json
import csv
import os
from finance_tracker.expense import Expense
DATA_FILE = "data/expenses.json"
EXPORT_DIR = "data/exports"
BACKUP_DIR = "data/backup"
def save(expenses):
    os.makedirs("data", exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump([e.to_dict() for e in expenses], f, indent=4)
def load():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            return []
    expenses = []
    for d in data:
        expenses.append(
            Expense(d["date"], d["amount"], d["category"], d["description"])
        )
    return expenses
def export_csv(expenses):
    os.makedirs(EXPORT_DIR, exist_ok=True)
    with open(f"{EXPORT_DIR}/expenses.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "Amount", "Category", "Description"])

        for e in expenses:
            writer.writerow([
                e.date.strftime("%Y-%m-%d"),
                e.amount,
                e.category,
                e.description
            ])
def backup(expenses):
    os.makedirs(BACKUP_DIR, exist_ok=True)
    with open(f"{BACKUP_DIR}/backup.json", "w") as f:
        json.dump([e.to_dict() for e in expenses], f, indent=4)
