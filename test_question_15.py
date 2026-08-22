class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
    def deposit(self, amount):
        self.balance +=amount
        print("Deposited:", amount)
        print("Current balance:", self.balance)
    def withdraw(self, amount):
        if amount<=self.balance:
            self.balance -=amount
            print("Withdrawn", amount)
        else:
            print("Insufficient funds")
            print("Current balance", self.balance)
    def check_balance(self):
        print("Current balance:", self.balance)
name = input("Enter your name:")
account = BankAccount(name)
while True:
    choice = input("Do you want to deposit(1), withdraw(2), check(3) your balance?")
    if choice =="1":
        amount = float(input("Enter the amount to deposit"))
        account.deposit(amount)
    elif choice =="2":
        amount = float(input("Enter the amount to withdraw"))
        account.withdraw(amount)
    elif choice=="3":
        account.check_balance()
    else:
        print("Invalid choice, goodbye")
        break