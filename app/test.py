import psycopg2

connection = psycopg2.connect(database='postgres', user='postgres', password='admin', host='localhost')
print("Connection is opened...!")
obj = connection.cursor()

try :
    # obj.execute(""" create table app2 (
    #                 uname varchar(255),
    #                 upass varchar(255)
    #             ); """)
    # obj.execute(""" insert into app2 values ('prajwal', '12prajwal'); """)
    # obj.execute(""" insert into app2 values ('ayush', '12ayush'); """)
    obj.execute(""" select * from app """)
    results = obj.fetchall()
    connection.commit()
    print(results)
    print("Query successfully executed...!")
except :
    print("There some problem in executing query...!")
finally :
    connection.close()
    print("Connection is closed...!")