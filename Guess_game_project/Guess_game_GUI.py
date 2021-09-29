import tkinter as tk
from tkinter import messagebox
from tkinter.font import BOLD
import random

def play_again(score) :
    guess_window.destroy()
    again_window = tk.Tk()
    again_window.geometry("500x500")
    again_window.title("Guess the Number")
    
    if score > 40 :
        lab = tk.Label(text="\nCongratulations...!", fg="green", font=("arial", 18, BOLD)).pack()
        lab = tk.Label(text="\nYou win, Your Score is " + str(score), fg="blue", font=("arial", 15)).pack()
    elif score <= 40 :
        lab = tk.Label(text="\nOOPS...!", fg="green", font=("arial", 18, BOLD)).pack()
        lab = tk.Label(text="\nYou loose, Your Score is " + str(score), fg="blue", font=("arial", 15)).pack()
    
    lab = tk.Label(text="\nDo you want to play again?", fg="green", font=("arial", 15)).pack()
    lab = tk.Label(text=" ").pack()
    def if_yes() :
        again_window.destroy()
        game()
    yes = tk.Button(text="YES", fg="white", bg="green", command=if_yes).pack()
    lab = tk.Label(text=" ").pack()
    def if_no() :
        action = messagebox.askquestion("Confirm","Are you sure?")
        if action == "yes" :
            again_window.destroy()
        elif action == "no" :
            pass
    no = tk.Button(text="NO", fg="white", bg="green", command=if_no).pack()

def checking_number(user_num, random_answer, score, start, end) :
    real_score = score
    if real_score > 40 :
        if user_num < random_answer :
            score = score - 5
            messagebox.showwarning("showwarning","Guess a higher number...!\nYour score is : {}".format(score))
            guess_window.destroy()
            guess_number(start, end, random_answer, score)
        elif user_num > random_answer :
            score = score - 5
            messagebox.showwarning("showwarning","Guess a smaller number...!\nYour score is : {}".format(score))
            guess_window.destroy()
            guess_number(start, end, random_answer, score)
        elif user_num == random_answer :
            play_again(score)
    elif score <= 40 :
        play_again(score)

def guess_number(start, end, random_answer, score) :
    global guess_window
    guess_window = tk.Tk()
    guess_window.geometry("500x400")
    guess_window.title("Guess the Number")

    head = tk.Label(text="\nGuessing Game\n", font=("arial", 18, BOLD)).pack()
    
    if start > end :
        start, end = end, start
    elif start == end :
        messagebox.showwarning("showwarning","Enter a valid range...!")

    l_1 = tk.Label(text="A number has been choosen from " + str(start) + " and " + str(end), font=("arial", 12)).pack()

    lab = tk.Label(text=" ").pack()

    l_1 = tk.Label(text="Guess the number : ", font=("arial", 12)).pack()
    e = tk.Entry(guess_window, width=30, fg="blue")
    e.pack()
    
    def to_check() :
        user_num = e.get()
        try :
            user_num = int(user_num)
            checking_number(user_num, random_answer, score, start, end)
        except :
            messagebox.showwarning("showwarning","Number must be numeric...!")
            guess_window.destroy()
            guess_number(start, end, random_answer)

    lab = tk.Label(text=" ").pack()
    submit = tk.Button(text="Submit", fg="white", bg="green", command=to_check).pack()
    
    guess_window.mainloop()

def set_range() :
    window = tk.Tk()
    window.geometry("500x400")
    window.title("Guess the Number")

    head = tk.Label(text="\nGuessing Game\n", font=("arial", 18, BOLD)).pack()

    l_1 = tk.Label(text="Enter lower limit : ", font=("arial", 12)).place(x=70, y=100)
    e_1 = tk.Entry(window, fg="blue", width=30, bg='white')
    e_1.place(x=200, y=101)
    
    l_2 = tk.Label(text="Enter upper limit : ", font=("arial", 12)).place(x=70, y=150)
    e_2 = tk.Entry(window, width=30, fg="blue", bg='white')
    e_2.place(x=200, y=151)
    
    def to_guess() :
        score = 100
        start = e_1.get()
        end = e_2.get()
        try :
            start = int(start)
            end = int(end)
            num_list = []
            for num in range(start, end+1) :
                num_list.append(num)
            random_answer = random.choice(num_list)
            print(random_answer)
            window.destroy()
            guess_number(start, end, random_answer, score)
        except :
            messagebox.showwarning("showwarning","Number must be numeric...!")
            window.destroy()
            set_range()

    submit = tk.Button(text="Submit", fg="white", bg="green", command=to_guess).place(x=220, y=190)
    window.mainloop()

def game() :
    main_window = tk.Tk()
    main_window.geometry("700x450")
    main_window.title("Guess the Number")

    head = tk.Label(text="\nGuessing Game\n", font=("arial", 18, BOLD)).pack()

    l_1 = tk.Label(text="Please go through the rules before starting it =>", font=("arial", 11)).place(x=10, y=70)
    l_1 = tk.Label(text="1. You have to enter a range and we choose a random number between this range.", font=("arial", 11)).place(x=10, y=100)
    l_1 = tk.Label(text="2. You have to guess that choosen number.", font=("arial", 11)).place(x=10, y=130)
    l_1 = tk.Label(text="3. Score starts from 100 points and for each wrong guess 5 points is deducted.", font=("arial", 11)).place(x=10, y=160)
    l_1 = tk.Label(text="4. We will give you hints during the guessing of number.", font=("arial", 11)).place(x=10, y=190)
    l_1 = tk.Label(text="5. You have to maintain a minimum score of 40 points, if points become less than 40 than you loose.", font=("arial", 11)).place(x=10, y=220)
    
    def to_set() :
        main_window.destroy()
        set_range()

    start = tk.Button(text="Start Game", fg="white", bg="green", command=to_set).place(x=300, y=300)
    main_window.mainloop()

game()