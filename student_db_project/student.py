import tkinter as tk
from tkinter.font import BOLD
from tkinter import messagebox
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from db import *

# SHOW STUDENT DETAILS
def show_details(id) :
    window = tk.Tk()
    window.geometry("480x600")
    window.title("Student Management")

    head  = tk.Label(text="\nDetails of Student\n", fg="blue", font=("arial", 18, BOLD)).pack()
    detail_list = get_student(id)
    
    lab = tk.Label(text="Student ID : ", font=("arial", 12, BOLD)).place(x=20, y=100)
    lab = tk.Label(text=detail_list[0], font=("arial", 12), fg="blue").place(x=125, y=100)

    lab = tk.Label(text="Name : ", font=("arial", 12, BOLD)).place(x=20, y=150)
    lab = tk.Label(text=detail_list[1], font=("arial", 12), fg="blue").place(x=115, y=150)

    lab = tk.Label(text="Age : ", font=("arial", 12, BOLD)).place(x=20, y=200)
    lab = tk.Label(text=detail_list[2], font=("arial", 12), fg="blue").place(x=115, y=200)

    lab = tk.Label(text="Mail ID : ", font=("arial", 12, BOLD)).place(x=20, y=250)
    lab = tk.Label(text=detail_list[3], font=("arial", 12), fg="blue").place(x=115, y=250)

    lab = tk.Label(text="Course : ", font=("arial", 12, BOLD)).place(x=20, y=300)
    lab = tk.Label(text=detail_list[4], font=("arial", 12), fg="blue").place(x=115, y=300)

    lab = tk.Label(text="Stream : ", font=("arial", 12, BOLD)).place(x=20, y=350)
    lab = tk.Label(text=detail_list[5], font=("arial", 12), fg="blue").place(x=115, y=350)

    lab = tk.Label(text="Percentage : ", font=("arial", 12, BOLD)).place(x=15, y=400)
    lab = tk.Label(text=str(detail_list[12]) + "%", font=("arial", 12), fg="blue").place(x=115, y=400)

    lab = tk.Label(text="Grade : ", font=("arial", 12, BOLD)).place(x=20, y=450)
    lab = tk.Label(text=detail_list[13], font=("arial", 12), fg="blue").place(x=115, y=450)

    def back_window() :
        window.destroy()
        main_screen()

    back_btn = tk.Button(text="Back", fg="white", bg="red", width=20, command=back_window).place(x=170, y=520)

    window.mainloop()

def show_student() :
    window = tk.Tk()
    window.geometry("480x350")
    window.title("Student Management")

    head  = tk.Label(text="\nDetails of Student\n", fg="blue", font=("arial", 18, BOLD)).pack()

    lab = tk.Label(text="Enter the Student ID whom you want to see : ", font=("arial", 12, BOLD)).pack()
    
    lab = tk.Label(text=" ").pack()
    
    tkid = tk.Entry(width=30, fg="blue", bg="white")
    tkid.pack()

    lab = tk.Label(text=" ").pack()

    def to_show() :
        id = tkid.get()
        try :
            id = int(id)
            id_list, mail_list = check_id()
            if str(id) not in id_list :
                messagebox.showwarning("No Id", "Id does not exists...!")
            else :
                window.destroy()
                show_details(id)
        except :
            messagebox.showwarning("Wrong Id", "Id must be numeric...!")

    show_btn = tk.Button(text="Show Details", fg="white", bg="green", width=20, command=to_show).pack()

    lab = tk.Label(text=" ").pack()

    def back_window() :
        window.destroy()
        main_screen()

    back_btn = tk.Button(text="Back", fg="white", bg="red", width=20, command=back_window).pack()

    window.mainloop()

# ADD STUDENT
def add_marks(id, name, age, mail, course, stream) :
    window = tk.Tk()
    window.geometry("480x550")
    window.title("Student Management")

    head  = tk.Label(text="\nAdd Marks\n", fg="blue", font=("arial", 18, BOLD)).pack()

    lab = tk.Label(text="Maths : ", font=("arial", 12, BOLD)).place(x=90, y=100)
    tkmath = tk.Entry(width=30, fg="blue", bg="white")
    tkmath.place(x=185, y=102)

    lab = tk.Label(text="English : ", font=("arial", 12, BOLD)).place(x=90, y=150)
    tkeng = tk.Entry(width=30, fg="blue", bg="white")
    tkeng.place(x=185, y=152)

    lab = tk.Label(text="Computer : ", font=("arial", 12, BOLD)).place(x=90, y=200)
    tkcomp = tk.Entry(width=30, fg="blue", bg="white")
    tkcomp.place(x=185, y=202)

    lab = tk.Label(text="Python : ", font=("arial", 12, BOLD)).place(x=90, y=250)
    tkpy = tk.Entry(width=30, fg="blue", bg="white")
    tkpy.place(x=185, y=252)

    lab = tk.Label(text="DBMS : ", font=("arial", 12, BOLD)).place(x=90, y=300)
    tkdb = tk.Entry(width=30, fg="blue", bg="white")
    tkdb.place(x=185, y=302)

    lab = tk.Label(text="Data Structure : ", font=("arial", 12, BOLD)).place(x=58, y=350)
    tkds = tk.Entry(width=30, fg="blue", bg="white")
    tkds.place(x=185, y=352)

    def to_add() :
        math = tkmath.get()
        english = tkeng.get()
        computer = tkcomp.get()
        python = tkpy.get()
        dbms = tkdb.get()
        data_struct = tkds.get()
        if math.isalpha() or english.isalpha() or computer.isalpha() or python.isalpha() or dbms.isalpha() or data_struct.isalpha() :
            messagebox.showwarning("Wrong Marks Format", "Marks must be numerical...!")
        else :
            sum = int(math) + int(english) + int(computer) + int(python) + int(dbms) + int(data_struct)
            percentage = (sum/600)*100
            grade = "F"
            if 91<=percentage<=100 :
                grade = "A+"
            elif 81<=percentage<=90 :
                grade = "A"
            elif 71<=percentage<=80 :
                grade = "B+"
            elif 61<=percentage<=70 :
                grade = "B"
            elif 51<=percentage<=60 :
                grade = "C"
            elif 41<=percentage<=50 :
                grade = "D"
            elif 34<=percentage<40 :
                grade = "E"
            save_student(id, name, age, mail, course, stream, math, english, computer, python, dbms, data_struct, percentage, grade)
            messagebox.showinfo("Success", "Student added successfully...!")
            window.destroy()
            main_screen()

    add_btn = tk.Button(text="Submit", fg="white", bg="green", width=20, command=to_add).place(x=180, y=400)

    def back_window() :
        window.destroy()
        main_screen()

    back_btn = tk.Button(text="Back", fg="white", bg="red", width=20, command=back_window).place(x=180, y=450)

    window.mainloop()

def add_student() :
    window = tk.Tk()
    window.geometry("480x550")
    window.title("Student Management")

    head  = tk.Label(text="\nAdd a Student\n", fg="blue", font=("arial", 18, BOLD)).pack()

    lab = tk.Label(text="Student ID : ", font=("arial", 12, BOLD)).place(x=80, y=100)
    tkid = tk.Entry(width=30, fg="blue", bg="white")
    tkid.place(x=185, y=102)

    lab = tk.Label(text="Name : ", font=("arial", 12, BOLD)).place(x=90, y=150)
    tkname = tk.Entry(width=30, fg="blue", bg="white")
    tkname.place(x=185, y=152)

    lab = tk.Label(text="Age : ", font=("arial", 12, BOLD)).place(x=90, y=200)
    tkage = tk.Entry(width=30, fg="blue", bg="white")
    tkage.place(x=185, y=202)

    lab = tk.Label(text="Mail ID : ", font=("arial", 12, BOLD)).place(x=90, y=250)
    tkmail = tk.Entry(width=30, fg="blue", bg="white")
    tkmail.place(x=185, y=252)

    lab = tk.Label(text="Course : ", font=("arial", 12, BOLD)).place(x=90, y=300)
    tkcourse = tk.Entry(width=30, fg="blue", bg="white")
    tkcourse.place(x=185, y=302)

    lab = tk.Label(text="Stream : ", font=("arial", 12, BOLD)).place(x=90, y=350)
    tkstream = tk.Entry(width=30, fg="blue", bg="white")
    tkstream.place(x=185, y=352)

    def to_add() :
        id = tkid.get()
        name = tkname.get()
        age = tkage.get()
        mail = tkmail.get()
        course = tkcourse.get()
        stream = tkstream.get()
        try :
            id = int(id)
            age = int(age)
            id_list, mail_list = check_id()
            if name.isalpha() == True :
                if '@' not in mail :
                    messagebox.showwarning("Wrong E-mail", "Please input valid email...!")
                else :
                    if mail not in mail_list and id not in id_list:
                        window.destroy()
                        add_marks(id, name, age, mail, course, stream)
                    else :
                        messagebox.showwarning("Warning", "Id or E-mail already exists...!")
            else :
                messagebox.showwarning("Wrong Name", "Please input valid name...!")
        
        except :
            messagebox.showwarning("Id or age must be numeric...!")

    add_btn = tk.Button(text="Submit", fg="white", bg="green", width=20, command=to_add).place(x=180, y=400)

    def back_window() :
        window.destroy()
        main_screen()

    back_btn = tk.Button(text="Back", fg="white", bg="red", width=20, command=back_window).place(x=180, y=450)

    window.mainloop()

# REMOVE STUDENT
def remove_student() :
    window = tk.Tk()
    window.geometry("480x350")
    window.title("Student Management")

    head  = tk.Label(text="\nRemove a Student\n", fg="blue", font=("arial", 18, BOLD)).pack()

    lab = tk.Label(text="Enter the Student ID whom you want to remove : ", font=("arial", 12, BOLD)).pack()
    
    lab = tk.Label(text=" ").pack()
    
    tkid = tk.Entry(width=30, fg="blue", bg="white")
    tkid.pack()

    lab = tk.Label(text=" ").pack()

    def to_remove() :
        id = tkid.get()
        try :
            id = int(id)
            id_list, mail_list = check_id()
            if str(id) not in id_list :
                messagebox.showwarning("No Id", "Id does not exists...!")
            else :
                delete_student(id)
                messagebox.showinfo("Success", "Student Removed Successfully...!")
                window.destroy()
                main_screen()
        except :
            messagebox.showwarning("Wrong Id", "Id must be numeric...!")

    remove_btn = tk.Button(text="Remove Student", fg="white", bg="green", width=20, command=to_remove).pack()

    lab = tk.Label(text=" ").pack()

    def back_window() :
        window.destroy()
        main_screen()

    back_btn = tk.Button(text="Back", fg="white", bg="red", width=20, command=back_window).pack()

    window.mainloop()

# MAIL REPORT
def body_mail(id) :
    sender = "pythons2021@gmail.com"
    password = "sjls vnkb gymr ldlb"
    reciever = get_mail_id(id)

    percentage, grade = percentage_student(id)

    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = reciever

    msg["Subject"] = "Report Card"
    grading = """Please look after your Report Card
    Grading System =>
    91% to 100% - A+
    81% to 90% - A
    71% to 80% - B+
    61% to 70% - B
    51% to 60% - C
    41% to 50% - D
    34% to 40% - E
    Below 33% - F (FAIL)\n"""

    if percentage<=100 and percentage>=61 :
        message = "Congratulations...! You Passed the final exam\nGrade : " + grade + "\nYou did great, Keep it up...!"
    elif percentage<=60 and percentage>=34 :
        message = "Congratulations...! You Passed the final exam\nGrade : " + grade + "\nYou did great, But you need little improvement...!"
    elif percentage<=33 :
        message = "Sorry...! You Failed the exam\nGrade : " + grade + "\nBetter Luck next time...!"

    body = grading + message
    msg.attach(MIMEText(body, "plain"))

    server = smtplib.SMTP("smtp.gmail.com", 587)

    server.starttls()
    server.login(sender, password)

    text = msg.as_string()
    server.sendmail(sender, reciever, text)

    server.quit()

def send_mail() :
    window = tk.Tk()
    window.geometry("480x350")
    window.title("Student Management")

    head  = tk.Label(text="\nSend report to Student\n", fg="blue", font=("arial", 18, BOLD)).pack()

    lab = tk.Label(text="Enter the Student ID whom you want to send the report : ", font=("arial", 12, BOLD)).pack()
    
    lab = tk.Label(text=" ").pack()
    
    tkid = tk.Entry(width=30, fg="blue", bg="white")
    tkid.pack()

    lab = tk.Label(text=" ").pack()

    def to_mail() :
        id = tkid.get()
        try :
            id = int(id)
            id_list, mail_list = check_id()
            if str(id) not in id_list :
                messagebox.showwarning("No Id", "Id does not exists...!")
            else :
                answer = messagebox.askquestion("Send", "Are you sure?")
                if answer == "yes" :
                    body_mail(id)
                    messagebox.showinfo("Success", "Report Send Successfully...!")
                    window.destroy()
                    send_mail()
        except :
            messagebox.showwarning("Wrong Id", "Id must be numeric...!")

    send_btn = tk.Button(text="Send Report", fg="white", bg="green", width=20, command=to_mail).pack()

    lab = tk.Label(text=" ").pack()

    def back_window() :
        window.destroy()
        main_screen()

    back_btn = tk.Button(text="Back", fg="white", bg="red", width=20, command=back_window).pack()

    window.mainloop()

# MAIN SCREEN 
def main_screen() :
    window = tk.Tk()
    window.geometry("480x400")
    window.title("Student Management")

    head  = tk.Label(text="\nWelcome to Student Management...!\n", fg="blue", font=("arial", 18, BOLD)).pack()
    
    def to_show() :
        window.destroy()
        show_student()

    show_btn = tk.Button(text="Show Student Details", fg="white", bg="green", width=20, command=to_show).place(x=20, y=120)

    def to_add() :
        window.destroy()
        add_student()

    add_btn = tk.Button(text="Add Student", fg="white", bg="green", width=20, command=to_add).place(x=300, y=120)

    def to_remove() :
        window.destroy()
        remove_student()

    remove_btn = tk.Button(text="Remove Student", fg="white", bg="green", width=20, command=to_remove).place(x=20, y=220)

    def to_send() :
        window.destroy()
        send_mail()

    send_btn = tk.Button(text="Send Report", fg="white", bg="green", width=20, command=to_send).place(x=300, y=220)

    def exit_window() :
        answer = messagebox.askquestion("Exit", "Are you sure?")
        if answer == "yes" :
            window.destroy()

    exit_btn = tk.Button(text="EXIT", fg="white", bg="red", width=20, command=exit_window).place(x=160, y=300)

    window.mainloop()

main_screen()