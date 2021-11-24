import psycopg2
from user import User
from werkzeug.security import generate_password_hash

connection = psycopg2.connect(database='postgres', user='postgres', password='admin', host='localhost')
obj = connection.cursor()
print("Creating connection")

obj.execute(""" create table if not exists messages (
                room varchar(255),
                text varchar(255),
                sender varchar(255)
            ); """)
connection.commit()

def save_user(username, password, email) :
    hash_password = generate_password_hash(password)
    obj.execute(""" insert into chatapp values ('{0}', '{1}', '{2}') """.format(username, hash_password, email))
    connection.commit()
    print("Save user Query executed")

def get_user(username) :
    obj.execute(""" select * from chatapp where username='{0}' """.format(username))
    data_user = obj.fetchall()
    user_data = data_user.pop()
    user_data = list(user_data)
    print("Get user Query executed")
    x = User(user_data[0], user_data[1], user_data[2]) if user_data else None
    return x

def save_message(room, text, sender) :
    obj.execute(""" insert into messages values ('{0}', '{1}', '{2}') """.format(room, text, sender))
    connection.commit()
    print("Save message Query executed")

def get_message(room) :
    obj.execute(""" select sender, text from messages where room='{0}' """.format(room))
    msg = obj.fetchall()
    print("Get msg Query executed")
    return msg