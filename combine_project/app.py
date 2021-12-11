from flask import Flask, request, render_template, redirect
from flask.helpers import url_for
from Calculator_GUI_project.gui_calculator import calculator

app = Flask(__name__)
app.secret_key = 'COMBINING ALL PROJECTS'

@app.route('/')
def index() :
    return render_template('index.html')

@app.route('/Calculator')
def to_calculator() :
    calculator()
    return redirect(url_for('index'))

if __name__ == "__main__" :
    app.run(debug=True)