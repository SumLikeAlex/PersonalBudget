def add_transaction():
    print("\n--- Add New Transaction ---")
    date = input("Enter date (YYYY-MM-DD): ")
    description = input("Enter description: ")

    while True:
        transaction_type = input("Is this an (1) Income, (2) Fixed Expense, or (3) Variable Expense? (1/2/3): ")
        if transaction_type in ('1', '2', '3'):
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount < 0:
                print("Please enter a positive number.")
            else:
                break
        except ValueError:
            print("Invalid amount. Please enter a number.")
    
    category = input("Enter a specific category (e.g., Salary, Rent, Groceries): ")

    if transaction_type == '1':
        category_label = f"Income ({category})"
    elif transaction_type == '2':
        amount = -abs(amount)
        category_label = f"Fixed ({category})"
    else: 
        amount = -abs(amount)
        category_label = f"Variable ({category})"

    new_transaction = {
        'date': date,
        'description': description,
        'amount': amount,
        'category': category_label
    }
    
    print("Transaction added successfully!")
    return new_transaction


def view_all_transactions(transactions):

    if not transactions:
        print("No transactions to display.")
        return

    print("\n--- All Transactions ---")
    print(f"{'Date':<12} {'Description':<25} {'Amount':>10} {'Category':<25}")
    print("-" * 72)

    for transaction in transactions:
        date = transaction['date']
        description = transaction['description']
        amount = f"{transaction['amount']:.2f}"
        category = transaction['category']
        
        print(f"{date:<12} {description:<25} {amount:>10} {category:<25}")


def view_budget_summary(transactions):
    if not transactions:
        print("No transactions to display.")
        return

    total_income = 0.0
    total_fixed_expenses = 0.0
    total_variable_expenses = 0.0
    
    for transaction in transactions:
        if "Income" in transaction['category']:
            total_income += transaction['amount']
        elif "Fixed" in transaction['category']:
            total_fixed_expenses += transaction['amount']
        elif "Variable" in transaction['category']:
            total_variable_expenses += transaction['amount']

    current_balance = total_income + total_fixed_expenses + total_variable_expenses

    print("\n--- Budget Summary ---")
    print(f"Total Income:           ${total_income:,.2f}")
    print(f"Total Fixed Expenses:   ${total_fixed_expenses:,.2f}")
    print(f"Total Variable Expenses:${total_variable_expenses:,.2f}")
    print("-" * 35)
    print(f"Current Balance:        ${current_balance:,.2f}")
    print("-" * 35)


def main_menu():
    transactions = []
    
    print("Welcome to the CLI Budget App!")

    while True:
        try:
            print("\n--- Main Menu ---")
            print("1. Add a new transaction")
            print("2. View Budget Summary")
            print("3. View all transactions")
            print("4. Exit")

            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                new_transaction = add_transaction()
                transactions.append(new_transaction)
            elif choice == '2':
                view_budget_summary(transactions)
            elif choice == '3':
                view_all_transactions(transactions)
            elif choice == '4':
                print("Goodbye!")
                break  
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except EOFError:
            break

if __name__ == "__main__":
    main_menu()
