import sqlite3

obj = sqlite3.connect("calculator.db", check_same_thread=False)

obj.execute(""" create table if not exists calculator (
                operation varchar(255),
                answer varchar(255)
) """)
obj.commit()

def save_history(operation, answer) :
    obj.execute(""" insert into calculator values ('{}', '{}') """.format(operation, answer))
    obj.commit()

def show_history() :
    history = []
    query = obj.execute(""" select * from calculator """)
    lst = query.fetchall()
    for data in lst :
        history.append(list(data))
    return history

def delete_history() :
    obj.execute(""" drop table if exists calculator """)
    obj.commit()
    obj.execute(""" create table if not exists calculator (
                    operation varchar(255),
                    answer varchar(255)
    ) """)
    obj.commit()