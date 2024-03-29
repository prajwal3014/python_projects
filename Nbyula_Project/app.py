from flask import Flask, render_template, request, redirect, url_for
from db import check_email, check_empid, login_user, register_user, get_name

app = Flask(__name__)
app.secret_key = "THIS IS A NBYULA PROJECT"

@app.route('/')
def sign_in() :
    return render_template('login.html')

@app.route('/sign-up')
def sign_up() :
    return render_template('register.html')

@app.route('/login', methods = ['POST', 'GET'])
def register() :
    name = request.form.get('name')
    emp_id = request.form.get('emp_id')
    email = request.form.get('email')
    create_pass = request.form.get('create_pass')
    confirm_pass = request.form.get('confirm_pass')
    if check_empid(emp_id) :
        return render_template('register.html', name = name, emp_id = emp_id, email = email, create_pass = create_pass, confirm_pass = confirm_pass, msg = "Employee Id already Exists!!!")
    if check_email(email) :
        return render_template('register.html', name = name, emp_id = emp_id, email = email, create_pass = create_pass, confirm_pass = confirm_pass, msg = "Email Id already Exists!!!")
    if create_pass != confirm_pass :
        return render_template('register.html', name = name, emp_id = emp_id, email = email, create_pass = create_pass, confirm_pass = confirm_pass, msg = "Password is not matching!!!")
    
    register_user(name, emp_id, email, confirm_pass)
    
    return redirect(url_for('sign_in'))

@app.route('/home', methods = ['POST', 'GET'])
def home() :
    emp_id = request.form.get('emp_id')
    password = request.form.get('password')
    if check_empid(emp_id) :
        name = get_name(emp_id)
        if login_user(emp_id, password) :
            return render_template('home.html', name = name)
        else :
            return render_template('login.html', emp_id = emp_id, password = password, msg = "Wrong Password!!!")
    else :
        return render_template('login.html', emp_id = emp_id, password = password, msg = "Employee Doesnot Exists!!!")

@app.route('/booked/home', methods = ['POST', 'GET'])
def book() :
    guest_name = request.form.get('guest_name')
    title = request.form.get('title')
    agenda = request.form.get('agenda')
    start_time = request.form.get('start_time')
    end_time = request.form.get('end_time')
    return render_template('book_appointments.html')

@app.route('/change_password')
def change_password() :
    return render_template('change_password.html')

@app.route('/hours')
def hours() :
    return render_template('hours.html')

if __name__ == "__main__" :
    app.run(debug=True)