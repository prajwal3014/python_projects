import tkinter as tk
from tkinter import messagebox
from tkinter.font import BOLD
from connection_db import *
from PIL import Image, ImageTk
from datetime import datetime

################################### Admin Account ################################################
def admin_acc() :
    admin_window = tk.Tk()
    admin_window.geometry("600x600")
    admin_window.title("Fruits Shop")

    lst = get_profit()

    def log_out() :
        admin_window.destroy()
        Login()

    logout = tk.Button(text="Log Out", fg="white", bg="green", width=15, command=log_out).place(x = 450, y = 50)

    head = tk.Label(text="\nRecords\n", font=("arial", 18, BOLD)).pack()

    for data in lst :
        user_name, date_time, profit, profit_per = data
        lab = tk.Label(text="Dated : " + date_time, font=("arial", 15)).pack()
        lab = tk.Label(text="User : " + user_name, font=("arial", 15)).pack()
        lab = tk.Label(text="Profit : Rs. " + profit, font=("arial", 15)).pack()
        lab = tk.Label(text="Profit percentage : " + profit_per + "%", font=("arial", 15)).pack()
    
    admin_window.mainloop()
################################### END ################################################

################################### Wallet ################################################
def wallet(user_name) :
    wall_window = tk.Tk()
    wall_window.geometry("400x400")
    wall_window.title("Fruits Shop")

    wallet_money = get_money(user_name)

    head = tk.Label(text="\nWallet\n", font=("arial", 18, BOLD)).pack()

    bal = tk.Label(text="Balance : " + str(wallet_money) + "\n", font=("arial", 12), fg="blue").pack()

    lab = tk.Label(text="Enter amount : \n", font=("arial", 12)).pack()

    depo_money = tk.Entry(wall_window, fg="blue", bg="white", width=30)
    depo_money.pack()

    lab = tk.Label(text=" ").pack()

    def update_wall() :
        x = depo_money.get()
        try :
            x = int(x)
            if x <= 10000 and x >= 1:
                money = wallet_money + x
                update_money(user_name, money)
                wall_window.destroy()
                wallet(user_name)
            else :
                messagebox.showwarning("showwarning", "Limit is between 1 to 10,000...!")
        except :
            messagebox.showwarning("showwarning", "Amount must be numeric...!")
    
    depo = tk.Button(text="Deposit", fg="white", bg="green", width=15, command=update_wall).pack()

    def to_back() :
        wall_window.destroy()
        shop(user_name)
    lab = tk.Label(text=" ").pack()
    back = tk.Button(text="Back", fg="white", bg="green", width=15, command=to_back).pack()

    wall_window.mainloop()
################################### END ################################################

################################### Shopping ################################################
def shop(user_name) :
    man, ban, app, gua, ora, dra = show_quantity()
    shop_window = tk.Tk()
    shop_window.geometry("1000x700")
    shop_window.title("Fruits Shop")

    head = tk.Label(text="\nShopping", font=("arial", 18, BOLD)).pack()
    wallet_money = get_money(user_name)
    bal = tk.Label(text="Balance : " + str(wallet_money) + "\n", font=("arial", 12), fg="blue").pack()

    lab = tk.Label(text="Price per unit : Rs.10").place(x=20, y=90)
    f_1 = "mango.jpg"
    load_1 = Image.open(f_1)
    render_1 = ImageTk.PhotoImage(load_1)
    img_1 = tk.Label(shop_window, image=render_1)
    img_1.place(x=20, y=110)

    lab = tk.Label(text="Quantity : " + str(man), font=("arial", 12)).place(x=20, y=270)
    m = tk.Entry(shop_window, fg="blue", bg="white")
    m.insert(0, "0")
    m.place(x=20, y=300)

    lab = tk.Label(text="Price per unit : Rs.5").place(x=400, y=90)
    f_2 = "banana.jpg"
    load_2 = Image.open(f_2)
    render_2 = ImageTk.PhotoImage(load_2)
    img_2 = tk.Label(shop_window, image=render_2)
    img_2.place(x=400, y=110)

    lab = tk.Label(text="Quantity : " + str(ban), font=("arial", 12)).place(x=400, y=270)
    b = tk.Entry(shop_window, fg="blue", bg="white")
    b.insert(0, "0")
    b.place(x=400, y=300)

    lab = tk.Label(text="Price per unit : Rs.15").place(x=800, y=90)
    f_3 = "apple.jpg"
    load_3 = Image.open(f_3)
    render_3 = ImageTk.PhotoImage(load_3)
    img_3 = tk.Label(shop_window, image=render_3)
    img_3.place(x=800, y=110)

    lab = tk.Label(text="Quantity : " + str(app), font=("arial", 12)).place(x=800, y=270)
    a = tk.Entry(shop_window, fg="blue", bg="white")
    a.insert(0, "0")
    a.place(x=800, y=300)

    lab = tk.Label(text="Price per unit : Rs.5").place(x=20, y=360)
    f_4 = "guava.jpg"
    load_4 = Image.open(f_4)
    render_4 = ImageTk.PhotoImage(load_4)
    img_4 = tk.Label(shop_window, image=render_4)
    img_4.place(x=20, y=380)

    lab = tk.Label(text="Quantity : " + str(gua), font=("arial", 12)).place(x=20, y=540)
    g = tk.Entry(shop_window, fg="blue", bg="white")
    g.insert(0, "0")
    g.place(x=20, y=570)

    lab = tk.Label(text="Price per unit : Rs.5").place(x=400, y=360)
    f_5 = "orange.jpg"
    load_5 = Image.open(f_5)
    render_5 = ImageTk.PhotoImage(load_5)
    img_5 = tk.Label(shop_window, image=render_5)
    img_5.place(x=400, y=380)

    lab = tk.Label(text="Quantity : " + str(ora), font=("arial", 12)).place(x=400, y=540)
    o = tk.Entry(shop_window, fg="blue", bg="white")
    o.insert(0, "0")
    o.place(x=400, y=570)

    lab = tk.Label(text="Price per unit : Rs.30").place(x=800, y=360)
    f_6 = "dr_fruit.jpg"
    load_6 = Image.open(f_6)
    render_6 = ImageTk.PhotoImage(load_6)
    img_6 = tk.Label(shop_window, image=render_6)
    img_6.place(x=800, y=380)

    lab = tk.Label(text="Quantity : " + str(dra), font=("arial", 12)).place(x=800, y=540)
    d = tk.Entry(shop_window, fg="blue", bg="white")
    d.insert(0, "0")
    d.place(x=800, y=570)

    def buy_fun() :
        man_value = m.get()
        ban_value = b.get()
        app_value = a.get()
        gua_value = g.get()
        ora_value = o.get()
        dra_value = d.get()
        try : 
            man_value = int(man_value)
            ban_value = int(ban_value)
            app_value = int(app_value)
            gua_value = int(gua_value)
            ora_value = int(ora_value)
            dra_value = int(dra_value)
            add = man_value + ban_value + app_value + gua_value + ora_value + dra_value
            now=datetime.now()
            key=now.strftime("%d/%m/%Y at %H:%M:%S")
            print(man_value, ban_value, app_value, gua_value, ora_value, dra_value)
            if man_value>50 or ban_value>50 or app_value>50 or gua_value>50 or ora_value>50 or dra_value>50 :
                messagebox.showwarning("showwarning", "Quantity must be between 0 to 50...!")
            else :
                profit = man_value*2 + ban_value + app_value*3 + gua_value + ora_value + dra_value*5
                total_cost = man_value*8 + ban_value*4 + app_value*12 + gua_value*4 + ora_value*4 + dra_value*25
                profit_per = (profit/total_cost)*100
                selling_cost = profit + total_cost
                if selling_cost > wallet_money :
                    messagebox.showwarning("showwarning", "Less money in wallet...!")
                else :
                    update_m = wallet_money - selling_cost
                    update_money(user_name, update_m)
                    update_quantity(man_value, ban_value, app_value, gua_value, ora_value, dra_value)
                    save_user_data(user_name, add, key, profit, profit_per)
                    shop_window.destroy()
                    shop(user_name)
        except :
            messagebox.showwarning("showwarning", "Quantity must be integers...!")
    buy = tk.Button(text="BUY", fg="white", bg="green", width=20, command=buy_fun).place(x=400, y=620)

    def to_wallet() :
        shop_window.destroy()
        wallet(user_name)

    wall = tk.Button(text="Wallet", fg="white", bg="green", width=15, command=to_wallet).place(x=50, y=620)

    def log_out() :
        shop_window.destroy()
        Login()

    logout = tk.Button(text="Log Out", fg="white", bg="green", width=20, command=log_out).place(x = 400, y = 670)

    shop_window.mainloop()
################################### END ################################################

################################### Login ################################################
def Login() :
    login_window = tk.Tk()
    login_window.geometry("400x350")
    login_window.title("Fruits shop")

    head = tk.Label(text="\nLogin Page", font=("arial", 18, BOLD)).pack()

    l_1 = tk.Label(text="Username : ").place(x=70, y=100)
    username_login = tk.Entry(fg='blue', bg='white', width=30)
    username_login.place(x=140, y=100)

    l_2 = tk.Label(text="Password : ").place(x=70, y=150)
    password_login = tk.Entry(fg='blue', bg='white', width=30, show="*")
    password_login.place(x=140, y=150)

    def send_to_db() :
        user_name = username_login.get()
        user_pass = password_login.get()
        user_list = check_username()
        
        if user_name == "admin" and user_pass == "#admin" :
            login_window.destroy()
            admin_acc()
        elif user_name == "admin" and user_pass != "#admin" :
            messagebox.showwarning("showwarning", "Invalid Password...!")
        elif user_name in user_list :
            if check_password(user_name, user_pass).upper() == "TRUE" :
                login_window.destroy()
                shop(user_name)
            else :
                messagebox.showwarning("showwarning", "Invalid Password...!")
        elif user_name not in user_list :
            messagebox.showwarning("showwarning", "Username does not exists...!")

    login = tk.Button(text="Login", bg="green", fg="white", command=send_to_db).place(x=190, y=190)
    
    def redirect_to_register() :
        login_window.destroy()
        Register()

    l_3 = tk.Label(text="Not a user? Register here : ", fg="blue").place(x=80, y=300)
    to_register = tk.Button(text="Register", bg="green", fg="white", command=redirect_to_register).place(x=225, y=300)

    login_window.mainloop()
################################### END ################################################

################################### Register ################################################
def Register() :
    reg_window = tk.Tk()
    reg_window.geometry("400x350")
    reg_window.title("Fruits shop")

    head = tk.Label(reg_window, text="\nRegistration Page\n", font=("Arial", 20)).pack()

    l_1 = tk.Label(reg_window, text="Create Username : ").place(x=70, y=100)
    username = tk.Entry(reg_window, fg='blue', bg='white', width=30)
    username.place(x=180, y=100)

    l_2 = tk.Label(reg_window, text="Create Password : ").place(x=70, y=150)
    password = tk.Entry(reg_window, fg='blue', bg='white', width=30)
    password.place(x=180, y=150)

    def send_to_db() :
        user_name = username.get()
        user_pass = password.get()
        user_list = check_username()
        if '#' in user_pass or '@' in user_pass or '&' in user_pass :
            if (user_name not in user_list) and (user_name != "admin") :
                save_user(user_name, user_pass, 0)
                reg_window.destroy()
                Login()
            elif user_name in user_list :
                messagebox.showwarning("showwarning", "Username already exists...!")
        else :
            messagebox.showwarning("showwarning", "Password must contain # or @ or &...!")

    register = tk.Button(reg_window, text="Register", bg="green", fg="white", command=send_to_db).place(x=190, y=190)

    def redirect_to_login() :
        reg_window.destroy()
        Login()

    l_10 = tk.Label(reg_window, text="Already a user? Login here : ", fg="blue").place(x=80, y=300)
    to_login = tk.Button(reg_window, text="Login", bg="green", fg="white", command=redirect_to_login).place(x=225, y=300)

    reg_window.mainloop()
################################### END ################################################

################################### Main Window ################################################
def main_screen() :
    main_window = tk.Tk()
    main_window.geometry("800x800")
    main_window.title("Fruits shop")

    head = tk.Label(text="Fruits Shop", font=("arial", 18, BOLD)).pack()

    f = "fruit.jpg"
    load= Image.open(f)
    render = ImageTk.PhotoImage(load)
    img = tk.Label(main_window, image=render)
    img.pack()

    def to_login() :
        main_window.destroy()
        Login()

    login = tk.Button(text="Login", fg="white", bg="green", width=15, command=to_login).place(x=250, y=650)
    
    def to_register() :
        main_window.destroy()
        Register()

    register = tk.Button(text="Register", fg="white", bg="green", width=15, command=to_register).place(x=450, y=650)

    main_window.mainloop()
################################### END ################################################

main_screen()