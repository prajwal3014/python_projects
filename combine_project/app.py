from flask import Flask, request, render_template, redirect, url_for
from Calculator_GUI_project.gui_calculator import calculator
from Youtube_video_downloader.youtube_downloader import window_main
from Email_sender.email_sender import main
from own_database import get_users, save_user, get_name

app = Flask(__name__)
app.secret_key = 'COMBINING ALL PROJECTS'

@app.route('/')
def index() :
    return render_template('index.html')

@app.route('/Calculator')
def to_calculator() :
    calculator()
    return redirect(url_for('index'))

@app.route('/Youtube')
def to_youtube() :
    window_main()
    return redirect(url_for('index'))

@app.route('/Email')
def to_email() :
    main()
    return redirect(url_for('index'))

@app.route('/register_for_database')
def to_register() :
    return render_template('register_for_database.html')

@app.route('/register', methods = ['GET', 'POST'])
def registration() :
    name = request.form.get('fullname')
    user_name = request.form.get('username')
    tables_dict, check_user_dict, users_list = get_users()
    if user_name not in users_list :
        id = len(users_list) + 1
        uid = "UV-" + user_name + "@00" + str(id)
        save_user(name, user_name, uid, "")
        return render_template('create_view_database.html', name = name, uid = uid, msg = "No data found...!")
    elif user_name in users_list :
        return render_template('register_for_database.html', msg = "Username already exists...!")

@app.route('/login_for_database')
def to_login() :
    return render_template('login_for_database.html')

@app.route('/login', methods = ['GET', 'POST'])
def login() :
    user_name = request.form.get('username')
    uid = request.form.get('uid')
    tables_dict, check_user_dict, users_list = get_users()
    if user_name in users_list :
        uid_2 = check_user_dict[user_name]
        if uid == uid_2 :
            y = tables_dict[user_name]
            if len(y) > 0 :
                i = y.pop()
                tables_list = list(map(str, i.split(", ")))
                return render_template('create_view_database.html', name = get_name(uid), uid = uid, tables = tables_list, msg = "No data found...!")
        elif uid != uid_2 :
            return render_template('login_for_database.html', msg = "Invalid Username or UNIQUEVERSE ID...!")
    elif user_name not in users_list :
        return render_template('login_for_database.html', msg = "Username does not exists...!")

if __name__ == "__main__" :
    app.run(debug=True)