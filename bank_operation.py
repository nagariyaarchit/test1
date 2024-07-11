class bank:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
    def Deposit(self, money_to_deposit):
        self.balance += money_to_deposit
    def withdrawal(self, money_to_withdraw):
        if self.balance < money_to_withdraw:
            print("")
            print("Transaction has been cancelled because there is not enough money for you to withdraw")
            print("")
        else:
            self.balance = self.balance - money_to_withdraw
    def check_balance(self):
        return self.balance

a = bank("Archit",0)
name = "Archit"
bank_account_list = []
bank_account_list.append(name)

while True:
    print("If you wish to check your bank balance press 1")
    print("If you wish to deposit money press 2")
    print("if you wish to withdraw money press 3")
    print("If you wish to quit press 4")
    print("If you wish to open a bank account press 5")
    print("")

    choice = int(input("Please pick an option:"))

    if choice == 1:
        x = a.check_balance()
        print("Your bank balance has this much amount:$",x)
        print("")
    if choice == 2:
        money_to_deposit = int(input("How much money would you like to deposit:$"))
        y = a.Deposit(money_to_deposit)
    if choice == 3:
        money_to_withdraw = int(input("How much money would you like to withdraw:$"))
        z = a.withdrawal(money_to_withdraw)
    if choice == 4:
        break
    if choice == 5:
        new_bank_account = input("Enter the new bank account name")
        x = str(new_bank_account)
        bank_account_list.append(x)
