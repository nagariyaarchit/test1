class Bank:
    def __init__(self):
        self.account_ledger = {}

    def deposit(self, account_holder_name, money_to_deposit):
        if account_holder_name in self.account_ledger:
            self.account_ledger[account_holder_name] += money_to_deposit
        else:
            self.account_ledger[account_holder_name] = money_to_deposit

    def withdrawal(self, account_holder_name, money_to_withdraw):
        if account_holder_name in self.account_ledger:
            if self.account_ledger[account_holder_name] >= money_to_withdraw:
                self.account_ledger[account_holder_name] -= money_to_withdraw
            else:
                print("Transaction has been cancelled because there is not enough money to withdraw.")
        else:
            print("Account not found.")

    def check_balance(self, account_holder_name):
        if account_holder_name in self.account_ledger:
            return self.account_ledger[account_holder_name]
        else:
            print("Account not found.")
            return None

    def open_account(self, account_holder_name, initial_balance):
        print(f"Opening account for {account_holder_name} with initial balance of {initial_balance}")
        self.account_ledger[account_holder_name] = initial_balance


# Interactive interface to use the Bank class
bank = Bank()

while True:
    print("")
    print("Choose an option:")
    print("1. Open a bank account")
    print("2. Deposit money into a bank account")
    print("3. Withdraw money from a bank account")
    print("4. Check the balance of a bank account")
    print("5. Quit")

    choice = int(input("Enter your choice (1-5):"))

    if choice == 1:
        account_holder_name = input("Enter account holder name: ")
        initial_balance = float(input("Enter initial balance: "))
        bank.open_account(account_holder_name, initial_balance)
        print("Account opened successfully!")

    elif choice == 2:
        account_holder_name = input("Enter account holder name: ")
        money_to_deposit = float(input("Enter amount to deposit: "))
        bank.deposit(account_holder_name, money_to_deposit)
        print("Deposit successful!")

    elif choice == 3:
        account_holder_name = input("Enter account holder name: ")
        money_to_withdraw = float(input("Enter amount to withdraw: "))
        bank.withdrawal(account_holder_name, money_to_withdraw)

    elif choice == 4:
        account_holder_name = input("Enter account holder name: ")
        balance = bank.check_balance(account_holder_name)
        if balance is not None:
            print(f"Balance for {account_holder_name}: {balance}")

    elif choice == 5:
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
