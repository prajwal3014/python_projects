import sqlite3 as sq

connection = sq.connect('test.db')

obj = connection.cursor()

obj.execute(""" create table car (
                uname varchar(255),
                pass varchar(255)
); """)

obj.execute(""" insert into car values ('prajwal', '12prajwal'); """)
obj.execute(""" insert into car values ('ayush', '12prajwal'); """)
# obj.execute(""" insert into car values ('harshit', '12prajwal'); """)
# print("executed...")

obj.execute(""" select * from car """)

result = obj.fetchall()

print(result)