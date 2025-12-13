"""10. BankAccount Class 
● Create a class BankAccount with private balance. 
● Add methods deposit(), withdraw(), and get_balance(). 
● Ensure withdraw() does NOT allow negative balance. 
● Test by attempting an invalid withdrawal."""

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount

    def get_balance(self):
        return self.balance

acc = BankAccount(100)
acc.deposit(50)
print(acc.get_balance())
acc.withdraw(150)  