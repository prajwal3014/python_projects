import sqlite3

# CREATING CONNECTION AND TABLES
obj = sqlite3.connect("student.db")

obj.execute(""" create table if not exists student (
                st_id varchar(255),
                st_name varchar(255),
                age varchar(255),
                st_mail_id varchar(255),
                st_course varchar(255),
                st_stream varchar(255),
                math varchar(255),
                english varchar(255),
                computer_science varchar(255),
                python varchar(255),
                dbms varchar(255),
                data_structure varchar(255),
                percentage int,
                grade varchar(255)
) """)
obj.commit()

def save_student(id, name, age, mail, course, stream, math, english, computer, python, dbms, data_st, percentage, grade) :
    obj.execute(""" insert into student values ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}') """
                .format(id, name, age, mail, course, stream, math, english, computer, python, dbms, data_st, percentage, grade))
    obj.commit()

def check_id() :
    id_list = []
    mail_list = []
    query_1 = obj.execute(""" select st_id from student """)
    lst = query_1.fetchall()
    for i in lst :
        i = list(i)
        id = i.pop()
        id_list.append(id)
    
    query_2 = obj.execute(""" select st_mail_id from student """)
    lst = query_2.fetchall()
    for i in lst :
        i = list(i)
        mail = i.pop()
        mail_list.append(mail)
    return id_list, mail_list

def get_student(id) :
    query = obj.execute(""" select * from student where st_id = '{}' """.format(id))
    lst = query.fetchall()
    details = lst.pop()
    details = list(details)
    return details

def delete_student(id) :
    obj.execute(""" delete from student where st_id = '{}' """.format(id))
    obj.commit()

def percentage_student(id) :
    query = obj.execute(""" select percentage from student where st_id = '{}' """.format(id))
    lst = query.fetchall()
    y = lst.pop()
    y = list(y)
    percentage = y.pop()

    query = obj.execute(""" select grade from student where st_id = '{}' """.format(id))
    lst = query.fetchall()
    y = lst.pop()
    y = list(y)
    grade = y.pop()

    return percentage, grade

def get_mail_id(id) :
    query = obj.execute(""" select st_mail_id from student where st_id = '{}' """.format(id))
    lst = query.fetchall()
    y = lst.pop()
    y = list(y)
    reciever = y.pop()
    
    return reciever
# save_student('2', 'prajwal', '30/04/2001', 'prajjusharma@gmail.com', 'B.E.', 'CSE-1/C', '92', '85', '95', '98', '78', '97')