import json
import os

class ExpenseTracker:
    def __init__(self):# Corrected from _init to _init_
        # Load previous data or initialize an empty list if no file exists
        self.transactions = self.load_data()

    def load_data(self):
        """Load transactions from a JSON file if available."""
        if os.path.exists("transactions.json"):
            with open("transactions.json", "r") as file:
                return json.load(file)
        else:
            return []

    def save_data(self):
        """Save the transactions to a JSON file."""
        with open("transactions.json", "w") as file:
            json.dump(self.transactions, file)

    def add_income(self, amount):
        """Add income to the transactions."""
        transaction = {"type": "Income", "amount": amount}
        self.transactions.append(transaction)
        self.save_data()
        print(f"Income of ${amount} added successfully.")

    def add_expense(self, amount):  # Indentation fixed
        """Add expense to the transactions."""
        transaction = {"type": "Expense", "amount": amount}
        self.transactions.append(transaction)
        self.save_data()
        print(f"Expense of ${amount} added successfully.")

    def view_balance(self):
        """Calculate and display the current balance."""
        income = sum(t["amount"] for t in self.transactions if t["type"] == "Income")
        expense = sum(t["amount"] for t in self.transactions if t["type"] == "Expense")
        balance = income - expense
        print(f"Current Balance: ${balance}")

    def view_transactions(self):
        """View all income and expense transactions."""
        if not self.transactions:
            print("No transactions recorded.")
        else:
            print("\nTransactions:")
            for t in self.transactions:
                print(f"{t['type']}: ${t['amount']}")

    def menu(self):
        """Display the menu and handle user inputs."""
        while True:
            print("\nSimple Expense Tracker")
            print("1. Add Income")
            print("2. Add Expense")  # Indentation fixed
            print("3. View Balance")
            print("4. View Transactions")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                try:
                    amount = float(input("Enter income amount: $"))
                    if amount > 0:
                        self.add_income(amount)
                    else:
                        print("Amount must be positive.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

            elif choice == "2":
                try:
                    amount = float(input("Enter expense amount: $"))
                    if amount > 0:
                        self.add_expense(amount)
                    else:
                        print("Amount must be positive.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

            elif choice == "3":
                self.view_balance()

            elif choice == "4":  # Indentation fixed
                self.view_transactions()

            elif choice == "5":
                print("Exiting the application. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

            input("\nPress Enter to continue...")

if __name__ == "__main__":  # Corrected from _name and main to _name_ and _main_
    tracker = ExpenseTracker()
    tracker.menu()
