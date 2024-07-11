class bank:
    def __init__(self,name):
        self.name = name
        self.balance = 0
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

x = "Archit"
name = bank(x)
bank_account_list = []
bank_account_list.append(x)
accounts_made = []
accounts_made.append(name)

while True:
    choice1 = int(input("If you wish to open a bank account press 1 if not press 2:"))
    if choice1 == 1:
        new_name = input("Please enter the name of the new bank account:")
        bank_account_list.append(new_name)
        y =  (len(bank_account_list)-1)
        new_account = bank(bank_account_list[y])
        accounts_made.append(new_account)
    else:
        print("These are the lists of bank accounts available right now\n:",bank_account_list)
        choice2 = input("please type in the name of the bank account you would like to open:")
        for i in range (0,len(bank_account_list)):
            if choice2 == bank_account_list[i]:
                z = i
        print("If you wish to check your bank balance press 1")
        print("If you wish to deposit money press 2")
        print("if you wish to withdraw money press 3")
        print("If you wish to quit press 4")
        print("")

        choice = int(input("Please pick an option:"))

        if choice == 1:
            x = accounts_made[z].check_balance()
            print("Your bank balance has this much amount:$",x)
            print("")
        if choice == 2:
            money_to_deposit = int(input("How much money would you like to deposit:$"))
            y = accounts_made[z].Deposit(money_to_deposit)
        if choice == 3:
            money_to_withdraw = int(input("How much money would you like to withdraw:$"))
            z = accounts_made[z].withdrawal(money_to_withdraw)
        if choice == 4:
            break
        
