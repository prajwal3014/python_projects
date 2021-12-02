import sqlite3

connection = sqlite3.connect("customers.db")
obj = connection.cursor()
print("Connection created...!")

obj.execute(""" create table if not exists bank (
                name varchar(255),
                acc_no varchar(255),
                balance int 
            )""")
connection.commit()