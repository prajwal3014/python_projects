# import psycopg2

# connection = psycopg2.connect(database='postgres', user='postgres', password='admin', host='localhost')
# print("Connection is opened...!")
# obj = connection.cursor()

# try :
#     # obj.execute(""" create table app2 (
#     #                 uname varchar(255),
#     #                 upass varchar(255)
#     #             ); """)
#     # obj.execute(""" insert into app2 values ('prajwal', '12prajwal'); """)
#     # obj.execute(""" insert into app2 values ('ayush', '12ayush'); """)
#     obj.execute(""" select * from app """)
#     results = obj.fetchall()
#     connection.commit()
#     print(results)
#     print("Query successfully executed...!")
# except :
#     print("There some problem in executing query...!")
# finally :
#     connection.close()
#     print("Connection is closed...!")
import json

# with open('uname.json', 'r') as userfile :
#     uname = json.load(userfile)
# with open('details.json', 'r') as userfile :
#     user_dict = json.load(userfile)
# x="prajju"
# y="prajju"
# count_name = -1
# count_pass = -2
# upass = list(user_dict.values())
# if x in uname :
#     count_name = uname.index(x)
# if y in upass :
#     count_pass = upass.index(y)
# if count_name == count_pass :
#     print("Yes")
# else :
#     print("No")
u_name = input()
user_name = u_name.lower()
user_pass = input()
d_file = 'details.json'
with open(d_file, 'r') as n :
    user_dict = json.load(n)
user_list = list(user_dict.keys())
pass_list = list(user_dict.values())
if user_pass in pass_list :
    count_pass = pass_list.index(user_pass)
if user_name in user_list :
    count_name = user_list.index(user_name)
if count_name != count_pass :
    print("invalid username or password")
elif count_name == count_pass :
    print("welcome {0}".format(user_name))
