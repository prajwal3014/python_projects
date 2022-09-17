from pickle import TRUE
from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, login_user, login_required, logout_user

app = Flask(__name__)
app.secret_key = "THIS IS A NBYULA PROJECT"

@app.route('/')
def sign_in() :
    return render_template('login.html')

@app.route('/sign-up')
def sign_up() :
    return render_template('register.html')

@app.route('/home')
def home() :
    return render_template('home.html')

@app.route('/book')
def book() :
    return render_template('book_appointments.html')

@app.route('/change_password')
def change_password() :
    return render_template('change_password.html')

if __name__ == "__main__" :
    app.run(debug=TRUE)