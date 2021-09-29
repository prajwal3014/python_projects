import sqlite3
from werkzeug.security import check_password_hash, generate_password_hash

################################### Creating Connection & Tables ################################################
connection = sqlite3.connect("fruit.db")
obj = connection.cursor()

obj.execute(""" create table if not exists user (
                username varchar(255),
                password varchar(255),
                wallet_money int
            ) """)
connection.commit()
obj.execute(""" create table if not exists fruit_manage (
                username varchar(255),
                quantity int,
                date_time varchar(255),
                profit varchar(255),
                profit_percentage varchar(255)
            ) """)
connection.commit()
obj.execute(""" create table if not exists fruit_quantity (
                sp_id varchar(255),
                mango varchar(255),
                banana varchar(255),
                apple varchar(255),
                guava varchar(255),
                orange varchar(255),
                dragon_fruit varchar(255)
            ) """)
connection.commit()
################################### END ################################################

################################### Returning Fruits Quantity ################################################
def show_quantity() :
    obj.execute(""" insert into fruit_quantity (sp_id, mango, banana, apple, guava, orange, dragon_fruit) select '1', '200', '200', '200', '200', '200', '200' where not exists (select * from fruit_quantity)""")
    connection.commit()
    query_1 = obj.execute(""" select mango from fruit_quantity """)
    lst = query_1.fetchall()
    y = lst.pop()
    y = list(y)
    man = y.pop()
    man = int(man)

    query_2 = obj.execute(""" select banana from fruit_quantity """)
    lst = query_2.fetchall()
    y = lst.pop()
    y = list(y)
    ban = y.pop()
    ban = int(ban)

    query_3 = obj.execute(""" select apple from fruit_quantity """)
    lst = query_3.fetchall()
    y = lst.pop()
    y = list(y)
    app = y.pop()
    app = int(app)

    query_4 = obj.execute(""" select guava from fruit_quantity """)
    lst = query_4.fetchall()
    y = lst.pop()
    y = list(y)
    gua = y.pop()
    gua = int(gua)

    query_5 = obj.execute(""" select orange from fruit_quantity """)
    lst = query_5.fetchall()
    y = lst.pop()
    y = list(y)
    ora = y.pop()
    ora = int(ora)

    query_6 = obj.execute(""" select dragon_fruit from fruit_quantity """)
    lst = query_6.fetchall()
    y = lst.pop()
    y = list(y)
    dra = y.pop()
    dra = int(dra)
    return man, ban, app, gua, ora, dra
################################### END ################################################

################################### Updating Fruits Quantity ################################################
def update_quantity(man_value, ban_value, app_value, gua_value, ora_value, dra_value) :
    query_1 = obj.execute(""" select mango from fruit_quantity """)
    lst = query_1.fetchall()
    y = lst.pop()
    y = list(y)
    man = y.pop()
    man = int(man)
    if man<=10 :
        obj.execute(""" update fruit_quantity set mango = '200' """)
        connection.commit()
    else :
        real_1 = man-man_value
        obj.execute(""" update fruit_quantity set mango = {} """.format(str(real_1)))
        connection.commit()

    query_2 = obj.execute(""" select banana from fruit_quantity """)
    lst = query_2.fetchall()
    y = lst.pop()
    y = list(y)
    ban = y.pop()
    ban = int(ban)
    if ban<=10 :
        obj.execute(""" update fruit_quantity set banana = '200' """)
        connection.commit()
    else :
        real_2 = ban-ban_value
        obj.execute(""" update fruit_quantity set banana = {} """.format(str(real_2)))
        connection.commit()

    query_3 = obj.execute(""" select apple from fruit_quantity """)
    lst = query_3.fetchall()
    y = lst.pop()
    y = list(y)
    app = y.pop()
    app = int(app)
    if app<=10 :
        obj.execute(""" update fruit_quantity set apple = '200' """)
        connection.commit()
    else :
        real_3 = app-app_value
        obj.execute(""" update fruit_quantity set apple = {} """.format(str(real_3)))
        connection.commit()

    query_4 = obj.execute(""" select guava from fruit_quantity """)
    lst = query_4.fetchall()
    y = lst.pop()
    y = list(y)
    gua = y.pop()
    gua = int(gua)
    if gua<=10 :
        obj.execute(""" update fruit_quantity set guava = '200' """)
        connection.commit()
    else :
        real_4 = gua-gua_value
        obj.execute(""" update fruit_quantity set guava = {} """.format(str(real_4)))
        connection.commit()

    query_5 = obj.execute(""" select orange from fruit_quantity """)
    lst = query_5.fetchall()
    y = lst.pop()
    y = list(y)
    ora = y.pop()
    ora = int(ora)
    if ora<=10 :
        obj.execute(""" update fruit_quantity set orange = '200' """)
        connection.commit()
    else :
        real_5 = ora-ora_value
        obj.execute(""" update fruit_quantity set orange = {} """.format(str(real_5)))
        connection.commit()

    query_6 = obj.execute(""" select dragon_fruit from fruit_quantity """)
    lst = query_6.fetchall()
    y = lst.pop()
    y = list(y)
    dra = y.pop()
    dra = int(dra)
    if dra<=10 :
        obj.execute(""" update fruit_quantity set dragon_fruit = '200' """)
        connection.commit()
        print("fruit is less than 150")
    else : 
        real_6 = dra-dra_value
        obj.execute(""" update fruit_quantity set dragon_fruit = {} """.format(str(real_6)))
        connection.commit()
################################### END ################################################

################################### Username Checking ################################################
def check_username() :
    user_list = []
    query_1 = obj.execute(""" select username from user """)
    lst = query_1.fetchall()
    for i in range(0, len(lst)) :
        user = lst.pop()
        user = list(user)
        usernames = user.pop()
        user_list.append(usernames)
    return user_list
################################### END ################################################

################################### Password Checking ################################################
def check_password(user_name, password) :
    query = obj.execute(""" select password from user where username='{}' """.format(user_name))
    lst = query.fetchall()
    y = lst.pop()
    y = list(y)
    hash_password = y.pop()
    return str(check_password_hash(hash_password, password))
################################### END ################################################

################################### Saving User ################################################
def save_user(user_name, password, wallet_money) :
    hash_password = generate_password_hash(password)
    obj.execute(""" insert into user values('{}', '{}', '{}') """.format(user_name, hash_password, wallet_money))
    connection.commit()
################################### END ################################################

################################### Returning Wallet Money ################################################
def get_money(user_name) :
    query = obj.execute(""" select wallet_money from user where username = '{}' """.format(user_name))
    lst = query.fetchall()
    y = lst.pop()
    y = list(y)
    money = y.pop()
    return money
################################### END ################################################

################################### Updating Wallet Money ################################################
def update_money(user_name, wallet_money) :
    obj.execute(""" update user set wallet_money = {} where username = '{}' """.format(wallet_money, user_name))
    connection.commit()
################################### END ################################################

################################### Saving User Data ################################################
def save_user_data(user_name, value, d_t, profit, profit_per) :
    obj.execute(""" insert into fruit_manage values('{}', '{}', '{}', '{}', '{}') """.format(user_name, value, d_t, profit, profit_per))
    connection.commit()
################################### END ################################################

################################### Returning Profit List ################################################
def get_profit() :
    query = obj.execute(""" select username, date_time, profit, profit_percentage from fruit_manage """)
    lst = query.fetchall()
    return lst
################################### END ################################################