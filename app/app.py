from flask import Flask, render_template, request
import psycopg2
import json

app = Flask(__name__)

connection = psycopg2.connect(database='postgres', user='postgres', password='admin', host='localhost')
obj = connection.cursor()

# Home
@app.route("/")
def home() :
    return render_template("register.html")

#Redirect to login page
@app.route("/tologin")
def to_login() :
    return render_template("login.html")

#Logout
@app.route("/logout")
def logout() :
    return render_template("login.html", msg = "Logout Successfully")

#Register page working
@app.route("/register", methods = ['POST', 'GET'])
def register() :
    u_name = request.form['uname']
    user_name = u_name.lower()
    user_pass = request.form['upass']
    u_file = 'uname.json'
    d_file = 'details.json'
    with open(u_file, 'r') as user_file :
        user_list = json.load(user_file)
    with open(d_file, 'r') as n :
        user_dict = json.load(n)
    
    if user_name not in user_list :
        user_list.append(user_name)
        user_dict[user_name] = user_pass
        with open(u_file, 'w') as u :
            json.dump(user_list, u, indent=4)
        with open(d_file, 'w') as n1 :
            json.dump(user_dict, n1, indent=4)
        obj.execute(""" insert into app values ('{0}', '{1}') """.format(user_name, user_pass))
        connection.commit()
        return render_template("login.html")
    elif user_name in user_list :
        return render_template("register.html", msg = "Username Already taken...!")

#Login page working
@app.route("/login", methods = ['POST', 'GET'])
def login() :
    u_name = request.form['uname']
    user_name = u_name.lower()
    user_pass = request.form['upass']
    d_file = 'details.json'
    with open(d_file, 'r') as n :
        user_dict = json.load(n)
    user_list = list(user_dict.keys())
    pass_list = list(user_dict.values())
    count_name = -1
    count_pass = -2
    if user_pass in pass_list :
        count_pass = pass_list.index(user_pass)
    if user_name in user_list :
        count_name = user_list.index(user_name)
    if count_name != count_pass :
        return render_template("login.html", msg = "Incorrect username or password, please check again...!")
    elif count_name == count_pass :
        return render_template("user.html", msg = user_name, list = user_list)

#Navigate to Create room page
@app.route("/create")
def create() :
    return render_template("create_room.html")

#Create room page working
@app.route("/create_room", methods = ['POST', 'GET'])
def create_room() :
    room_name = request.form['create']
    room_file = "room.json"
    with open(room_file, 'r') as f :
        room_list = json.load(room_file)
    
