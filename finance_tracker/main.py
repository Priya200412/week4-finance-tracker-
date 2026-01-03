from finance_tracker.expense import Expense
from finance_tracker.expense_manager import ExpenseManager
from finance_tracker import file_handler, reports


class FinanceTracker:
    def __init__(self):
        self.manager = ExpenseManager()
        self.manager.expenses = file_handler.load()

    def run(self):
        print("=" * 60)
        print("          PERSONAL FINANCE TRACKER")
        print("=" * 60)

        try:
            while True:
                print("\n" + "=" * 40)
                print("              MAIN MENU")
                print("=" * 40)
                print("1. Add New Expense")
                print("2. View All Expenses")
                print("3. Search Expenses")
                print("4. Generate Monthly Report")
                print("5. View Category Breakdown")
                print("6. Set/Update Budget")
                print("7. Export Data to CSV")
                print("8. View Statistics")
                print("9. Backup/Restore Data")
                print("0. Exit")
                print("=" * 40)

                choice = input("\nEnter your choice (0-9): ").strip()

                if choice == "1":
                    self.add_expense()
                elif choice == "2":
                    self.view_expenses()
                elif choice == "3":
                    self.search_expenses()
                elif choice == "4":
                    self.generate_monthly_report()
                elif choice == "5":
                    self.view_category_breakdown()
                elif choice == "6":
                    self.set_budget()
                elif choice == "7":
                    self.export_data()
                elif choice == "8":
                    self.view_statistics()
                elif choice == "9":
                    self.backup_restore()
                elif choice == "0":
                    print("\n" + "=" * 60)
                    print("Thank you for using Personal Finance Tracker!")
                    print("=" * 60)
                    break
                else:
                    print("Invalid choice! Please enter 0-9.")

        except KeyboardInterrupt:
            print("\n" + "=" * 60)
            print("Program interrupted by user. Exiting safely.")
            print("=" * 60)

    # ---------------- MENU FUNCTIONS ---------------- #

    def add_expense(self):
        print("\n--- ADD NEW EXPENSE ---")
        try:
            date = input("Enter date (YYYY-MM-DD): ")
            amount = input("Enter amount: ")
            category = input("Enter category: ")
            description = input("Enter description: ")

            expense = Expense(date, amount, category, description)
            self.manager.add(expense)

            # Save to JSON
            file_handler.save(self.manager.all())

            print("Expense added successfully!")

        except KeyboardInterrupt:
            print("\nInput cancelled by user.")
        except Exception as e:
            print("Error:", e)

    def view_expenses(self):
        print("\n--- ALL EXPENSES ---")
        if not self.manager.all():
            print("No expenses found.")
            return
        for i, e in enumerate(self.manager.all(), start=1):
            print(f"{i}. {e.date} | ₹{e.amount} | {e.category} | {e.description}")

    def search_expenses(self):
        print("\n--- SEARCH EXPENSES ---")
        keyword = input("Enter keyword: ")
        results = self.manager.search(keyword)
        if not results:
            print("No matching expenses found.")
            return
        for e in results:
            print(f"{e.date} | ₹{e.amount} | {e.category} | {e.description}")

    def generate_monthly_report(self):
        print("\n--- MONTHLY REPORT ---")
        report = reports.monthly(self.manager.all())
        if not report:
            print("No data available.")
            return
        for month, total in report.items():
            print(f"{month} : ₹{total}")

    def view_category_breakdown(self):
        print("\n--- CATEGORY BREAKDOWN ---")
        report = reports.category(self.manager.all())
        if not report:
            print("No data available.")
            return
        for cat, total in report.items():
            print(f"{cat} : ₹{total}")

    def set_budget(self):
        print("\n--- SET/UPDATE BUDGET ---")
        print("Budget feature can be extended further.")
        print("Budget set successfully!")

    def export_data(self):
        print("\n--- EXPORT DATA ---")

        print("DEBUG → Expenses in memory:", len(self.manager.all()))

        if not self.manager.all():
            print("No expenses to export.")
            return

        file_handler.export_csv(self.manager.all())
        print("Data exported to CSV successfully!")

    def view_statistics(self):
        print("\n--- STATISTICS ---")
        stats = reports.stats(self.manager.all())
        if not stats:
            print("No statistics available.")
            return
        for k, v in stats.items():
            print(f"{k} : ₹{v}")

    def backup_restore(self):
        print("\n--- BACKUP/RESTORE ---")

        if not self.manager.all():
            print("No expenses to backup.")
            return

        file_handler.backup(self.manager.all())
        print("Backup completed successfully!")
