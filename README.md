# Bank Account Simulator

The following code mimics a simplistic banking system, where the user is presented with a dynamic command line interface. The architecture of the program is depicted as follows:



        ![BankAccountArchitecture](https://github.com/Aaron-O-Gonzalez/BankAccount/blob/master/BankAccountArchitecture.png)



In short, the user is presented with one of three options: (1) deposit money into account, (2) withdraw money from account, or (3) create a new account.  

* If the user opts for "3", the user will be prompted to enter the following: first name, last name, address, city, state, and zip code. These values will be stored into the CustomerAccount class from the **CustomerDetails.py** and a unique 9-digit number will be generated for the user. The user is encouraged to store the number, should he/she want to perform any additional transactions during that session or in the future. The variables stored from the CustomerAccount class are then inherited into the BankAccount class from **account_transactions.py**, which enables the methods withdraw and deposit for existing accounts. Finally, these variables are written to a MySQL backend, with the account balance defaulting to 0.
* If the user opts for "1" or "2", the user will be prompted to enter their unique 9 digit number. The database will be searched for the account number, and should this number not exist or be typed incorrectly, the user will be notified as such. Otherwise, the data from the MySQL database will be read inserted into a BankAccount object, and the user will be asked to state the amount that he/she would like to deposit/withdraw. There are no limits on the number or amount of deposits, and for withdrawals, the user will not be able to withdraw an amount greater than his/her balance. Each action will immediately be reflected on the BankAccount object, which will then update the corresponding value in the customer database.



