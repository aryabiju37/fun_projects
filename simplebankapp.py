import sys

class BankingApp:
    def __init__(self,bank_name):
        self.bank_name = bank_name
        print("Welcome to {}".format(self.bank_name))

class AccountCreation(BankingApp):
    def __init__(self,bank_name, Acc_holder_name,balance):
        super().__init__(bank_name)
        self.Acc_holder_name = Acc_holder_name
        if balance > 0:
            self.balance = balance
        else:
            print("deposits cannot be negative")

    def deposits(self,amount):
        self.balance += amount
        print(f"{self.balance} is your new balance")

    def withdraw(self,amount):
        if self.balance < amount:
            print("insufficient funds")
        else:
            self.balance -= amount
            print(f"current balace is {self.balance}")

    def show_balance(self):
        print(f"The current balance is {self.balance}")

init_bank_name = input("Enter the bank name to create an Account with them: ")
Account_holder_name = input("Enter the account holder name : ")
init_balance = int(input("Enter the initial Account balance : "))

a = AccountCreation(init_bank_name,Account_holder_name,init_balance)

while True:
    i = input("Choose your operation: d-Deposit,w-withdraw,s-show Balance,e-Exit: ")
    if i == "d":
        d=int(input("enter the amount to be deposited: "))
        a.deposits(d)
    elif i == "w":
        w = int(input("Enter the amount to be withdrawn:"))
        a.withdraw(w)
    elif i == "s":
        a.show_balance()
    elif i == "e":
        sys.exit()
    else:
        print("please enter a valid input")    

        
