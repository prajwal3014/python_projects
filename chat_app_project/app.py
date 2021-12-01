from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO, join_room, leave_room
from flask_login import LoginManager, login_user, login_required, logout_user
import json
import db_connect as db

app = Flask(__name__)
app.secret_key = "prajwal sharma"
socketio = SocketIO(app,cors_allowed_origins="*")
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

@app.route('/')
def home():
    return render_template("signup.html")

#Redirect to login page
@app.route("/tologin")
def to_login() :
    return render_template("login.html")

@app.route('/login', methods = ['GET', 'POST'])
def login() :
    message = ''
    if request.method == 'POST' :
        username = request.form.get('username')
        password_input = request.form.get('password')
        file = 'username.json'
        with open(file, 'r') as r :
            username_list = json.load(r)
        if username not in username_list :
            message = "Invalid username or password, please try again...!"
        elif username in username_list :
            user = db.get_user(username)
            if user and user.check_password(password_input) :
                login_user(user)
                return render_template('index.html')
            else :
                message = "Invalid username or password, please try again...!"
    return render_template('login.html', msg = message)

@app.route('/signup', methods = ['GET', 'POST'])
def signup() :
    if request.method == 'POST' :
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        file = 'username.json'
        with open(file, 'r') as r :
            username_list = json.load(r)
        
        if username not in username_list :
            username_list.append(username)
            with open(file, 'w') as w :
                json.dump(username_list, w, indent=4)
            db.save_user(username, password, email)
            return render_template('login.html', msg = "Account created successfully...!")
        elif username in username_list : 
            return render_template('signup.html', msg = "Username already exists...!")

@app.route('/logout')
@login_required
def logout() :
    logout_user()
    return render_template('login.html', msg = "Logout successfully...!")

@app.route('/chat')
@login_required
def chat():
    username = request.args.get('username')
    room = request.args.get('room')

    if username and room:
        msg_data = db.get_message(room)
        if msg_data :
            return render_template('chat.html', username=username, room=room, messages = msg_data)
        else :
            return render_template('chat.html', username=username, room=room, no_msg = "Be the first to start chat...")
    else:
        return redirect(url_for('to_login'))

@app.route('/leave')
def leave() :
    return render_template('index.html', msg = "Successfully exited from recent chat room...!")

@socketio.on('send_message')
def handle_send_message_event(data):
    app.logger.info("{} has sent message to the room {}: {}".format(data['username'],data['room'],data['message']))
    db.save_message(data['room'], data['message'], data['username'])
    socketio.emit('receive_message', data, room=data['room'])

@socketio.on('join_room')
def handle_join_room_event(data):
    app.logger.info("{} has joined the room {}".format(data['username'], data['room']))
    join_room(data['room'])
    socketio.emit('join_room_announcement', data, room=data['room'])


@socketio.on('leave_room')
def handle_leave_room_event(data):
    app.logger.info("{} has left the room {}".format(data['username'], data['room']))
    leave_room(data['room'])
    socketio.emit('leave_room_announcement', data, room=data['room'])

@login_manager.user_loader
def load_user(username) :
    return db.get_user(username)

if __name__ == '__main__':
    socketio.run(app, debug=True)