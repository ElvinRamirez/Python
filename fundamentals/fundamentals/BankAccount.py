class BankAccount:
    accounts = []
    # don't forget to add some default values for these parameters!
    def __init__(self): 
        self.int_rate = 0.05
        self.balance = 0
        BankAccount.accounts.append(self)
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self
        # your code here
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds: Charging a $5 fee")
            self.balance = self.balance - 5
        else:
            self.balance = self.balance - amount
        return self

    def display_account_info(self):
        print(self.balance)
        # your code here
    def yield_interest(self):
        self.balance = self.balance * self.int_rate + self.balance
        return self
        # your code here
    
    @classmethod
    def all_accounts(cls):
            for account in cls.accounts:
                account.display_account_info()

            

account1 = BankAccount()
account2 = BankAccount()

account1.deposit(200).deposit(500).deposit(700).withdraw(800).yield_interest().display_account_info()
account2.deposit(200).deposit(500).withdraw(800).withdraw(800).withdraw(800).withdraw(800).yield_interest().display_account_info()
BankAccount.all_accounts()
