from flask import Flask, render_template, request, redirect, url_for
from flask.helpers import url_for
from pyttsx3 import speak
import Jerry

app = Flask(__name__)

#Home
@app.route('/')
def home() :
    return render_template("home.html")

@app.route('/toMain', methods = ['POST'])
def to_main() :
    command = request.form['data']
    Jerry.Speak(command)
    return redirect(url_for('home'))


if __name__ == '__main__' :
    app.run(debug=True)