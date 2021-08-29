import psycopg2
from werkzeug.security import generate_password_hash, check_password_hash

connection = psycopg2.connect(database='postgres', user='postgres', password='admin', host='localhost')
obj = connection.cursor()
print("Connection opened successfully...!")

def save_user(name, email, number, username, password) :
    hash_password = generate_password_hash(password)
    obj.execute(""" insert into loginApp values ('{0}', '{1}', '{2}', '{3}', '{4}') """.format(name, email, number, username, hash_password))
    connection.commit()
    print("Save user function executed successfully...!")

def get_user(username) :
    obj.execute(""" select name, email, number, username from loginApp where username='{0}' """.format(username))
    data = obj.fetchall()
    user_data = data.pop()
    print("Get user function executed successfully...!")
    return user_data

def check_password(username, password) :
    obj.execute(""" select password from loginApp where username='{0}' """.format(username))
    x = obj.fetchall()
    y = x.pop()
    y = list(y)
    hash_password = y.pop()
    print("Password checking completed...!")
    return str(check_password_hash(hash_password, password))

# obj.execute(""" create table loginApp (
#                 name varchar(255),
#                 email varchar(255),
#                 number varchar(255),
#                 username varchar(255),
#                 password varchar(255)
#             ) """)
# connection.commit()
# print("Table created...!")
# save_user("prajwal sharma", "something@some.com", "123456789", "rocking", "rocking1")
# print(get_user("rocking"))
# print(check_password("rocking", "rocking1"))