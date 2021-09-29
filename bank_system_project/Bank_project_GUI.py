import tkinter as tk
from tkinter.font import BOLD
from tkinter import messagebox
import json
import os
from tkinter.constants import RIGHT, Y
from datetime import datetime
from PIL import Image, ImageTk
############################ FILES ###########################################
file = "user_details.json"
file_2 = "special_id.txt"
file_3 = "password.json"
file_4 = "transaction.json"
file_5 = "y.txt"
file_6 = "trans_history.json"
file_7 = "saving.json"
############################ END ###########################################

############################ SAVINGS ###########################################
def saving_acc(user_name, to_save, from_save) :
    with open(file_4, 'r') as r :
        money_dict = json.load(r)
    money = money_dict[user_name]
    with open(file_7, 'r') as r :
        save_dict = json.load(r)
    saving = save_dict[user_name]
    
    if to_save != 0 :
        saving = saving + to_save
        save_dict[user_name] = saving
        with open(file_7, 'w') as w :
            json.dump(save_dict, w, indent=4)
        money = money - to_save
        money_dict[user_name] = money
        with open(file_4, 'w') as w :
            json.dump(money_dict, w, indent=4)
    elif from_save != 0 :
        saving = saving - from_save
        save_dict[user_name] = saving
        with open(file_7, 'w') as w :
            json.dump(save_dict, w, indent=4)
        money = money + from_save
        money_dict[user_name] = money
        with open(file_4, 'w') as w :
            json.dump(money_dict, w, indent=4)
        
    saving_gui(user_name)

def saving_gui(user_name) :
    saving = tk.Tk()
    saving.geometry("1000x500")
    saving.title("Banking System")

    head = tk.Label(text="\nSavings", font=("arial", 18, BOLD)).pack()

    des = tk.Label(text="\n***Welcome to your Savings, here you can save your money and you can withdraw it whenever there is a strong need***", font=("arial", 12), fg="red").pack()

    lab = tk.Label(text=" ").pack()

    with open(file_7, 'r') as r :
        a = json.load(r)
    savings = a[user_name]
    with open(file_4, 'r') as r :
        money_dict = json.load(r)
    money = money_dict[user_name]
    money = int(money)

    lab = tk.Label(text="Your savings : " + str(savings), fg="blue", font=("arial", 15, BOLD)).pack()
    def to_save_acc() :
        saving.destroy()
        save_money = tk.Tk()
        save_money.geometry("500x500")
        save_money.title("Banking System")

        head = tk.Label(text="\nSavings", font=("arial", 18, BOLD)).pack()

        lab = tk.Label(text=" ").pack()

        lab = tk.Label(text="Enter money to save : ", font=("arial", 14)).pack()
        e = tk.Entry(save_money, fg="blue", bg="white", width=50)
        e.pack()

        def func1() :
            to_save = e.get()
            try :
                to_save = int(to_save)
                if money < to_save or money == 0:
                    messagebox.showwarning('showwarning', "Limit Exceeded...!")
                else :
                    save_money.destroy()
                    saving_acc(user_name, to_save, 0)
            except :
                messagebox.showwarning('showwarning', "Money must be numeric...!")

        def back() :
            save_money.destroy()
            saving_gui(user_name)
        
        lab = tk.Label(text=" ").pack()
        submit = tk.Button(text="Save", fg="white", bg="green", command=func1, width=15).pack()
        lab = tk.Label(text=" ").pack()
        back_b = tk.Button(text="Back", fg="white", bg="green", command=back, width=15).pack()

        save_money.mainloop()

    lab = tk.Label(text=" ").pack()

    save = tk.Button(text="SAVE MONEY", fg="white", bg= "green", width=15, command=to_save_acc).pack()

    lab = tk.Label(text=" ").pack()

    def to_withd_acc() :
        saving.destroy()
        save_money = tk.Tk()
        save_money.geometry("500x500")
        save_money.title("Banking System")

        head = tk.Label(text="\nSavings", font=("arial", 18, BOLD)).pack()

        lab = tk.Label(text=" ").pack()

        lab = tk.Label(text="Enter money to withdraw : ", font=("arial", 14)).pack()
        e = tk.Entry(save_money, fg="blue", bg="white", width=50)
        e.pack()

        def func1() :
            from_save = e.get()
            try :
                from_save = int(from_save)
                if savings < from_save or saving == 0:
                    messagebox.showwarning('showwarning', "Limit Exceeded...!")
                else :
                    save_money.destroy()
                    saving_acc(user_name, 0, from_save)
            except :
                messagebox.showwarning('showwarning', "Money must be numeric...!")
        def back() :
            save_money.destroy()
            saving_gui(user_name)
        lab = tk.Label(text=" ").pack()
        submit = tk.Button(text="Withdraw", fg="white", bg="green", command=func1, width=15).pack()
        lab = tk.Label(text=" ").pack()
        back_b = tk.Button(text="Back", fg="white", bg="green", command=back, width=15).pack()

        save_money.mainloop()
    
    withd = tk.Button(text="WITHDRAW MONEY", fg="white", bg= "green", width=15, command=to_withd_acc).pack()

    lab = tk.Label(text=" ").pack()

    def to_pass() :
        saving.destroy()
        Passbook(user_name)

    back_1 = tk.Button(text="BACK", fg="white", bg= "green", width=15, command=to_pass).pack()

    saving.mainloop()
############################ END ###########################################

############################ ADMIN ###########################################
def admin_acc() :
    admin = tk.Tk()
    admin.geometry("800x700")
    admin.title("Banking System")
    scroll = tk.Scrollbar(admin)
    scroll.pack(side=RIGHT, fill=Y)
    def to_login() :
        admin.destroy()
        Login()
    back = tk.Button(text="Back", bg="green", fg="white", width=10, command=to_login).place(x=500, y=10)
    head = tk.Label(text="\nCustomers\n", font=("arial", 18)).pack()

    if os.path.exists(file) :
        with open(file, 'r') as r :
            user_dict = json.load(r)
        unique = open(file_2, 'r')
        customer = unique.read()
        customer = int(customer)
        i=1
        while i<customer :
            data = user_dict[str(i)]
            a = 10
            unique_2 = open(file_5, 'r')
            b = unique_2.read()
            b = int(b)
            for key, value in data.items() :
                if key == "password" :
                    continue
                if key == "name":
                    lab_1 = tk.Label(admin, text=key + ' : ', font=("arial", 12, BOLD)).place(x=a, y=b)
                    lab_2 = tk.Label(admin, text=str(value), font=("arial", 12), fg="blue").place(x=a+60, y=b)
                if key == "age" :
                    lab_1 = tk.Label(admin, text=key + ' : ', font=("arial", 12, BOLD)).place(x=a, y=b)
                    lab_2 = tk.Label(admin, text=str(value), font=("arial", 12), fg="blue").place(x=a+50, y=b)
                if key == "number" or key == "address" :
                    lab_1 = tk.Label(admin, text=key + ' : ', font=("arial", 12, BOLD)).place(x=a, y=b)
                    lab_2 = tk.Label(admin, text=str(value), font=("arial", 12), fg="blue").place(x=a+80, y=b)
                if key == "adhar_number" or key == "account_type":
                    lab_1 = tk.Label(admin, text=key + ' : ', font=("arial", 12, BOLD)).place(x=a, y=b)
                    lab_2 = tk.Label(admin, text=str(value), font=("arial", 12), fg="blue").place(x=a+130, y=b)
                if key == "Username" :
                    lab_1 = tk.Label(admin, text=key + ' : ', font=("arial", 12, BOLD)).place(x=a, y=b)
                    lab_2 = tk.Label(admin, text=str(value), font=("arial", 12), fg="blue").place(x=a+100, y=b)
                if key == "account_number" :
                    lab_1 = tk.Label(admin, text=key + ' : ', font=("arial", 12, BOLD)).place(x=a, y=b)
                    lab_2 = tk.Label(admin, text=str(value), font=("arial", 12), fg="blue").place(x=a+150, y=b)
                b = b+40
            lab = tk.Label(text="**************************************************************", font=("arial", 15, BOLD)).place(x=a, y=b+10)
            i = i+1
            y_val = b+50
            f = open(file_5, 'w')
            f.write(str(y_val))
            f.close()
    else :
        lab = tk.Label(text="NO CUSTOMERS YET...!", font=("arial", 15, BOLD)).pack()
    admin.mainloop()
############################ END ###########################################

############################ TRANSACTION HISTORY ###########################################
def trans_history(user_name) :
    history_window = tk.Tk()
    history_window.geometry("600x600")
    history_window.title("Banking System")
    def to_pass() :
        history_window.destroy()
        Passbook(user_name)
    back = tk.Button(text="Back", bg="green", fg="white", width=10, command=to_pass).place(x=500, y=10)
    head = tk.Label(text="Transaction History\n", font=("arial", 18)).pack()

    with open(file_6, 'r') as r :
        history_dict = json.load(r)
    history = history_dict[user_name]
    if history :
        with open(file_4, 'r') as r :
            trans = json.load(r)
        lab = tk.Label(text="Current Balance : " + str(trans[user_name]), font=("arial", 15)).pack()
        l = tk.Label(text=" ").pack()
        for key, value in history.items() :
            d, t, action = key.split("@")
            lab_1 = tk.Label(text="Dated : " + d + ' at ' + t, font=("arial", 12)).pack()
            if action == 'd' :
                lab_2 = tk.Label(text="Deposited : " + str(value), font=("arial", 12)).pack()
            elif action == 'w' :
                lab_2 = tk.Label(text="Withdrawed : " + str(value), font=("arial", 12)).pack()
            lab_3 = tk.Label(text=" ").pack()
    else :
        lab = tk.Label(text="No Transaction history...!", font=("arial", 15, BOLD), fg="red").pack()
    history_window.mainloop()
############################ END ###########################################

############################# TRANSACTION ###########################################
def tdeposit():
    twindow.destroy()
    deposit()

def twithdrawal():
    twindow.destroy()
    withdrawal()

def dtransaction():
    dwindow.destroy()
    transaction()

def wtransaction():
    wwindow.destroy()
    transaction()

def wdeposit():
    wwindow.destroy()
    deposit()

def dwithdrawal():
    dwindow.destroy()
    withdrawal()

def ddeposit():
    dwindow.destroy()
    deposit()

def wwithdrawal():
    wwindow.destroy()
    withdrawal()

def calcd():
    damount=d_5.get()
    try:
        damount=int(damount)
        if(damount>10000)or(damount<1):
            messagebox.showinfo("showinfo","Limit is between 1 and 10000")
            ddeposit()
        elif(damount<=10000)or(damount>=1):
            now=datetime.now()
            key=now.strftime("%d/%m/%Y@%H:%M:%S")+"@d"
            with open(file_6, 'r') as r :
                t_hdict1 = json.load(r)
            data = t_hdict1[uname]
            data[key] = damount
            t_hdict1[uname] = data
            with open("trans_history.json","w") as w:
                json.dump(t_hdict1, w, indent=4)
            with open(file_4,"r") as r:
                tdict=json.load(r)
            tdict[uname]=int(tdict[uname])+damount
            with open(file_4,"w") as w:
                json.dump(tdict, w, indent=4)
            dtransaction()
    except:
        messagebox.showerror("showerror","Please enter valid input!")
        ddeposit()

def calcw():
    wamount=w_5.get()
    try:
        wamount=int(wamount)
        with open(file_4,"r") as r:
            tdict=json.load(r)
        if(wamount<=int(tdict[uname])):
            if(wamount>10000)or(wamount<1):
                messagebox.showinfo("showinfo","Limit is between 1 and 10000")
                wwithdrawal()
            elif(wamount<=10000)or(wamount>=1):
                now=datetime.now()
                key=now.strftime("%d/%m/%Y@%H:%M:%S")+"@w"
                with open(file_6, 'r') as r :
                    t_hdict1 = json.load(r)
                data = t_hdict1[uname]
                data[key] = wamount
                t_hdict1[uname] = data
                with open("trans_history.json","w") as w:
                    json.dump(t_hdict1, w, indent=4)
                with open(file_4,"r") as r:
                    tdict=json.load(r)
                tdict[uname]=int(tdict[uname])-wamount
                with open(file_4,"w") as w:
                    json.dump(tdict, w, indent=4)
                wtransaction()
        elif(wamount>int(tdict[uname])):
            messagebox.showwarning("showwarning","Limit Exceeded...!")
            wwithdrawal()

    except:
        messagebox.showerror("showerror","Please enter valid input!")
        wwithdrawal()

def deposit():
    global dwindow
    global damount
    global d_5
    dwindow=tk.Tk()   
    dwindow.geometry("300x300")
    dwindow.title("deposit")
    d_1=tk.Label(dwindow,text="DEPOSIT",font=("Ariel",12,BOLD))
    d_1.place(x=100,y=20)
    d_2=tk.Label(dwindow,text="Your current balance :",font=("Ariel",10))
    d_2.place(x=20,y=60)
    d_3=tk.Label(dwindow,text=tdict[uname],font=("Ariel",10))
    d_3.place(x=180,y=60)
    d_4=tk.Label(dwindow,text="Enter the amount :",font=("Ariel",10))
    d_4.place(x=20,y=100)
    d_5=tk.Entry(dwindow)
    d_5.place(x=150,y=100)

    d_6=tk.Button(dwindow,text="Deposit",width=10,bg="green", fg="white",command=calcd)
    d_6.place(x=112,y=140)
    d_7=tk.Button(dwindow,text="Back",width=10,bg="green", fg="white",command=dtransaction)
    d_7.place(x=20,y=180)
    d_7=tk.Button(dwindow,text="Withdrawal",width=10,bg="green", fg="white",command=dwithdrawal)
    d_7.place(x=200,y=180)
    dwindow.mainloop()

def withdrawal():
    global wwindow
    global wamount
    global w_5
    wwindow=tk.Tk()   
    wwindow.geometry("300x300")
    wwindow.title("withdrawal")
    w_1=tk.Label(wwindow,text="WITHDRAWAL",font=("Ariel",12,BOLD))
    w_1.place(x=80,y=20)
    w_2=tk.Label(wwindow,text="Your current balance :",font=("Ariel",10))
    w_2.place(x=20,y=60)
    w_3=tk.Label(wwindow,text=tdict[uname],font=("Ariel",10))
    w_3.place(x=180,y=60)
    w_4=tk.Label(wwindow,text="Enter the amount :",font=("Ariel",10))
    w_4.place(x=20,y=100)
    w_5=tk.Entry(wwindow)
    wamount=w_5.get()
    w_5.place(x=150,y=100)
    w_6=tk.Button(wwindow,text="Withdraw",width=10,bg="green", fg="white",command=calcw)
    w_6.place(x=112,y=140)
    w_7=tk.Button(wwindow,text="Back",width=10,bg="green", fg="white",command=wtransaction)
    w_7.place(x=20,y=180)
    w_7=tk.Button(wwindow,text="Deposit",width=10,bg="green", fg="white",command=wdeposit)
    w_7.place(x=200,y=180)
    wwindow.mainloop()
    
def transaction():
    global twindow
    global uname
    global tdict
    uname = user_1
    twindow=tk.Tk()
    twindow.geometry("300x300")
    twindow.title("transaction")
    with open(file_4,"r") as r:
        tdict=json.load(r)
    t_1=tk.Label(twindow,text="TRANSACTION",font=("Ariel",12,BOLD))
    t_1.place(x=80,y=20)
    t_2=tk.Label(twindow,text="Your current balance :",font=("Ariel",10))
    t_2.place(x=20,y=60)
    t_3=tk.Label(twindow,text=tdict[uname],font=("Ariel",10))
    t_3.place(x=180,y=60)

    t_4=tk.Button(twindow,text="Deposit",bg="green", fg="white",width=10,command=tdeposit)
    t_4.place(x=110,y=100)

    t_5=tk.Button(twindow,text="Withdrawal",bg="green", fg="white",width=10,command=twithdrawal)
    t_5.place(x=110,y=140)
    
    def to_passbook() :
        twindow.destroy()
        Passbook(uname)

    t_6=tk.Button(twindow,text="Back",bg="green", fg="white",width=10, command=to_passbook)
    t_6.place(x=110,y=180)
    twindow.mainloop()
############################ END ###########################################

############################ DELETE ACCOUNT ###########################################
def to_main() :
    passbook.destroy()
    main_screen()

def acc_delete(user_name) :
    with open(file_4, 'r') as r :
        money_dict = json.load(r)
    money = money_dict[user_name]
    money = int(money)
    if money == 0 :
        count = open(file_2, 'r')
        customer = count.read()
        customer = int(customer)
        with open(file, 'r') as r :
            user_dict = json.load(r)
        for i in range(1, customer) :
            data = user_dict[str(i)]
            if data["Username"] == user_name :
                data["Status"] = "deleted"
                user_dict[str(i)] = data
                with open(file, 'w') as w :
                    json.dump(user_dict, w, indent=4)
                with open(file_3, 'r') as r :
                    user = json.load(r)
                del user[user_name]
                with open(file_3, 'w') as w :
                    json.dump(user, w, indent=4)
                del money_dict[user_name]
                with open(file_4, 'w') as w :
                    json.dump(money_dict, w, indent=4)
        to_main()
    else :
        messagebox.showwarning("showwarning","Please withdraw your all money before deleting your account...!")
############################ END ###########################################

############################# PASSBOOK ###########################################
def Passbook(user_name) :
    global user_1
    user_1 = user_name
    global passbook
    passbook = tk.Tk()
    passbook.geometry("500x600")
    passbook.title("Banking System")

    head = tk.Label(text="\nUser Details\n", font=("Arial", 18)).pack()
    
    with open(file, 'r') as r :
        user_dict = json.load(r)

    unique = open(file_2, 'r')
    customer = unique.read()
    customer = int(customer)
    for i in range(1, customer) :
        data = user_dict[str(i)]
        if data["Username"] == user_name :
            name = data["name"]
            name = name.upper()
            lab_1 = tk.Label(text="Name : ", font=("arial", 12, BOLD)).place(x=10, y=60)
            lab_2 = tk.Label(text=name, font=("arial", 12), fg="blue").place(x=70, y=60)

            lab_3 = tk.Label(text="Age : ", font=("arial", 12, BOLD)).place(x=10, y=100)
            lab_4 = tk.Label(text=data["age"], font=("arial", 12), fg="blue").place(x=60, y=100)

            lab_5 = tk.Label(text="Number : ", font=("arial", 12, BOLD)).place(x=10, y=140)
            lab_6 = tk.Label(text=data["number"], font=("arial", 12), fg="blue").place(x=90, y=140)

            lab_7 = tk.Label(text="Address : ", font=("arial", 12, BOLD)).place(x=10, y=180)
            lab_8 = tk.Label(text=data["address"], font=("arial", 12), fg="blue").place(x=90, y=180)

            lab_9 = tk.Label(text="Adhar Number : ", font=("arial", 12, BOLD)).place(x=10, y=220)
            lab_10 = tk.Label(text=data["adhar_number"], font=("arial", 12), fg="blue").place(x=140, y=220)

            lab_11 = tk.Label(text="Username : ", font=("arial", 12, BOLD)).place(x=10, y=260)
            lab_12 = tk.Label(text=data["Username"], font=("arial", 12), fg="blue").place(x=110, y=260)

            lab_13 = tk.Label(text="Account Number : ", font=("arial", 12, BOLD)).place(x=10, y=300)
            lab_14 = tk.Label(text=data["account_number"], font=("arial", 12), fg="blue").place(x=160, y=300)

            lab_15 = tk.Label(text="Account Type : ", font=("arial", 12, BOLD)).place(x=10, y=340)
            lab_16 = tk.Label(text=data["account_type"], font=("arial", 12), fg="blue").place(x=140, y=340)
        else :
            pass
    
    def log_out() :
        passbook.destroy()
        Login()

    def destroy_passbook() :
        passbook.destroy()
        transaction()

    def to_history() :
        passbook.destroy()
        trans_history(user_name)

    def delete_acc() :
        acc_delete(user_name)
    
    def to_savings() :
        passbook.destroy()
        saving_gui(user_name)

    trans = tk.Button(text="Deposit/Withdraw money", bg="green", fg="white", width=20, command=destroy_passbook).place(x=10, y=400)
    tran_history = tk.Button(text="Transaction History", bg="green", fg="white", width=20, command=to_history).place(x=175, y=400)
    save_ac = tk.Button(text="Start Savings", bg="green", fg="white", width=20, command=to_savings).place(x=340, y=400)
    logout = tk.Button(text="Log out", bg="green", fg="white", width=20, command=log_out).place(x=175, y=470)
    delete = tk.Button(text="Delete Acc.", bg="green", fg="white", width=20, command=delete_acc).place(x=175, y=540)    
    passbook.mainloop()
############################ END ###########################################

############################# LOGIN ###########################################
def login_data() :
    try :
        user_name = username_login.get()
        user_password = password_login.get()
        if user_name == "admin" and user_password == "#admin_12" :
            unique_4 = open(file_5, 'w')
            unique_4.write("60")
            unique_4.close()
            try :
                window_1.destroy()
                admin_acc()
            except :
                window.destroy()
                admin_acc()
        elif user_name == "admin" and user_password != "#admin_12" :
            try :
                window_1.destroy()
                Login_dup("Invalid Password...!")
            except :
                window.destroy()
                Login_dup("Invalid Password...!")
        else :
            return user_name, user_password
    except :
        user_name = username_login_1.get()
        user_password = password_login_1.get()
        if user_name == "admin" and user_password == "#admin_12" :
            unique_4 = open(file_5, 'w')
            unique_4.write("60")
            unique_4.close()
            try :
                window_1.destroy()
                admin_acc()
            except :
                window.destroy()
                admin_acc()
        elif user_name == "admin" and user_password != "#admin_12" :
            try :
                window_1.destroy()
                Login_dup("Invalid Password...!")
            except :
                window.destroy()
                Login_dup("Invalid Password...!")
        else :
            return user_name, user_password

def login_json() :
    file = "password.json"
    if os.path.exists(file) :
        with open(file, 'r') as r :
            user_dict = json.load(r)
        user_list = list(user_dict.keys())
        user_name, user_password = login_data()
        while True :
            if user_name in user_list :
                if user_password == user_dict[user_name] :
                    print("Login successful...!")
                    try :
                        window_1.destroy()
                        Passbook(user_name)
                    except :
                        window.destroy()
                        Passbook(user_name)
                elif user_password != user_dict[user_name] :
                    print("Invalid Password...!")
                    try :
                        window_1.destroy()
                        Login_dup("Invalid Password...!")
                    except :
                        window.destroy()
                        Login_dup("Invalid Password...!")
            elif user_name not in user_list :
                print("Username does not exists...!")
                try :
                    window_1.destroy()
                    Login_dup("Username does not exists...!")
                except :
                    window.destroy()
                    Login_dup("Username does not exists...!")
    else :
        print("Please register first...!")
        try :
            window_1.destroy()
            Login_dup("Please register first...!")
        except :
            window.destroy()
            Login_dup("Please register first...!")

def Login() :
    global window
    window = tk.Tk()
    window.geometry("400x350")
    window.title("Banking System")

    head = tk.Label(window, text="\nLogin Page\n", font=("Arial", 20)).pack()

    l_1 = tk.Label(window, text="Username : ").place(x=70, y=100)
    global username_login
    username_login = tk.Entry(window, fg='blue', bg='white', width=30)
    username_login.place(x=140, y=100)

    l_2 = tk.Label(window, text="Password : ").place(x=70, y=150)
    global password_login
    password_login = tk.Entry(window, fg='blue', bg='white', width=30, show="*")
    password_login.place(x=140, y=150)

    login = tk.Button(window, text="Login", bg="green", fg="white", command=login_json).place(x=190, y=190)
    
    def redirect_to_register() :
        window.destroy()
        Register()

    l_3 = tk.Label(window, text="Not a user? Register here : ", fg="blue").place(x=80, y=300)
    to_register = tk.Button(window, text="Register", bg="green", fg="white", command=redirect_to_register).place(x=225, y=300)

    window.mainloop()

def Login_dup(msg) :
    global window_1
    window_1 = tk.Tk()
    window_1.geometry("400x350")
    window_1.title("Banking System")

    head = tk.Label(window_1, text="\nLogin Page\n", font=("Arial", 20)).pack()

    l_1 = tk.Label(window_1, text="Username : ").place(x=70, y=100)
    global username_login_1
    username_login_1 = tk.Entry(window_1, fg='blue', bg='white', width=30)
    username_login_1.place(x=140, y=100)

    l_2 = tk.Label(window_1, text="Password : ").place(x=70, y=150)
    global password_login_1
    password_login_1 = tk.Entry(window_1, fg='blue', bg='white', width=30, show="*")
    password_login_1.place(x=140, y=150)

    login = tk.Button(window_1, text="Login", bg="green", fg="white", command=login_json).place(x=190, y=190)
    
    lab = tk.Label(text=msg, fg="red")
    lab.place(x=100, y=250)

    def redirect_to_register() :
        window_1.destroy()
        Register()

    l_3 = tk.Label(window_1, text="Not a user? Register here : ", fg="blue").place(x=80, y=300)
    to_register = tk.Button(window_1, text="Register", bg="green", fg="white", command=redirect_to_register).place(x=225, y=300)

    window_1.mainloop()
############################ END ###########################################

############################# REGISTER ###########################################
def register_data() :
    global first
    global last
    global age_1
    global number
    global add
    global adhar
    global account
    global u_name
    global u_pass

    try :
        FName = name_1.get()
        first = FName
        
        LName = name_2.get()
        last = LName
        
        age = Age.get()
        age_1 = age
        
        num = Num.get()
        number = num
        
        address = Address.get()
        add = address
        
        adhar_card = Adhar_card.get()
        adhar = adhar_card
        
        acc_type = Acc_type.get()
        account = acc_type

        user_name = username.get()
        u_name = user_name
        
        user_password = password.get()
        u_pass = user_password
    except :
        FName = name_1_1.get()
        first = FName
        
        LName = name_2_2.get()
        last = LName
        
        age = Age_1.get()
        age_1 = age
        
        num = Num_1.get()
        number = num
        
        address = Address_1.get()
        add = address
        
        adhar_card = Adhar_card_1.get()
        adhar = adhar_card

        acc_type = Acc_type_1.get()
        account = acc_type
        
        user_name = username_1.get()
        u_name = user_name
        
        user_password = password_1.get()
        u_pass = user_password
    return FName, LName, age, num, address, adhar_card, acc_type, user_name, user_password

def register_in_json() : 
    FName, LName, age, num, address, adhar_card, acc_type, user_name, user_password = register_data()

    while True:
        if FName.isalpha() == True :
            break
        else:
            print("Plese enter accepetable name...!")
            try :
                new_window.destroy()
                Register_dup("Plese enter accepetable name...!")
            except :
                new_window_1.destroy()
                Register_dup("Plese enter accepetable name...!")
    
    while True:
        if LName.isalpha() == True :
            break
        else:
            print("Plese enter accepetable name...!")
            print("First name : {}".format(FName))
            try :
                new_window.destroy()
                Register_dup("Plese enter accepetable name...!")
            except :
                new_window_1.destroy()
                Register_dup("Plese enter accepetable name...!")
    
    name = FName + ' ' + LName
    
    while True :
        try :
            while True :
                age = int(age)
                if age <= 17 :
                    print("Age must be greater than or equal to 18...!")
                    print("Name : {}".format(name))
                    try :
                        new_window.destroy()
                        Register_dup("Age must be greater than or equal to 18...!")
                    except :
                        new_window_1.destroy()
                        Register_dup("Age must be greater than or equal to 18...!")
                elif age >= 18 :
                    break
            break
        except :
            print("Age must be in numbers...!")
            print("Name : {}".format(name))
            try :
                new_window.destroy()
                Register_dup("Age must be in numbers...!")
            except :
                new_window_1.destroy()
                Register_dup("Age must be in numbers...!")
    
    while True :
        try :
            while True :
                if len(num) != 10 :
                    print("Phone number must be of 10-digits only...!")
                    print("Name : {}".format(name))
                    print("Age : {}".format(age))
                    try :
                        new_window.destroy()
                        Register_dup("Phone number must be of 10-digits only...!")
                    except :
                        new_window_1.destroy()
                        Register_dup("Phone number must be of 10-digits only...!")
                elif len(num) == 10 :
                    num=int(num)
                    break
            break
        except :
            print("Phone number must be in numbers...!")
            print("Name : {}".format(name))
            print("Age : {}".format(age))
            try :
                new_window.destroy()
                Register_dup("Phone number must be in numbers...!")
            except :
                new_window_1.destroy()
                Register_dup("Phone number must be in numbers...!")
    
    while True :
        try :
            while True :
                if len(adhar_card) != 12 :
                    print("Adhar number must be of 12-digits only...!")
                    print("Name : {}".format(name))
                    print("Age : {}".format(age))
                    print("Number : {}".format(num))
                    print("Address : {}".format(address))
                    try :
                        new_window.destroy()
                        Register_dup("Adhar number must be of 12-digits only...!")
                    except :
                        new_window_1.destroy()
                        Register_dup("Adhar number must be of 12-digits only...!")
                elif len(adhar_card) == 12 :
                    adhar_card = int(adhar_card)
                    break
            break
        except :
            print("Adhar number must be in numbers...!")
            print("Name : {}".format(name))
            print("Age : {}".format(age))
            print("Number : {}".format(num))
            print("Address : {}".format(address))
            try :
                new_window.destroy()
                Register_dup("Adhar number must be in numbers...!")
            except :
                new_window_1.destroy()
                Register_dup("Adhar number must be in numbers...!")

    while True :
        if acc_type == "current" or acc_type == "savings" or acc_type == "saving" :
            break
        else :
            try :
                new_window.destroy()
                Register_dup("Please choose current or savings...!")
            except :
                new_window_1.destroy()
                Register_dup("Please choose current or savings...!")

    while True :
        if '#' in user_password or '@' in user_password or '&' in user_password :
            break
        else :
            print("Password must contain # or @ or &...!")
            print("Username : {}".format(user_name))    
            try :
                new_window.destroy()
                Register_dup("Password must contain # or @ or &...!")
            except :
                new_window_1.destroy()
                Register_dup("Password must contain # or @ or &...!")
    if os.path.exists(file_3) :
        with open(file_3, 'r') as r :
            user_dict = json.load(r)
        user_list = list(user_dict.keys())
        while True :
            if user_name not in user_list :
                user_dict[user_name] = user_password
                with open(file_3, 'w') as w :
                    json.dump(user_dict, w, indent=4)
                break
            elif user_name in user_list :
                print("Username already exists...!")
                try :
                    new_window.destroy()
                    Register_dup("Username already exists...!")
                except :
                    new_window_1.destroy()
                    Register_dup("Username already exists...!")
    else :
        user_dict = {user_name : user_password}
        with open(file_3, 'w') as w :
            json.dump(user_dict, w, indent=4)
    if os.path.exists(file) :
        unique = open(file_2, 'r')
        id = unique.read()
        unique.close()
        account_no = user_name + '@' + id
        id_1 = int(id)
        id_1 = id_1+1
        unique_1 = open(file_2, 'w')
        unique_1.write(str(id_1))
        unique_1.close()
        user_dict = {
            id : {
                "name" : name,
                "age" : age,
                "number" : num,
                "address" : address,
                "adhar_number" : adhar_card,
                "Username" : user_name,
                "password" : user_password,
                "account_number" : account_no,
                "account_type" : acc_type
            }
        }
        with open(file, 'r') as r :
            data = json.load(r)
        data.update(user_dict)
        with open(file, 'w') as w :
            json.dump(data, w, indent=4)
        with open(file_4, 'r') as r :
            balance = json.load(r)
        balance[user_name] = "0"
        with open(file_4, 'w') as w :
            json.dump(balance, w, indent=4)
        with open(file_6, 'r') as r :
            history = json.load(r)
        history[user_name] = {}
        with open(file_6, 'w') as w :
            json.dump(history, w, indent=4)
        sample = {user_name : 0}
        with open(file_7, 'w') as w :
            json.dump(sample, w, indent=4)
        print("Registration done...!")
        try :
            new_window.destroy()
            Login()
        except :
            new_window_1.destroy()
            Login()
    else :
        unique_3 = open(file_2, 'w')
        unique_3.write("2")
        unique_3.close()
        account_no = user_name + '@1'
        user_dict = {
            "1" : {
                "name" : name,
                "age" : age,
                "number" : num,
                "address" : address,
                "adhar_number" : adhar_card,
                "Username" : user_name,
                "password" : user_password,
                "account_number" : account_no,
                "account_type" : acc_type
            }
        }
        with open(file, 'w') as w :
            json.dump(user_dict, w, indent=4)
        balance = {user_name : "0"}
        with open(file_4, 'w') as w :
            json.dump(balance, w, indent=4)
        history = {user_name : {}}
        with open(file_6, 'w') as w :
            json.dump(history, w, indent=4)
        sample = {user_name : 0}
        with open(file_7, 'w') as w :
            json.dump(sample, w, indent=4)
        print("Registration done...!")
        try :
            new_window.destroy()
            Login()
        except :
            new_window_1.destroy()
            Login()

def Register() :
    global new_window
    new_window = tk.Tk()
    new_window.geometry("400x650")
    new_window.title("Banking System")

    head = tk.Label(new_window, text="\nRegistration Page\n", font=("Arial", 20)).pack()

    l_1 = tk.Label(new_window, text="First Name : ").place(x=70, y=100)
    global name_1
    name_1 = tk.Entry(new_window, fg='blue', bg='white', width=30)
    name_1.place(x=140, y=100)

    l_2 = tk.Label(new_window, text="Last Name : ").place(x=70, y=150)
    global name_2
    name_2 = tk.Entry(new_window, fg='blue', bg='white', width=30)
    name_2.place(x=140, y=150)

    l_3 = tk.Label(new_window, text="Age : ").place(x=70, y=200)
    global Age
    Age = tk.Entry(new_window, fg='blue', bg='white', width=30)
    Age.place(x=140, y=200)

    l_4 = tk.Label(new_window, text="Phone No. : ").place(x=70, y=250)
    global Num
    Num = tk.Entry(new_window, fg='blue', bg='white', width=30)
    Num.place(x=140, y=250)

    l_5 = tk.Label(new_window, text="Address : ").place(x=70, y=300)
    global Address
    Address = tk.Entry(new_window, fg='blue', bg='white', width=30)
    Address.place(x=140, y=300)

    l_6 = tk.Label(new_window, text="Adhar No. : ").place(x=70, y=350)
    global Adhar_card
    Adhar_card = tk.Entry(new_window, fg='blue', bg='white', width=30)
    Adhar_card.place(x=140, y=350)

    l_7 = tk.Label(new_window, text="Account type : ").place(x=70, y=400)
    global Acc_type
    Acc_type = tk.Entry(new_window, fg="blue", bg='white', width=30)
    Acc_type.insert(0, "current")
    Acc_type.configure(state='disabled')
    Acc_type.place(x=155, y=400)

    l_8 = tk.Label(new_window, text="Username : ").place(x=70, y=450)
    global username
    username = tk.Entry(new_window, fg='blue', bg='white', width=30)
    username.place(x=140, y=450)

    l_9 = tk.Label(new_window, text="Password : ").place(x=70, y=500)
    global password
    password = tk.Entry(new_window, fg='blue', bg='white', width=30)
    password.place(x=140, y=500)

    register = tk.Button(new_window, text="Register", bg="green", fg="white", command=register_in_json).place(x=190, y=540)

    def redirect_to_login() :
        new_window.destroy()
        Login()

    l_10 = tk.Label(new_window, text="Already a user? Login here : ", fg="blue").place(x=80, y=600)
    to_login = tk.Button(new_window, text="Login", bg="green", fg="white", command=redirect_to_login).place(x=230, y=600)

    new_window.mainloop()

def Register_dup(msg_1) :
    global new_window_1
    new_window_1 = tk.Tk()
    new_window_1.geometry("400x650")
    new_window_1.title("Banking System")

    head = tk.Label(new_window_1, text="\nRegistration Page\n", font=("Arial", 20)).pack()

    l_1 = tk.Label(new_window_1, text="First Name : ").place(x=70, y=100)
    global name_1_1
    name_1_1 = tk.Entry(new_window_1, fg='blue', bg='white', width=30)
    if first :
        name_1_1.insert(0, first)
    else :
        name_1_1.insert(0, "")
    name_1_1.place(x=140, y=100)

    l_2 = tk.Label(new_window_1, text="Last Name : ").place(x=70, y=150)
    global name_2_2
    name_2_2 = tk.Entry(new_window_1, fg='blue', bg='white', width=30)
    if last :
        name_2_2.insert(0, last)
    else :
        name_2_2.insert(0, "")
    name_2_2.place(x=140, y=150)

    l_3 = tk.Label(new_window_1, text="Age : ").place(x=70, y=200)
    global Age_1
    Age_1 = tk.Entry(new_window_1, fg='blue', bg='white', width=30)
    if age_1 :
        Age_1.insert(0, age_1)
    else :
        Age_1.insert(0, "")
    Age_1.place(x=140, y=200)

    l_4 = tk.Label(new_window_1, text="Phone No. : ").place(x=70, y=250)
    global Num_1
    Num_1 = tk.Entry(new_window_1, fg='blue', bg='white', width=30)
    if number :
        Num_1.insert(0, number)
    else :
        Num_1.insert(0, "")
    Num_1.place(x=140, y=250)

    l_5 = tk.Label(new_window_1, text="Address : ").place(x=70, y=300)
    global Address_1
    Address_1 = tk.Entry(new_window_1, fg='blue', bg='white', width=30)
    if add :
        Address_1.insert(0, add)
    else :
        Address_1.insert(0, "")
    Address_1.place(x=140, y=300)

    l_6 = tk.Label(new_window_1, text="Adhar No. : ").place(x=70, y=350)
    global Adhar_card_1
    Adhar_card_1 = tk.Entry(new_window_1, fg='blue', bg='white', width=30)
    if adhar :
        Adhar_card_1.insert(0, adhar)
    else :
        Adhar_card_1.insert(0, "")
    Adhar_card_1.place(x=140, y=350)

    l_7 = tk.Label(new_window_1, text="Account type : ").place(x=70, y=400)
    global Acc_type_1
    Acc_type_1 = tk.Entry(new_window_1, fg="blue", bg='white', width=30)
    if account :
        Acc_type_1.insert(0, account)
        Acc_type_1.configure(state='disabled')
    else :
        Acc_type_1.insert(0, "current")
        Acc_type.configure(state='disabled')
    Acc_type_1.place(x=155, y=400)

    l_8 = tk.Label(new_window_1, text="Username : ").place(x=70, y=450)
    global username_1
    username_1 = tk.Entry(new_window_1, fg='blue', bg='white', width=30)
    if u_name :
        username_1.insert(0, u_name)
    else :
        username_1.insert(0, "")
    username_1.place(x=140, y=450)

    l_9 = tk.Label(new_window_1, text="Password : ").place(x=70, y=500)
    global password_1
    password_1 = tk.Entry(new_window_1, fg='blue', bg='white', width=30)
    if u_pass :
        password_1.insert(0, u_pass)
    else :
        password_1.insert(0, "")
    password_1.place(x=140, y=500)

    register = tk.Button(new_window_1, text="Register", bg="green", fg="white", command=register_in_json).place(x=190, y=540)
    
    lab = tk.Label(text=msg_1, fg="red")
    lab.place(x=100, y=570)

    def redirect_to_login() :
        new_window_1.destroy()
        Login()

    l_10 = tk.Label(new_window_1, text="Already a user? Login here : ", fg="blue").place(x=80, y=600)
    to_login = tk.Button(new_window_1, text="Login", bg="green", fg="white", command=redirect_to_login).place(x=230, y=600)

    new_window_1.mainloop()
############################ END ###########################################

############################ MAIN SCREEN ###########################################
def main_screen() :
    main_window = tk.Tk()

    main_window.geometry("1010x800")

    main_window.title("Banking System")
    head = tk.Label(main_window, text="\nWelcome to my bank\n", font=("Arial", 25)).pack()

    def to_login() :
        main_window.destroy()
        Login()

    def to_register() :
        main_window.destroy()
        Register()
    
    f = "bank.jpg"
    load= Image.open(f)
    render = ImageTk.PhotoImage(load)
    img = tk.Label(main_window, image=render)
    img.pack()

    login_button = tk.Button(text="Login", bg="green", fg="white", height=2, width=10, command=to_login)
    login_button.place(x=300, y=690)

    empty = tk.Label(text=" ").pack()

    register_button = tk.Button(text="Register", bg="green", fg="white", height=2, width=10, command=to_register)
    register_button.place(x=600, y=690)

    main_window.mainloop()
############################ END ###########################################

############################ CALLING MAIN FUNCTION ###########################################
main_screen()
############################ END ###########################################