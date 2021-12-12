import sqlite3

connection = sqlite3.connect("own_db.db", check_same_thread=False)
obj = connection.cursor()

obj.execute(""" create table if not exists users (
                fullname varchar(255),
                uid varchar(255),
                allTables varchar(255)
) """)
connection.commit()

def save_user(full_name, uid, all_tables) :
    obj.execute(""" insert into users values('{}', '{}', '{}') """.format(full_name, uid, all_tables))
    connection.commit()

def get_users() :
    query = obj.execute(""" select * from users """)
    lst = query.fetchall()
    return lst

# save_user("Prajwal Sharma", "prajwal@1", "tuition, development")
# save_user("Ayush Rana", "ayush@2", "other, todo")
print(get_users())