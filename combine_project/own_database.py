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

def save_table(table_name) :
    obj.execute(""" create table if not exists {} (
                    sno integer primary key autoincrement
    )""".format(table_name))
    connection.commit()

def add_cols(table_name, cols_list) :
    for cols_name in cols_list :
        obj.execute(""" alter table {} add {} varchar(255) """.format(table_name, cols_name))
        connection.commit()

def add_row(table_name) :
    obj.execute

def get_table(table_name) :
    query = obj.execute(""" select * from {} """.format(table_name))
    lst = query.fetchall()
    if lst :
        return lst
    else :
        return "Empty list"    

# save_user("Prajwal Sharma", "prajju_174", "prajwal@1", "tuition, development")
# save_user("Ayush Rana", "ayush_12", "ayush@2", "")
# dict_1, dict_2, lst = get_users()
# print(dict_1)
# print(dict_2)
# print(lst)
# print(get_name("prajwal@1"))
# save_table("todos")
# lst = ['python', 'flask', 'react']
# add_cols("todos", lst)
print(get_table("todos"))