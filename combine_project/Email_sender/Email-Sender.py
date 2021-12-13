import tkinter as tk
from tkinter import *
from tkinter import font
from tkinter.font import BOLD
from tkinter import messagebox
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def body_mail(reciever) :
    sender = "pythons2021@gmail.com"
    password = "whze hqve awkc otgd"

    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = reciever

    msg["Subject"] = s_4.get()

    body = s_5.get(1.0, "end-1c")
    msg.attach(MIMEText(body, "plain"))

    server = smtplib.SMTP("smtp.gmail.com", 587)

    server.starttls()
    server.login(sender, password)

    text = msg.as_string()
    server.sendmail(sender, reciever, text)

    server.quit()
    messagebox.showinfo("Successfull", "Email send Successfully...!")
    main_window.destroy()
    main()

def main():
    global s_2,s_4,s_5
    global main_window
    main_window=tk.Tk()
    main_window.geometry("500x650")
    main_window.resizable(False,False)
    main_window.title("Email-Sender")
    main_window.config(background="Orange")
    head1=tk.Label(main_window,text="",bg="orange")
    head1.pack()
    head=tk.Label(main_window,text="EMAIL SENDER",font=("ariel",18,BOLD),fg="white",bg="orange")
    head.pack()
    s_1=tk.Label(main_window,text="Reciever :",font=("ariel",12,BOLD),fg="white",bg="orange")
    s_1.place(x=10,y=120)
    s_2=tk.Entry(main_window,font="ariel",width=40)
    s_2.place(x=120,y=120)
    s_3=tk.Label(main_window,text="subject :",font=("ariel",12,BOLD),fg="white",bg="orange")
    s_3.place(x=10,y=170)
    s_4=tk.Entry(main_window,font="ariel",width=40)
    s_4.place(x=120,y=170)
    s_5 = tk.Text(main_window, height = 15, width = 49)
    s_5.place(x=50,y=250)

    def to_send():
        reciever = s_2.get()
        if "@" in reciever and "." in reciever: 
            body_mail(reciever)
        else:
            messagebox.showwarning("WARNING","Email must contain @ and .")

    s_6=tk.Button(main_window,text="Send Email",font=("ariel",10,BOLD),fg="white",bg="green",width=10,command=to_send)
    s_6.place(x=200,y=520)

    def to_exit():
        main_window.destroy()

    s_7=tk.Button(main_window,text="Exit",font=("ariel",10,BOLD),fg="white",bg="red",width=10,command=to_exit)
    s_7.place(x=200,y=560)
    main_window.mainloop()

main()