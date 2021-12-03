import sqlite3

connection = sqlite3.connect("customers.db", check_same_thread=False)
obj = connection.cursor()
print("Connection created...!")

obj.execute(""" create table if not exists bank (
                name varchar(255),
                acc_no varchar(255),
                balance varchar(255) 
            )""")
connection.commit()

# obj.execute(""" insert into bank values('Prajwal Sharma', 'prajwal@1', '1000') """)
# connection.commit()
# obj.execute(""" insert into bank values('Ayush Rana', 'ayush@2', '1000') """)
# connection.commit()
# obj.execute(""" insert into bank values('Harshit Srivastava', 'harshit@3', '1000') """)
# connection.commit()
# obj.execute(""" insert into bank values('Parv Arora', 'parv@4', '1000') """)
# connection.commit()
# obj.execute(""" insert into bank values('Ankit Luthra', 'ankit@5', '1000') """)
# connection.commit()
# obj.execute(""" insert into bank values('Aryan Anand', 'aryan@6', '1000') """)
# connection.commit()
# obj.execute(""" insert into bank values('Shubam Khandelwal', 'shubam@7', '1000') """)
# connection.commit()
# obj.execute(""" insert into bank values('Arihant Jain', 'arihant@8', '1000') """)
# connection.commit()
# obj.execute(""" insert into bank values('Bhagyansh Kumar', 'bhagyansh@9', '1000') """)
# connection.commit()
# obj.execute(""" insert into bank values('Rohit Kumar', 'rohit@10', '1000') """)
# connection.commit()

def get_balance(acc_no) :
    query = obj.execute(""" select balance from bank where acc_no = '{}' """.format(acc_no))
    lst = query.fetchall()
    y = lst.pop()
    y = list(y)
    balance = y.pop()
    return balance

# print(get_balance("prajwal@1"))
# query = obj.execute(""" select * from bank """)
# lst = query.fetchall()
# print(lst)

# obj.execute(""" drop table bank """)
# connection.commit()
