
import json
import os
from datetime import datetime


class Expense:
    def __init__(self, amount, category, description):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = datetime.now().strftime("%d-%m-%Y %H:%M")

    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
            "date": self.date
        }


class ExpenseTracker:
    def __init__(self, filename="expenses.json"):
        self.filename = filename
        self.expenses = []
        self.load_expenses()

    def load_expenses(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    self.expenses = json.load(file)
            except (json.JSONDecodeError, OSError):
                print("Could not load saved expenses.")

    def save_expenses(self):
        with open(self.filename, "w") as file:
            json.dump(self.expenses, file, indent=4)

    def add_expense(self):
        try:
            amount = float(input("Enter amount: "))

            if amount <= 0:
                print("Amount must be greater than zero.")
                return

            category = input("Enter category: ").strip()
            description = input("Enter description: ").strip()

            if not category:
                print("Category cannot be empty.")
                return

            expense = Expense(amount, category, description)
            self.expenses.append(expense.to_dict())
            self.save_expenses()

            print("Expense added successfully!")

        except ValueError:
            print("Please enter a valid amount.")

        except OSError:
            print("Could not save the expense.")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
            return

        for index, expense in enumerate(self.expenses, start=1):
            print(f"\nExpense ID: {index}")
            print(f"Amount: ₹{expense['amount']:.2f}")
            print(f"Category: {expense['category']}")
            print(f"Description: {expense['description']}")
            print(f"Date: {expense['date']}")

    def total_expenses(self):
        total = sum(expense["amount"] for expense in self.expenses)
        print(f"Total expenses: ₹{total:.2f}")

    def filter_by_category(self):
        category = input("Enter category to search: ").strip().lower()

        found = False

        for expense in self.expenses:
            if expense["category"].lower() == category:
                print(
                    f"₹{expense['amount']:.2f} - "
                    f"{expense['description']} - {expense['date']}"
                )
                found = True

        if not found:
            print("No expenses found in this category.")

    def delete_expense(self):
        self.view_expenses()

        if not self.expenses:
            return

        try:
            expense_id = int(input("Enter Expense ID to delete: "))

            if 1 <= expense_id <= len(self.expenses):
                deleted = self.expenses.pop(expense_id - 1)
                self.save_expenses()
                print(f"Deleted expense: {deleted['description']}")
            else:
                print("Invalid Expense ID.")

        except ValueError:
            print("Please enter a valid ID.")

        except OSError:
            print("Could not save the changes.")


def main():
    tracker = ExpenseTracker()

    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Filter by Category")
        print("5. Delete Expense")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            tracker.add_expense()
        elif choice == "2":
            tracker.view_expenses()
        elif choice == "3":
            tracker.total_expenses()
        elif choice == "4":
            tracker.filter_by_category()
        elif choice == "5":
            tracker.delete_expense()
        elif choice == "6":
            print("Thank you for using Expense Tracker!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
