from account_transactions import BankAccount
from connect_database import connect_database, connect_to_server, create_table

server_connection = connect_to_server()
db_connection = connect_database(server_connection)
create_table(db_connection)

print("Welcome to HashBank. Please select a reason for today's interface.")

while(1):
    print("Press 1 to deposit funds into your account")
    print("Press 2 to withdraw funds from your account")
    print("Press 3 to create an account")
    print("To exit please press anything else.")
    clientRequest = input()

    if int(clientRequest) == 3:
        client_interface = BankAccount(customer_input=clientRequest)
        cursor = db_connection.cursor()

        sql_statement = """INSERT INTO customerAccounts(account_number, firstName, lastName, address,
                                                        city, state, zip_code, account_balance)
                                                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""

        values = (client_interface.account_number,client_interface.firstName, client_interface.lastName, client_interface.address, client_interface.city, client_interface.state, client_interface.zip, client_interface.account_balance)
        cursor.execute(sql_statement, values)
        db_connection.commit()
        cursor.close()

    elif int(clientRequest) == 1 or int(clientRequest) == 2:
        client_account_number = input('Please enter your account number: ')
        sql_statement = """SELECT account_number, firstName, lastName, address, city, state, zip_code, account_balance
                           FROM customerAccounts
                           WHERE account_number = %s"""

        cursor = db_connection.cursor()
        value = (client_account_number,)
        try:
            cursor.execute(sql_statement, value)
            row = cursor.fetchone()
            client_interface = BankAccount(customer_input=clientRequest,firstName=row[1], lastName=row[2], address=row[3], city = row[4], state = row[5], zip=row[6], account_balance=row[7], account_number=row[0])

            if int(clientRequest) == 1:
                client_interface.deposit()
            
            else:
                client_interface.withdraw()
            
            sql_statement = """UPDATE customerAccounts
                               SET account_balance = %s
                               WHERE account_number = %s;"""
        
            values = (client_interface.account_balance, client_interface.account_number)
            cursor.execute(sql_statement, values)
            db_connection.commit()
            cursor.close()

        except:
            print('Sorry, your account number does not match with our records')
    
    else:
        break