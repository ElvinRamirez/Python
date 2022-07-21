class BankAccount:
    accounts = []
    # don't forget to add some default values for these parameters!
    def __init__(self,int_rate,checking_balance,savings_balance): 
        self.int_rate = int_rate
        self.checking_balance = checking_balance
        self.savings_balance = savings_balance
        BankAccount.accounts.append(self)
        
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, checking_amount,savings_amount):
                self.checking_balance = self.checking_balance + checking_amount   
                self.savings_balance = self.savings_balance + savings_amount
                return self            
        # selection = input("To which account would you like to deposit?:")
        # if selection == "checking":
        #     amount = int(input("How much would you like to deposit?:"))
        #     self.checking_balance = self.checking_balance + amount
        #     print(self.checking_balance)
        #     return self
        # elif selection == "savings":#need to then get the amount entered on line amount inputted, and add it to savings
        #     amount = int(input("How much would you like to deposit?:"))
        #     self.savings_balance = self.savings_balance + amount
        #     return self   
        #else:#this else is not working
            #exit
        
        
        # your code here
    def withdraw(self,checking_amount,savings_amount):
                self.checking_balance = self.checking_balance - checking_amount   
                self.savings_balance = self.savings_balance - savings_amount
                return self 
        # selection = input("From which account would you like to withdraw?:")
        # if selection == "checking":
        #     amount = int(input("How much would you like to withdraw?:"))
        #     if amount > self.checking_balance:
        #         print("Insufficient funds: Charging a $5 fee")
        #         self.checking_balance = self.checking_balance - 5
        #     else:
        #         print("Transfer successful")
        #         self.checking_balance = self.checking_balance - amount
        # elif selection == "savings":
        #     amount = int(input("How much would you like to withdraw?:"))
        #     if amount > self.savings_balance:
        #         print("Insufficient funds: Charging a $5 fee")
        #         self.savings_balance = self.savings_balance - 5
        #     else:
        #         print("Transfer successful")
        #         self.savings_balance = self.savings_balance - amount    
        # else:
        #     print("incorrect selection")
        #     return self

    def display_account_info(self):
        return f"{self.checking_balance}{self.savings_balance}"
        
        # your code here
    def yield_interest(self):
        self.balance = self.balance * self.int_rate + self.balance
        return self
        # your code here
    
    @classmethod
    def all_accounts(cls):
            for account in cls.accounts:
                account.display_account_info()

#account1 = BankAccount(0.8,0,0)
#account2 = BankAccount(0.5,0,0)


class User:
    def __init__(self, first_name, last_name, email, age):
        #self.account = super().__init__(0.05)
        self.account = BankAccount(0.5,0,0)
        self.first_name = first_name#
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        
    def enroll(self):
        if  self.is_rewards_member == True:
            print("User is already a member")
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
        return self   
        
    def spend_points(self, amount):
        if amount > self.gold_card_points:
            print("Sorry, you do not have enough balance to cover this transaction")
        else:
            self.gold_card_points = self.gold_card_points - amount
            print(self.gold_card_points)       

    def display_info(self):
        print(f"Name: {self.first_name} \nLast Name: {self.last_name} \nEmail: {self.email} \nAge: {self.age}")
        return self

    def make_deposit(self,checking_amount,savings_amount):
        self.account.deposit(checking_amount,savings_amount)
        return self    
    
    def make_withdraw(self,checking_amount,savings_amount):
        self.account.withdraw(checking_amount,savings_amount)
        return self
    
    def display_user_balance(self):#this will need a for loop to display multiple user balances
        print(f"User: {self.first_name},\n Checking balance: {self.account.checking_balance},\n Savings balance:{self.account.savings_balance}")
    
    # def transfer_money(self,checking_amount,savings_amount):#takes self checking amoun, self savings amount, users checking & savings                
    #             User = BankAccount
    #             self.checking_balance = self.checking_balance - checking_amount   
    #             self.savings_balance = self.savings_balance - savings_amount
    #             john.checking_balance = john.checking_balance + checking_amount
    #             john.savings_balance = john.savings_balance - savings_amount
    #             return self
    #     amount = input("How much would you like to transfer?:")
    #     my_account = input("From which account would you like to transfer?:")
    #     if my_account == "checking":
    #         other_account = input("To which account would you like to transfer?:")
    #         if other_account == "checking":
    #             #user1 = input(User(f"Enter receiving user:"))
    #             self.account.checking_balance -= int(amount)
    #             transfer_user.checking_balance += int(amount)
    #             transfer_user.display_user_balance
    #             return self     
elvin = User("Elvin", "Ramirez", "Elvin.Ramirez31293@gmail.com", 28)
john = User("John", "Doe", "john.doe@gmail.com", 29)
terry = User("Terry", "Black", "Terry.Back@gmail.com",42)

#elvin.display_info().enroll().spend_points(50)
#elvin.make_deposit(0)
#john.make_deposit(0)
#john.display_user_balance()
#elvin.make_withdraw(0)
#elvin.display_user_balance()

john.make_deposit(200,150)
john.display_user_balance()
elvin.make_deposit(190,800)
elvin.make_withdraw(45,20)
#elvin.transfer_money(150,0)
elvin.display_user_balance()











