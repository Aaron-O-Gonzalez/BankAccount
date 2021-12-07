import mysql.connector

'''Python connection to MySQL localhost, which will create a database BankCustomers
   and create a table customerAccounts'''

def connect_to_server():
    connection = None
    try:
        connection = mysql.connector.connect(user = '<user>',
                                             password = '<password>',
                                             host ='localhost',
                                             port = '3306')
        print("Connection to server successful")
    
    except Exception as error:
        print("Error while connecting to server", error)
    
    return connection


def connect_database(connection):
    mycursor = connection.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS BankCustomers;")
    
    try:
        connection = mysql.connector.connect(user = '<user>',
                                             password = '<password>',
                                             host ='localhost',
                                             port = '3306',
                                             database = 'BankCustomers')
        print("Connection to database successful")
    
    except Exception as error:
        print("Error while connecting to server", error)
    
    return connection

def create_table(connection):
    sql_statement = """CREATE TABLE IF NOT EXISTS customerAccounts(
                                    account_number INT NOT NULL PRIMARY KEY,
                                    firstName VARCHAR(50),
                                    lastName VARCHAR(50),
                                    address VARCHAR(100),
                                    city VARCHAR(50),
                                    state VARCHAR(20),
                                    zip_code INT,
                                    account_balance DECIMAL)
                     """
    
    cursor = connection.cursor()
    cursor.execute(sql_statement)
    cursor.close()

server_connection = connect_to_server()
db_connection = connect_database(server_connection)
create_table(db_connection)
