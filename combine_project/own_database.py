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
    user_tables_dict = {}
    check_user_dict = {}
    query = obj.execute(""" select * from users """)
    lst = query.fetchall()
    for y in lst :
        y = list(y)
        sample_dict = {y[0] : [y[2]]}
        user_dict = {y[0] : y[1]}
        check_user_dict.update(user_dict)
        user_tables_dict.update(sample_dict)
    return user_tables_dict, check_user_dict

# save_user("Prajwal Sharma", "prajwal@1", "tuition, development")
# save_user("Ayush Rana", "ayush@2", "other, todo")
print(get_users())