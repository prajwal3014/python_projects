import psycopg2
from user import User
from werkzeug.security import generate_password_hash

connection = psycopg2.connect(database='postgres', user='postgres', password='admin', host='localhost')
obj = connection.cursor()
print("Creating connection")

def save_user(username, password, email) :
    hash_password = generate_password_hash(password)
    obj.execute(""" insert into chatapp values ('{0}', '{1}', '{2}') """.format(username, hash_password, email))
    connection.commit()
    print("Query executed")

def get_user(username) :
    obj.execute(""" select * from chatapp where username='{0}' """.format(username))
    data_user = obj.fetchall()
    user_data = data_user.pop()
    user_data = list(user_data)
    print("Query executed")
    x = User(user_data[0], user_data[1], user_data[2]) if user_data else None
    return x

