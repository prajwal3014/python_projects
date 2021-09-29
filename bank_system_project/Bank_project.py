"""
1. opening page
2. login page
3. registration page
4. authentication
"""
import time
import json
import os
from art import tprint
import tkinter as tk

def welcome():
    os.system('cls')
    tprint("WELCOME TO THE \nBANKING SYSTEM")   
    while True:
        a=input("***What you want to do***\n1. Login\n2. Registration\nEnter your choice :")
        if(a=='1'or a=='2'):
            try:
                a=int(a)
                break
            except:
                os.system('cls')
        else:
            os.system('cls')
        print("***Please enter right input according to the given options***\n")
    if(a==1):
        os.system('cls')
        tprint("LOGIN")
        login_json()
    elif(a==2):
        os.system('cls')
        tprint("REGISTER")
        register_in_json()

def register_data() :
    while True:
        FName=input("Enter your First name :")
        if FName.isalpha()==True :
            break
        else:
            print("Plese enter accepetable name...!\nRefreshing")
            time.sleep(2)
            os.system('cls')
    while True:
        LName=input("Enter your Last name :")
        if LName.isalpha()==True :
            break
        else:
            print("Plese enter accepetable name...!\nRefreshing")
            time.sleep(2)
            os.system('cls')
            print("First name : {}".format(FName))
    name=FName+" "+LName
    while True :
        try :
            while True :
                age = input("Enter age : ")
                age = int(age)
                if age <= 17 :
                    print("Age must be greater than or equal to 18...!\nRefreshing...")
                    time.sleep(2)
                    os.system('cls')
                    print("Name : {}".format(name))
                elif age >= 18 :
                    break
            break
        except :
            print("Wrong input...!\nRefreshing...")
            time.sleep(2)
            os.system('cls')
            print("Name : {}".format(name))
    
    while True :
        try :
            while True :
                num = input("Enter number : ")
                if len(num) != 10 :
                    print("Phone number must be of 10-digits only...!\nRefreshing...")
                    os.time.sleep(2)
                    os.system('cls')
                    print("Name : {}".format(name))
                    print("Age : {}".format(age))
                elif len(num) == 10 :
                    num=int(num)
                    break
            break
        except :
            print("Wrong input...!\nRefreshing...")
            time.sleep(2)
            os.system('cls')
            print("Name : {}".format(name))
            print("Age : {}".format(age))
    
    address = input("Enter address : ")
    
    while True :
        try :
            while True :
                adhar_card = input("Enter adhar card no. : ")
                if len(adhar_card) != 12 :
                    print("Adhar number must be of 12-digits only...!\nRefreshing...")
                    time.sleep(2)
                    os.system('cls')
                    print("Name : {}".format(name))
                    print("Age : {}".format(age))
                    print("Number : {}".format(num))
                    print("Address : {}".format(address))
                elif len(adhar_card) == 12 :
                    adhar_card = int(adhar_card)
                    break
            break
        except :
            print("Wrong input...!\nRefreshing...")
            time.sleep(2)
            os.system('cls')
            print("Name : {}".format(name))
            print("Age : {}".format(age))
            print("Number : {}".format(num))
            print("Address : {}".format(address))
    return name, age, num, address, adhar_card

def create_user() :
    user_name = input("Create username : ")
    while True :
        print("*** Password must contain (# or @ or &) ***")
        user_password = input("Create password : ")
        if '#' in user_password or '@' in user_password or '&' in user_password :
            break
        else :
            print("Password must contain # or @ or &...!\nRefreshing...")
            time.sleep(2)
            os.system('cls')
            print("Username : {}".format(user_name))
    return user_name, user_password

def register_in_json() :
    name, age, num, address, adhar_card = register_data()
    os.system('cls')
    user_name, user_password = create_user() 
    file = "user_details.json"
    file_2 = "id.txt"
    if os.path.exists(file) :
        unique = open(file_2, 'r')
        id = unique.read()
        user_dict = {
            id : {
                "name" : name,
                "age" : age,
                "number" : num,
                "address" : address,
                "adhar_number" : adhar_card,
                "Username" : user_name,
                "password" : user_password
            }
        }
        with open(file, 'r') as r :
            data = json.load(r)
        data.update(user_dict)
        with open(file, 'w') as w :
            json.dump(data, w, indent=4)
        id = int(id)
        id = id+1
        unique = open(file_2, 'w')
        unique.write(str(id))
    else :
        user_dict = {
            "1" : {
                "name" : name,
                "age" : age,
                "number" : num,
                "address" : address,
                "adhar_number" : adhar_card,
                "Username" : user_name,
                "password" : user_password
            }
        }
        with open(file, 'w') as w :
            json.dump(user_dict, w, indent=4)
        unique = open(file_2, 'w')
        unique.write("2")
    
    file_3 = "password.json"
    if os.path.exists(file_3) :
        with open(file_3, 'r') as r :
            user_dict = json.load(r)
        user_list = list(user_dict.keys())
        while True :
            if user_name not in user_list :
                user_dict[user_name] = user_password
                with open(file_3, 'w') as w :
                    json.dump(user_dict, w, indent=4)
                print("Data updated...!")
                break
            elif user_name in user_list :
                print("Username already exists...!\nRefreshing...")
                time.sleep(2)
                os.system('cls')
                user_name, user_password = create_user()
    else :
        user_dict = {user_name : user_password}
        with open(file_3, 'w') as w :
            json.dump(user_dict, w, indent=4)
        print("Function successfull...!")

def login_data() :
    user_name = username.get()
    user_password = password.get()
    return user_name, user_password

def login_json() :
    file = "password.json"
    with open(file, 'r') as r :
        user_dict = json.load(r)
    user_list = list(user_dict.keys())
    user_name, user_password = login_data()
    while True :
        if user_name in user_list :
            if user_password == user_dict[user_name] :
                print("Login successful...!")
                break
            elif user_password != user_dict[user_name] :
                print("Invalid Password...!")
                break
        elif user_name not in user_list :
            print("Username does not exists...!")
            break

#GUI from here
# def register_gui() :
#     head = tk.Label(new_window, text="\nRegistration Page\n", font=("Arial", 20)).pack()

#     l_1 = tk.Label(new_window, text="First Name : ").place(x=70, y=100)
#     FName = tk.Entry(new_window, fg='blue', bg='white', width=30)
#     FName.place(x=140, y=100)

#     l_2 = tk.Label(new_window, text="Last Name : ").place(x=70, y=150)
#     LName = tk.Entry(new_window, fg='blue', bg='white', width=30)
#     LName.place(x=140, y=150)

#     l_3 = tk.Label(new_window, text="Age : ").place(x=70, y=200)
#     age = tk.Entry(new_window, fg='blue', bg='white', width=30)
#     age.place(x=140, y=200)

#     l_4 = tk.Label(new_window, text="Phone No. : ").place(x=70, y=250)
#     num = tk.Entry(new_window, fg='blue', bg='white', width=30)
#     num.place(x=140, y=250)

#     l_5 = tk.Label(new_window, text="Address : ").place(x=70, y=300)
#     address = tk.Entry(new_window, fg='blue', bg='white', width=30)
#     address.place(x=140, y=300)

#     l_6 = tk.Label(new_window, text="Adhar No. : ").place(x=70, y=350)
#     adhar_card = tk.Entry(new_window, fg='blue', bg='white', width=30)
#     adhar_card.place(x=140, y=350)

#     register = tk.Button(new_window, text="Register", bg="green", fg="white", command=register_data).place(x=190, y=390)

#     # l_7 = tk.Label(new_window, text="Already a user? Login here : ", fg="blue").place(x=80, y=500)
#     # to_login = tk.Button(new_window, text="Login", bg="green", fg="white", command=login_gui).place(x=230, y=500)

#     new_window.mainloop()

window = tk.Tk()
window.geometry("400x350")
window.title("Banking System")

# new_window = tk.Toplevel(window)
# new_window.geometry("400x550")
# new_window.title("Banking System")

#login
head = tk.Label(window, text="\nLogin Page\n", font=("Arial", 20)).pack()

l_1 = tk.Label(window, text="Username : ").place(x=70, y=100)
username = tk.Entry(window, fg='blue', bg='white', width=30)
username.place(x=140, y=100)

l_2 = tk.Label(window, text="Password : ").place(x=70, y=150)
password = tk.Entry(window, fg='blue', bg='white', width=30, show="*")
password.place(x=140, y=150)

login = tk.Button(window, text="Login", bg="green", fg="white", command=login_json).place(x=190, y=190)

l_3 = tk.Label(window, text="Not a user? Register here : ", fg="blue").place(x=80, y=300)
to_register = tk.Button(window, text="Register", bg="green", fg="white").place(x=225, y=300)

window.mainloop()
