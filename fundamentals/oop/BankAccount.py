    # The BankAccount class should have a balance. When a new BankAccount instance is created, if an amount is given, the balance of the account should initially be set to that amount; otherwise, the balance should start at $0. The account should also have an interest rate in decimal format. For example, a 1% interest rate would be saved as 0.01. The interest rate should be provided upon instantiation. (Hint: when using default values in parameters, the order of parameters matters!)

class BankAccount():
    # NINJA BONUS: use a classmethod to print all instances of a Bank Account's info
    all_instances =  []


    def __init__(self,int_rate, balance = 0): #balance will default to zero if no amount is given
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_instances.append(self)

    def deposit(self, amount):
        # Deposit money into the account
        self.balance += amount
        return self

    def withdraw(self, amount):
        # Method to withdraw money from the account
        if (self.balance - amount) > 0:
        # Decrease the account balance by the withdrawal amount
            self.balance -= amount
        else: 
            print(f'Sorry, but you do not have enough funds to withdraw money. Your balance: {self.balance}')
        return self

    def display_account_info(self):
        # Method to display the account's current balance
        print(self.balance)
        return self

    def yield_interest(self):
        # Method to calculate and add interest to the account balance
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        else: 
            print('Your account balance is negative')
            return self


    @classmethod
    def print_instances(cls):
        # Class method to print information for all created accounts
        for i in cls.all_instances:
            print(i.display_account_info())

# Create two bank accounts
christian = BankAccount(.2, 100)
daniela = BankAccount(0.5, 200)

# Print information for all accounts
BankAccount.print_instances()


christian.deposit(100).deposit(100).deposit(100).withdraw(200).yield_interest().display_account_info()
daniela.deposit(200).deposit(200).withdraw(50).withdraw(50).withdraw(20).withdraw(20).yield_interest().display_account_info()