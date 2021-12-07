from flask import Flask, render_template, request
import db
import json

app = Flask(__name__)

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

#To Change password page
@app.route('/tochange')
def to_change_password() :
    return render_template("change_pass.html")

#Register page working
@app.route("/register", methods = ['POST', 'GET'])
def register() :
    name = request.form['name']
    email = request.form['email']
    number = request.form['number']
    username = request.form['username']
    password = request.form['password']

    file = 'uname.json'
    with open(file, 'r') as r :
        user_list = json.load(r)
    
    if username not in user_list :
        user_list.append(username)
        with open(file, 'w') as w :
            json.dump(user_list, w, indent=4)
        db.save_user(name, email, number, username, password)
        return render_template("login.html", msg = "Account created successfully...!")
    elif username in user_list :
        return render_template("register.html", msg = "Username Already taken...!")

#Login page working
@app.route("/login", methods = ['POST', 'GET'])
def login() :
    username = request.form['username']
    password = request.form['password']
    
    file = 'uname.json'
    with open(file, 'r') as r :
        user_list = json.load(r)
    
    if username not in user_list :
        return render_template("login.html", msg = "Username does not exists...!")
    elif username in user_list :
        authentication = db.check_password(username, password)
        if authentication == "True" :
            user_data = db.get_user(username)
            return render_template("user.html", user_data = user_data, username = username)
        elif authentication == "False" :
            return render_template("login.html", msg = "Invalid Username or Password, Please try again...!")

if __name__ == '__main__' :
    app.run(debug=True) 