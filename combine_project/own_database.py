import sqlite3

connection = sqlite3.connect("own_db.db", check_same_thread=False)
obj = connection.cursor()

obj.execute(""" create table if not exists users (
                fullname varchar(255),
                username varchar(255),
                uid varchar(255),
                allTables varchar(255)
) """)
connection.commit()

def save_user(full_name, user_name, uid, all_tables) :
    obj.execute(""" insert into users values('{}', '{}', '{}', '{}') """.format(full_name, user_name, uid, all_tables))
    connection.commit()

def get_users() :
    users_list = []
    user_tables_dict = {}
    check_user_dict = {}
    query = obj.execute(""" select * from users """)
    lst = query.fetchall()
    for y in lst :
        y = list(y)
        users_list.append(y[1])
        sample_dict = {y[1] : [y[3]]}
        user_dict = {y[1] : y[2]}
        check_user_dict.update(user_dict)
        user_tables_dict.update(sample_dict)
    return user_tables_dict, check_user_dict, users_list

def get_name(uid) :
    query = obj.execute(""" select fullname from users where uid='{}' """.format(uid))
    lst = query.fetchall()
    y = lst.pop()
    y = list(y)
    name = y.pop()
    return name

# save_user("Prajwal Sharma", "prajju_174", "prajwal@1", "tuition, development")
# save_user("Ayush Rana", "ayush_12", "ayush@2", "other, todo")
# dict_1, dict_2, lst = get_users()
# print(dict_1)
# print(dict_2)
# print(lst)
# print(get_name("prajwal@1"))