from CustomerDetails import CustomerAccount
from decimal import Decimal

class BankAccount(CustomerAccount):
    def withdraw(self):
        amount = Decimal(input('Please enter amount you would like to withdraw: '))
        if amount > self.account_balance:
            print('There are insufficient funds in your account')
        else:
            self.account_balance -= amount
            print(f'Your account now has ${self.account_balance: .2f} in funds')
    def deposit(self):
        amount = Decimal(input('Please enter amount you would like to deposit: '))
        self.account_balance += amount
        print(f'Your account now has ${self.account_balance: .2f} in funds')