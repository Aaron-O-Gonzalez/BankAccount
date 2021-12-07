from random import randint
from decimal import Decimal

'''Create a random nine digit number for customer account number'''
def generate_random_id():
    lower = 10**(9-1)
    upper = (10**9)-1
    return randint(lower, upper)


class CustomerAccount:
    def __init__(self, customer_input, firstName = None, lastName = None, address = None, city = None, state = None, zip = None, account_number = None, account_balance =0):
        self.customer_input = customer_input

        if int(self.customer_input) == 3:
            self.firstName = firstName =  input('Please enter your first name: ')
            self.lastName = lastName = input('Please enter your last name: ') 
            self.address = address = input('Please enter your address: ')
            self.city = city = input('Please enter your city: ')
            self.state = state = input('Please enter your state: ')
            self.zip = zip = input('Please enter your zip code: ')
            self.account_number = generate_random_id()
            self.account_balance = 0.00
            
            print(f'Your account number is {self.account_number}. Please retain this for your records')
        
        elif int(self.customer_input) == 1 or int(self.customer_input) ==2: 
            self.firstName = firstName 
            self.lastName = lastName 
            self.address = address 
            self.city = city 
            self.state = state 
            self.zip = zip 
            self.account_number = account_number
            self.account_balance = Decimal(account_balance)

    