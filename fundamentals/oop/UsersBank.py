
class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance, balance2): 
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
        self.int_rate = int_rate
        self.balance = 0
        self.balance2 = 0

    def deposit(self, amount, account):
        if account == "Checkings":
            self.balance += amount
        elif account == "Savings":
            self.balance2 +=amount
        return self

    def withdraw(self, amount, account):
        if account == "Checkings":
            if self.balance >= amount:
                self.balance -= amount
                return self
            else:
                print( "Insufficient Funds: Charging a $5 fee" )
                self.balance -= 5
                return self
        if account == "Savings":
            if self.balance2 >= amount:
                self.balance2 -= amount
                return self
            else:
                print( "Insufficient Funds: Charging a $5 fee" )
                self.balance2 -= 5
                return self

    def display_account_info(self):
        # print( f"Interest Rate: {self.int_rate}" )
        print( f"Checkings: ${self.balance}" )
        print( f"Savings: ${self.balance2}" )
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = (self.balance * self.int_rate) + self.balance
            return self
        return self

    def print_all_info( self ): 
        self.display_account_info()
        print( f"Interest Rate: {self.int_rate}" )
# User_bank_account 
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0, balance2=0)
    
    def display_user_balance(self):
        self.account.display_account_info()
    
    def make_deposit( self, amount, account ):
        self.account.deposit( amount, account )
        return self

    def make_withdrawal( self, amount, account ):
        self.account.withdraw( amount, account )
        return self

    def transfer_money( self, amount, other_user ):
        self.account.withdraw( amount, "Checkings" )
        other_user.account.deposit( amount, "Checkings" )
        return self
# Create a Users objects named 'sameh' and 'random'.
user1 = User( "sameh", "nasri.sameh2016@gmail.com" )
user2 = User( "Random", "randomemail@gmail.com" )
# Deposit $100 into sameh's checking account.
user1.make_deposit( 100, "Savings" ).make_deposit( 500, "Checkings" ).make_withdrawal( 200, "Checkings" ).make_withdrawal( 50, "Savings" ).transfer_money( 1, user2 ).display_user_balance()
user2.display_user_balance()




# account_kelvin = BankAccount( 0.01, 0 )
# account_random = BankAccount( 0.02, 0 )

# account_kelvin.deposit( 100 ).deposit( 200 ).deposit( 300 ).withdraw( 100 ).yield_interest().display_account_info()
# account_random.deposit( 100 ).deposit( 100 ).withdraw( 50 ).withdraw( 50 ).withdraw( 100 ).withdraw( 100 ).yield_interest().display_account_info().print_all_info()