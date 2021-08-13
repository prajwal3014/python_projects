from flask import Flask, render_template, request
# , redirect, url_for, flash, abort, session, jsonify
from MainDBConnect import DataAccessor
import pandas as pd
import json
# from werkzeug.utils import secure_filename

obj = DataAccessor(hostname='localhost', database_name='postgres', username='postgres', password='admin')

app = Flask(__name__)
app.secret_key = 'hdashdgaganhwethit9w2532627'

lst=[]

# HOME
@app.route("/")
def home() :
    return render_template("home.html")

# Submit_Uname
@app.route("/submit_Uname", methods=['POST', 'GET'])
def user_name_func() :
        
    u_name=request.form['user']
    user_name = u_name.upper()
    lst.append(user_name)
    if request.method == 'POST' :
        with open('Uname.json', "r") as username_file :
            user_list = json.load(username_file)
            
        if user_name not in user_list :
            user_list.append(user_name)
            with open('Uname.json', "w") as f :
                json.dump(user_list, f, indent=4)
            obj.execute(""" insert into car values ('{0}') """.format(user_name))
            return render_template("SEAT.html", member=user_name)
        elif user_name in user_list :
            car_data = obj.execute(""" select * from car where username='{0}' """.format(user_name))
            return render_template("old_member.html", member=user_name, data=car_data)

#Go_home
@app.route("/Go_home", methods=['POST', 'GET'])
def go_home() :
    return render_template("home.html")

# SEAT
@app.route("/SEAT", methods=['POST', 'GET'])
def new_seat() :
    x=request.form['Seat']
    user_name = lst.pop()
    lst.append(user_name)
    obj.execute(""" update car 
                    set seat='{0}' where username='{1}' """.format(x, user_name))
    return render_template("TYRE.html", member=user_name)

# TYRE
@app.route("/TYRE", methods=['POST', 'GET'])
def new_tyre() :
    x=request.form['Tyre']
    user_name = lst.pop()
    lst.append(user_name)
    obj.execute(""" update car 
                    set tyre='{0}' where username='{1}' """.format(x, user_name))
    return render_template("BODY.html", member=user_name)

# BODY
@app.route("/BODY", methods=['POST', 'GET'])
def new_body() :
    x=request.form['Body']
    user_name = lst.pop()
    lst.append(user_name)
    obj.execute(""" update car 
                    set body='{0}' where username='{1}' """.format(x, user_name))
    return render_template("GEAR.html", member=user_name)

# GEAR
@app.route("/GEAR", methods=['POST', 'GET'])
def new_gear() :
    x=request.form['Gear']
    user_name = lst.pop()
    lst.append(user_name)
    obj.execute(""" update car 
                    set gear='{0}' where username='{1}' """.format(x, user_name))
    return render_template("FUEL.html", member=user_name)

# FUEL
@app.route("/FUEL", methods=['POST', 'GET'])
def new_fuel() :
    x=request.form['Fuel']
    user_name = lst.pop()
    lst.append(user_name)
    obj.execute(""" update car 
                    set fuel='{0}' where username='{1}' """.format(x, user_name))
    return render_template("B_MAT.html", member=user_name)

# B_MAT
@app.route("/B_MAT", methods=['POST', 'GET'])
def new_b_mat() :
    x=request.form['Body_Material']
    user_name = lst.pop()
    lst.append(user_name)
    obj.execute(""" update car 
                    set bodyMaterial='{0}' where username='{1}' """.format(x, user_name))
    return render_template("S_MAT.html", member=user_name)

# S_MAT
@app.route("/S_MAT", methods=['POST', 'GET'])
def new_s_mat() :
    x=request.form['Seat_Material']
    user_name = lst.pop()
    lst.append(user_name)
    obj.execute(""" update car 
                    set seatMaterial='{0}' where username='{1}' """.format(x, user_name))
    return render_template("F_MAT.html", member=user_name)

# F_MAT
@app.route("/F_MAT", methods=['POST', 'GET'])
def new_f_mat() :
    x=request.form['Foot_Mat_Material']
    user_name = lst.pop()
    lst.append(user_name)
    obj.execute(""" update car 
                    set floorMaterial='{0}' where username='{1}' """.format(x, user_name))
    return render_template("SPEEDOMETER.html", member=user_name)

# SPEEDOMETER
@app.route("/SPEEDOMETER", methods=['POST', 'GET'])
def new_speedometer() :
    x=request.form['Speedometer']
    user_name = lst.pop()
    lst.append(user_name)
    obj.execute(""" update car 
                    set speedometer='{0}' where username='{1}' """.format(x, user_name))
    return render_template("STEREO.html", member=user_name)

# STEREO
@app.route("/STEREO", methods=['POST', 'GET'])
def new_stereo() :
    x=request.form['Stereo']
    user_name = lst.pop()
    lst.append(user_name)
    obj.execute(""" update car 
                    set stereo='{0}' where username='{1}' """.format(x, user_name))
    return render_template("SUNROOF.html", member=user_name)

# SUNROOF
@app.route("/SUNROOF", methods=['POST', 'GET'])
def new_sunroof() :
    x=request.form['Sunroof']
    user_name = lst.pop()
    lst.append(user_name)
    obj.execute(""" update car 
                    set sunroof='{0}' where username='{1}' """.format(x, user_name))
    return render_template("STEREO_EF.html", member=user_name)

# STEREO_EF
@app.route("/STEREO_EF", methods=['POST', 'GET'])
def new_stereo_ef() :
    x=request.form['Stereo_ef']
    user_name = lst.pop()
    lst.append(user_name)
    obj.execute(""" update car 
                    set stereoAdvanced='{0}' where username='{1}' """.format(x, user_name))
    return render_template("ADVANCED.html", member=user_name)

# ADVANCED
@app.route("/ADVANCED", methods=['POST', 'GET'])
def new_advanced() :
    x=request.form['Advanced_ef']
    user_name = lst.pop()
    lst.append(user_name)
    obj.execute(""" update car 
                    set advancedFeatures='{0}' where username='{1}' """.format(x, user_name))
    return render_template("DOOR.html", member=user_name)

# DOOR
@app.route("/DOOR", methods=['POST', 'GET'])
def new_door() :
    x=request.form['Door']
    user_name = lst.pop()
    lst.append(user_name)
    obj.execute(""" update car 
                    set door='{0}' where username='{1}' """.format(x, user_name))

    car_data = obj.execute(""" select * from car where username='{0}' """.format(user_name))
    return render_template("new_member.html",member = user_name, data = car_data)

if __name__ == "__main__":
    app.run()