from flask import Flask, request, render_template, redirect, url_for
import tkinter as tk
from tkinter import messagebox
from tkinter.constants import END
import math
from tkinter.font import BOLD
import sqlite3

obj = sqlite3.connect("calculator.db", check_same_thread=False)

obj.execute(""" create table if not exists calculator (
                operation varchar(255),
                answer varchar(255)
            ) """)
obj.commit()

def save_history(operation, answer) :
    obj.execute(""" insert into calculator values ('{}', '{}') """.format(operation, answer))
    obj.commit()

def show_history() :
    history = []
    query = obj.execute(""" select * from calculator """)
    lst = query.fetchall()
    for data in lst :
        history.append(list(data))
    return history

def delete_history() :
    obj.execute(""" drop table if exists calculator """)
    obj.commit()
    obj.execute(""" create table if not exists calculator (
                    operation varchar(255),
                    answer varchar(255)
                ) """)
    obj.commit()

def history_calculator() :
    window = tk.Tk()
    window.geometry("500x500")
    window.title("Calculator")

    def to_clear() :
        window.destroy()
        delete_history()
        history_calculator()

    clear = tk.Button(text="Clear History", fg="white", bg="red", width=15, command=to_clear, borderwidth=5, activebackground="green", activeforeground="white").place(x=360, y=30)

    def to_main() :
        window.destroy()
        calculator()

    back = tk.Button(text="Back", fg="white", bg="red", width=15, command=to_main, borderwidth=5, activebackground="green", activeforeground="white").place(x=20, y=30)

    head = tk.Label(text="\nHistory\n", font=("arial", 18, BOLD)).pack()

    history = show_history()

    for data in history :
        lab = tk.Label(text=data[0] + " = " + data[1] + "\n", fg="blue", font=("arial", 15)).pack()
    
    window.mainloop()

equation = []
def calculator() :
    window = tk.Tk()
    window.geometry("510x520")
    window.title("Calculator")

    value = tk.Entry(window, bg="white", fg="blue", font=("arial", 20))
    value.insert(0, "0")
    value.place(x=10, y=10, height = 60, width=490)

    def to_all_clear() :
        value.delete(0, END)
        equation.clear()

    all_clear = tk.Button(text="AC", bg="Orange", fg="White", command=to_all_clear, font=("arial", 20), height=1, borderwidth=5).place(x=20, y=80)

    def to_clear() :
        a = value.get()
        value.delete(len(a)-1)

    clear = tk.Button(text="C", bg="orange", fg="white", command=to_clear, width=3, font=("arial", 20), height=1, borderwidth=5).place(x=100, y=80)

    def to_root() :
        a = value.get()
        try :
            a = float(a)
            answer = math.sqrt(a)
            value.delete(0, END)
            value.insert(0, answer)
            save_history(("√" + str(a)), str(answer))
        except :
            messagebox.showwarning("Wrong Input", "Invalid Input...!")
            value.delete(0, END)
    
    sq_root = tk.Button(window, text="√x", bg="blue", fg="white", command=to_root, font=("arial", 20), height=1, borderwidth=5, width=3).place(x=180, y=80)

    def to_cube_root() :
        a = value.get()
        try :
            a = float(a)
            if a>0 :
                answer = a ** (1/3)
            else :
                answer = -(-a) ** (1/3)
            value.delete(0, END)
            value.insert(0, answer)
            save_history(("∛" + str(a)), str(answer))
        except :
            messagebox.showwarning("Wrong Input", "Invalid Input...!")
            value.delete(0, END)
    
    cube_root = tk.Button(window, text="∛x", bg="blue", fg="white", command=to_cube_root, font=("arial", 20), height=1, borderwidth=5, width=3).place(x=260, y=80)

    def to_sq() :
        a = value.get()
        try :
            a = float(a)
            answer = a ** 2
            value.delete(0, END)
            value.insert(0, answer)
            save_history((str(a) + "²"), str(answer))
        except :
            messagebox.showwarning("Wrong Input", "Invalid Input...!")
            value.delete(0, END)
    
    sq = tk.Button(window, text="x²", bg="blue", fg="white", command=to_sq, font=("arial", 20), height=1, borderwidth=5, width=3).place(x=340, y=80)

    def to_cube() :
        a = value.get()
        try :
            a = float(a)
            answer = a ** 3
            value.delete(0, END)
            value.insert(0, answer)
            save_history((str(a) + "³"), str(answer))
        except :
            messagebox.showwarning("Wrong Input", "Invalid Input...!")
            value.delete(0, END)
    
    cube = tk.Button(window, text="x³", bg="blue", fg="white", command=to_cube, font=("arial", 20), height=1, borderwidth=5, width=3).place(x=420, y=80)

    def to_n_root() :
        a = value.get()
        try :
            a = float(a)
            equation.append(a)
            equation.append("**(1/")
            value.delete(0, END)
        except :
            messagebox.showwarning("Wrong Input", "Invalid Input...!")
            value.delete(0, END)
    
    n_root = tk.Button(text="ⁿ√x", bg="blue", fg="white", command=to_n_root, font=("arial", 20), height=1, borderwidth=5, width=3).place(x=260, y=150)

    def to_n_power() :
        a = value.get()
        try :
            a = float(a)
            equation.append(a)
            equation.append("**")
            value.delete(0, END)
        except :
            messagebox.showwarning("Wrong Input", "Invalid Input...!")
            value.delete(0, END)

    n_power = tk.Button(text="xⁿ", bg="blue", fg="white", command=to_n_power, font=("arial", 20), height=1, borderwidth=5, width=3).place(x=340, y=150)

    def to_fact() :
        a = value.get()
        try :
            a = float(a)
            answer = math.factorial(a)
            value.delete(0, END)
            value.insert(0, answer)
            save_history((str(a) + "!"), str(answer))
        except :
            messagebox.showwarning("Wrong Input", "Invalid Input...!")
            value.delete(0, END)

    fact = tk.Button(text="x!", bg="magenta", fg="white", command=to_fact, width=3, font=("arial", 20), height=1, borderwidth=5).place(x=260, y=220)

    def to_sin() :
        a = value.get()
        try :
            a = float(a)
            answer = math.sin(a)
            value.delete(0, END)
            value.insert(0, answer)
            save_history(("sin " + str(a)), str(answer))
        except :
            messagebox.showwarning("Wrong Input", "Invalid Input...!")
            value.delete(0, END)

    sin = tk.Button(text="sin", bg="magenta", fg="white", command=to_sin, width=3, font=("arial", 20), height=1, borderwidth=5).place(x=340, y=220)

    def to_cos() :
        a = value.get()
        try :
            a = float(a)
            answer = math.cos(a)
            value.delete(0, END)
            value.insert(0, answer)
            save_history(("cos " + str(a)), str(answer))
        except :
            messagebox.showwarning("Wrong Input", "Invalid Input...!")
            value.delete(0, END)

    cos = tk.Button(text="cos", bg="magenta", fg="white", command=to_cos, width=3, font=("arial", 20), height=1, borderwidth=5).place(x=260, y=290)

    def to_tan() :
        a = value.get()
        try :
            a = float(a)
            answer = math.tan(a)
            value.delete(0, END)
            value.insert(0, answer)
            save_history(("tan " + str(a)), str(answer))
        except :
            messagebox.showwarning("Wrong Input", "Invalid Input...!")
            value.delete(0, END)

    tan = tk.Button(text="tan", bg="magenta", fg="white", command=to_tan, width=3, font=("arial", 20), height=1, borderwidth=5).place(x=340, y=290)

    def to_nine() :
        a = value.get()
        if a :
            value.insert(len(a), "9")
        else :
            value.insert(0, "9")

    nine = tk.Button(text="9", bg="green", fg="white", command=to_nine, font=("arial", 20), height=1, borderwidth=5, width=3).place(x=20, y=150)

    def to_eigth() :
        a = value.get()
        if a :
            value.insert(len(a), "8")
        else :
            value.insert(0, "8")

    eight = tk.Button(text="8", bg="green", fg="white", command=to_eigth, width=3, font=("arial", 20), height=1, borderwidth=5).place(x=100, y=150)

    def to_seven() :
        a = value.get()
        if a :
            value.insert(len(a), "7")
        else :
            value.insert(0, "7")

    seven = tk.Button(text="7", bg="green", fg="white", command=to_seven, width=3, font=("arial", 20), height=1, borderwidth=5).place(x=180, y=150)

    def to_six() :
        a = value.get()
        if a :
            value.insert(len(a), "6")
        else :
            value.insert(0, "6")

    six = tk.Button(text="6", bg="green", fg="white", command=to_six, width=3, font=("arial", 20), height=1, borderwidth=5).place(x=20, y=220)

    def to_five() :
        a = value.get()
        if a :
            value.insert(len(a), "5")
        else :
            value.insert(0, "5")

    five = tk.Button(text="5", bg="green", fg="white", command=to_five, width=3, font=("arial", 20), height=1, borderwidth=5).place(x=100, y=220)

    def to_four() :
        a = value.get()
        if a :
            value.insert(len(a), "4")
        else :
            value.insert(0, "4")

    four = tk.Button(text="4", bg="green", fg="white", command=to_four, width=3, font=("arial", 20), height=1, borderwidth=5).place(x=180, y=220)

    def to_three() :
        a = value.get()
        if a :
            value.insert(len(a), "3")
        else :
            value.insert(0, "3")

    three = tk.Button(text="3", bg="green", fg="white", command=to_three, width=3, font=("arial", 20), height=1, borderwidth=5).place(x=20, y=290)

    def to_two() :
        a = value.get()
        if a :
            value.insert(len(a), "2")
        else :
            value.insert(0, "2")

    two = tk.Button(text="2", bg="green", fg="white", command=to_two, width=3, font=("arial", 20), height=1, borderwidth=5).place(x=100, y=290)

    def to_one() :
        a = value.get()
        if a :
            value.insert(len(a), "1")
        else :
            value.insert(0, "1")

    one = tk.Button(text="1", bg="green", fg="white", command=to_one, width=3, font=("arial", 20), height=1, borderwidth=5).place(x=180, y=290)

    def to_zero() :
        a = value.get()
        if a :
            value.insert(len(a), "0")
        else :
            value.insert(0, "0")

    zero = tk.Button(text="0", bg="green", fg="white", command=to_zero, width=3, font=("arial", 20), height=1, borderwidth=5).place(x=20, y=360)

    def to_d_zero() :
        a = value.get()
        if a :
            value.insert(len(a), "00")
        else :
            value.insert(0, "0")

    double_zero = tk.Button(text="00", bg="green", fg="white", command=to_d_zero, width=3, font=("arial", 20), height=1, borderwidth=5).place(x=100, y=360)

    def to_decimal() :
        a = value.get()
        if a :
            value.insert(len(a), ".")
        else :
            value.insert(0, "0.")

    decimal = tk.Button(text=".", bg="green", fg="white", command=to_decimal, width=3, font=("arial", 20), height=1, borderwidth=5).place(x=180, y=360)

    def to_divide() :
        a = value.get()
        try :
            a = float(a)
            equation.append(a)
            equation.append("/")
            value.delete(0, END)
        except :
            messagebox.showwarning("Wrong Input", "Invalid Input...!")
            value.delete(0, END)

    divide = tk.Button(window, text="/", bg="red", fg="white", command=to_divide, font=("arial", 20), width=3, height=1, borderwidth=5).place(x=420, y=150)

    def to_mul() :
        a = value.get()
        try :
            a = float(a)
            equation.append(a)
            equation.append("*")
            value.delete(0, END)
        except :
            messagebox.showwarning("Wrong Input", "Invalid Input...!")
            value.delete(0, END)

    mul = tk.Button(window, text="X", bg="red", fg="white", command=to_mul, font=("arial", 20), width=3, height=1, borderwidth=5).place(x=420, y=220)

    def to_sub() :
        a = value.get()
        try :
            a = float(a)
            equation.append(a)
            equation.append("-")
            value.delete(0, END)
        except :
            messagebox.showwarning("Wrong Input", "Invalid Input...!")
            value.delete(0, END)

    sub = tk.Button(window, text="-", bg="red", fg="white", command=to_sub, font=("arial", 20), width=3, height=1, borderwidth=5).place(x=420, y=290)

    def to_add() :
        a = value.get()
        try :
            a = float(a)
            equation.append(a)
            equation.append("+")
            value.delete(0, END)
        except :
            messagebox.showwarning("Wrong Input", "Invalid Input...!")
            value.delete(0, END)

    add = tk.Button(window, text="+", bg="red", fg="white", command=to_add, font=("arial", 20), width=3, height=1, borderwidth=5).place(x=420, y=360)
    
    def to_equal() :
        str_eq = ""
        a = value.get()
        try :
            a = float(a)
            if equation[-1] == "**(1/" :
                equation.append(str(a) + ")")
            else :
                equation.append(a)
            value.delete(0, END)
            for element in equation :
                str_eq = str_eq + str(element)
            value.insert(0, str(eval(str_eq)))
            save_history(str_eq.replace("**", "^"), str(eval(str_eq)))
            equation.clear()
        except :
            messagebox.showwarning("Wrong Input", "Invalid Input...!")
            value.delete(0, END)
    
    equal = tk.Button(window, text="=", bg="orange", fg="white", command=to_equal, font=("arial", 20), width=8, height=1, borderwidth=5).place(x=260, y=360)

    def to_history() :
        window.destroy()
        history_calculator()

    history = tk.Button(window, text="History", bg="brown", fg="white", command=to_history, width=15, borderwidth=5, font=("arial", 12), activebackground="green", activeforeground="white").place(x=50, y=450)

    def to_exit() :
        x = messagebox.askquestion("Exit", "Are you sure?")
        if x == "yes" :
            window.destroy()
        else :
            pass

    exit = tk.Button(window, text="Exit", bg="brown", fg="white", command=to_exit, width=15, borderwidth=5, font=("arial", 12), activebackground="green", activeforeground="white").place(x=300, y=450)
    window.mainloop()

app = Flask(__name__)
app.secret_key = 'COMBINING ALL PROJECTS'

@app.route('/')
def index() :
    return render_template('index.html')

@app.route('/Calculator', methods = ['GET', 'POST'])
def to_calculator() :
    calculator()
    return redirect(url_for('index'))

if __name__ == "__main__" :
    app.run(debug=True)