class Customer:
    def __init__(self, name):
        self.name = name

class Account:
    def __init__(self, customer, balance = 0):
        self.customer = customer
        self.balance = balance        

    def deposit(self, amount):
        self.balance += amount
        print(f"Rs. {amount} deposit successfully!")
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Rs: {amount} is withdrawn successfully!")
        else: 
            print("Insufficient balance")             
    def display_balance(self):
        print(f"Current balance Rs:{self.balance}")
name = input("Enter Your name:")
customer = Customer(name)                
account = Account(customer)
print(f"Account created for: {customer.name}")
deposit_amount = float(input("Enter amount to deposit:"))
account.deposit(deposit_amount)
withdraw_amount = float(input("Enter amount to withdraw:"))
account.withdraw(withdraw_amount)
account.display_balance()