import sqlite3
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

connection = sqlite3.connect("terraformers.db", check_same_thread=False)
obj = connection.cursor()
print("Connection created...!")

obj.execute(""" create table if not exists terraformers (
                name varchar(255),
                emp_id varchar(255),
                email varchar(255),
                password varchar(255)
            )""")
connection.commit()

obj.execute(""" create table if not exists available (
                name varchar(255),
                start_time varchar(255),
                end_time varchar(255)
            )""")
connection.commit()

obj.execute(""" create table if not exists appointments (
                name varchar(255),
                guest_name varchar(255),
                title varchar(255),
                agenda varchar(255),
                start_time varchar(255),
                end_time varchar(255)
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

def check_email(email) :
    email_list = []
    query = obj.execute(""" select email from terraformers """)
    lst = query.fetchall()
    for i in lst :
        i = list(i)
        y = i.pop()
        email_list.append(y)
    if email in email_list :
        return True
    else :
        return False

def check_empid(emp_id) :
    empid_list = []
    query = obj.execute(""" select emp_id from terraformers """)
    lst = query.fetchall()
    for i in lst :
        i = list(i)
        y = i.pop()
        empid_list.append(y)
    if emp_id in empid_list :
        return True
    else :
        return False

def register_user(name, emp_id, email, password) :
    hash_password = generate_password_hash(password)
    obj.execute(""" insert into terraformers values('{}', '{}', '{}', '{}') """.format(name, emp_id, email, hash_password))
    connection.commit()

def login_user(emp_id, password) :
    query = obj.execute(""" select password from terraformers where emp_id = '{}' """.format(emp_id))
    lst = query.fetchall()
    y = lst.pop()
    y = list(y)
    hash_password = y.pop()
    if check_password_hash(hash_password, password) :
        return True
    else :
        return False

def get_name(emp_id) :
    query = obj.execute(""" select name from terraformers where emp_id = '{}' """.format(emp_id))
    lst = query.fetchall()
    y = lst.pop()
    y = list(y)
    name = y.pop()
    return name

def book_app(name, guest_name, title, agenda, start_time, end_time) :
    obj.execute(""" insert into appointments values('{}', '{}', '{}', '{}', '{}', '{}') """.format(name, guest_name, title, agenda, start_time, end_time))
    connection.commit()

# def get_history() :
#     history_list = []
#     sub_list = []
#     query = obj.execute(""" select * from history """)
#     lst = query.fetchall()
#     for i in lst :
#         i = list(i)
#         sub_list.append("Date : " + i[0])
#         sub_list.append("Time : " + i[1])
#         sub_list.append(i[2])
#         history_list.append(sub_list)
#         sub_list = []
#     return history_list

# def check_acc() :
#     acc_list = []
#     query = obj.execute(""" select acc_no from bank """)
#     lst = query.fetchall()
#     for i in lst :
#         i = list(i)
#         y = i.pop()
#         acc_list.append(y)
#     return acc_list

# def update_balance(balance, acc_no) :
#     obj.execute(""" update bank set balance = '{}' where acc_no = '{}' """.format(balance, acc_no))
#     connection.commit()

# def update_history(s_name, r_name, amount) :
#     now = datetime.now()
#     date = now.strftime("%d/%m/%Y")
#     time = now.strftime("%H:%M:%S")
#     obj.execute(""" insert into history values('{}', '{}', '{} sent ₹{} to {}') """.format(date, time,s_name, amount, r_name))
#     connection.commit()

# print(get_balance("prajwal@1"))
# query = obj.execute(""" select * from bank """)
# lst = query.fetchall()
# print(lst)

# obj.execute(""" drop table history """)
# connection.commit()
# get_history()