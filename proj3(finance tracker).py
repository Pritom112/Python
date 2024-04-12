class FinanceManager:
    def __init__(self):
        self.balance = 0
        self.transactions = []

    def add_income(self, amount, description):
        self.balance += amount
        self.transactions.append((amount, description, 'Income'))

    def add_expense(self, amount, description):
        self.balance -= amount
        self.transactions.append((amount, description, 'Expense'))

    def view_balance(self):
        return self.balance

    def view_transactions(self):
        return self.transactions

    def save_transactions(self, filename):
        with open(filename, 'w') as file:
            for transaction in self.transactions:
                file.write(','.join(map(str, transaction)) + '\n')

    def load_transactions(self, filename):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    parts = line.strip().split(',')
                    self.transactions.append((float(parts[0]), parts[1], parts[2]))
        except FileNotFoundError:
            pass


def main():
    finance_manager = FinanceManager()
    finance_manager.load_transactions('transactions.txt')

    while True:
        print("\nFinance Management System")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Balance")
        print("4. View Transactions")
        print("5. Save Transactions")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter the income amount: "))
            description = input("Enter a description: ")
            finance_manager.add_income(amount, description)
            print("Income added successfully!")
        elif choice == '2':
            amount = float(input("Enter the expense amount: "))
            description = input("Enter a description: ")
            finance_manager.add_expense(amount, description)
            print("Expense added successfully!")
        elif choice == '3':
            print("Current Balance:", finance_manager.view_balance())
        elif choice == '4':
            transactions = finance_manager.view_transactions()
            print("\nTransactions:")
            for transaction in transactions:
                print("Type:", transaction[2], "| Amount:", transaction[0], "| Description:", transaction[1])
        elif choice == '5':
            finance_manager.save_transactions('transactions.txt')
            print("Transactions saved successfully!")
        elif choice == '6':
            print("Exiting Finance Management System.")
            finance_manager.save_transactions('transactions.txt')
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
