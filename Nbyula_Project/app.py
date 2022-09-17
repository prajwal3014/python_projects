from pickle import TRUE
from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, login_user, login_required, logout_user

app = Flask(__name__)
app.secret_key = "THIS IS A NBYULA PROJECT"

@app.route('/')
def home() :
    return render_template('login.html')

@app.route('/sign-up')
def sign_in() :
    return render_template('register.html')

if __name__ == "__main__" :
    app.run(debug=TRUE)