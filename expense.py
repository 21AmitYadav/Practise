class Expense:
    def __init__(self, amount, category, date):
        self.amount = amount
        self.category = category
        self.date = date

def add_expense(expenses, amount, category, date):
    expenses.append(Expense(amount, category, date))
    print("Expense added successfully.")

def view_expenses(expenses):
    for expense in expenses:
        print(f"Amount: {expense.amount}, Category: {expense.category}, Date: {expense.date}")

def main():
    expenses = []
    while True:
        print("\nExpense Tracking System")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter expense amount: "))
            category = input("Enter expense category: ")
            date = input("Enter expense date (YYYY-MM-DD): ")
            add_expense(expenses, amount, category, date)
        elif choice == "2":
            print("\nExpense List:")
            view_expenses(expenses)
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
