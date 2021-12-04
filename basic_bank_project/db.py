import sqlite3
from datetime import datetime

connection = sqlite3.connect("customers.db", check_same_thread=False)
obj = connection.cursor()
print("Connection created...!")

obj.execute(""" create table if not exists bank (
                name varchar(255),
                acc_no varchar(255),
                balance varchar(255) 
            )""")
connection.commit()

obj.execute(""" create table if not exists history (
                date varchar(255),
                time varchar(255),
                logs varchar(255)
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

def get_name(acc_no) :
    query = obj.execute(""" select name from bank where acc_no = '{}' """.format(acc_no))
    lst = query.fetchall()
    y = lst.pop()
    y = list(y)
    name = y.pop()
    return name

def get_history() :
    history_list = []
    sub_list = []
    query = obj.execute(""" select * from history """)
    lst = query.fetchall()
    for i in lst :
        i = list(i)
        sub_list.append("Date : " + i[0])
        sub_list.append("Time : " + i[1])
        sub_list.append(i[2])
        history_list.append(sub_list)
        sub_list = []
    return history_list

def check_acc() :
    acc_list = []
    query = obj.execute(""" select acc_no from bank """)
    lst = query.fetchall()
    for i in lst :
        i = list(i)
        y = i.pop()
        acc_list.append(y)
    return acc_list

def update_balance(balance, acc_no) :
    obj.execute(""" update bank set balance = '{}' where acc_no = '{}' """.format(balance, acc_no))
    connection.commit()

def update_history(s_name, r_name, amount) :
    now = datetime.now()
    date = now.strftime("%d/%m/%Y")
    time = now.strftime("%H:%M:%S")
    obj.execute(""" insert into history values('{}', '{}', '{} sent ₹{} to {}') """.format(date, time,s_name, amount, r_name))
    connection.commit()

# print(get_balance("prajwal@1"))
# query = obj.execute(""" select * from bank """)
# lst = query.fetchall()
# print(lst)

# obj.execute(""" drop table history """)
# connection.commit()
# get_history()
print(get_history())