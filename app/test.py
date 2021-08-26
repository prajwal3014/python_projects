from flask import Flask, render_template, request
from flask_socketio import SocketIO,join_room
import psycopg2
import json

from werkzeug import debug

app = Flask(__name__)
socketio = SocketIO(app)

connection = psycopg2.connect(database='postgres', user='postgres', password='admin', host='localhost')
obj = connection.cursor()

lst = []

# Home
@app.route("/")
def home() :
    return render_template("register.html")

#Redirect to login page
@app.route("/tologin")
def to_login() :
    return render_template("login.html")

#Logout
@app.route("/logout", methods = ['POST', 'GET'])
def logout() :
    return render_template("login.html", msg = "Logout Successfully...!")

#Navigate to Create room page
@app.route("/create", methods = ['POST', 'GET'])
def create() :
    return render_template("create_room.html")

#Navigate to Join room page
@app.route("/join", methods = ['POST', 'GET'])
def join() :
    return render_template("join_room.html")

#Leave Chat
@app.route("/leave", methods = ['POST', 'GET'])
def leave() :
    return render_template("user.html", msg = "Exited from the recent chat room...!")

#Register page working
@app.route("/register", methods = ['POST', 'GET'])
def register() :
    u_name = request.form['username']
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
    u_name = request.form['username']
    user_name = u_name.lower()
    user_pass = request.form['upass']
    lst.append(user_name)
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
        return render_template("user.html")

#Create room page working
@app.route("/create_room", methods = ['POST', 'GET'])
def create_room() :
    room_name = request.form['room']
    room_file = "room.json"
    user_name = lst.pop()
    lst.append(user_name)
    with open(room_file, 'r') as f :
        room_list = json.load(f)
    if room_name in room_list :
        return render_template("create_room.html", msg = "Room already exists...!")
    elif room_name not in room_list :
        room_list.append(room_name)
        with open(room_file, 'w') as c :
            json.dump(room_list, c, indent=4)
        return render_template("chat.html", user = user_name, room = room_name)

#Join room working
@app.route("/join_room", methods = ['POST', 'GET'])
def join_room() :
    room_name = request.form['room']
    user_name = lst.pop()
    lst.append(user_name)
    room_file = "room.json"
    with open(room_file, 'r') as f :
        room_list = json.load(f)
    if room_name in room_list :
        return render_template("chat.html", user = user_name, room = room_name)
    elif room_name not in room_list :
        return render_template("join_room.html", msg = "Room does not exists...!")

@socketio.on('join_room')
def join_room_event(data) :
	join_room(data['room'])
	socketio.emit('join_announce', data)

if __name__ == '__main__' :
    socketio.run(app, debug=True)