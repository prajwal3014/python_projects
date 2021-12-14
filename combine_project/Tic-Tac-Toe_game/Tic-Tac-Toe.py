import tkinter as tk
from tkinter import messagebox
from tkinter.constants import FALSE
from tkinter.font import BOLD

def Quit():
    global main_window    
    msg=messagebox.askquestion("Confirm","Are you sure you want to Quit? You still have chances!")
    if msg=='yes':
        main_window.destroy()

def retry():
    winnerWindow.destroy()
    pregame()
    

def destruct():
    msg=messagebox.askquestion("Confirm","Are you sure you want to Exit?")
    if msg=='yes':
        winnerWindow.destroy()

def displayWinner(winner):
    global winnerWindow    
    winnerWindow=tk.Tk()
    winnerWindow.title("Winner Window")
    winnerWindow.geometry("400x300")
    winnerWindow.resizable(FALSE,FALSE)
    winnerWindow.configure(bg="Red")
    l0=tk.Label(winnerWindow,text="",bg="Red")
    l0.pack()
    l1=tk.Label(winnerWindow,text="THE WINNER IS: ",font=("Ariel",30,BOLD),bg="Red",fg="White")
    l1.pack()
    l0=tk.Label(winnerWindow,text="",bg="Red")
    l0.pack()
    l2=tk.Label(winnerWindow,text=winner,font=("Ariel",12,BOLD),bg="Red",fg="White")
    l2.pack()
    l3=tk.Button(winnerWindow,text="RETRY",font=("Ariel",10,BOLD),width=10,command=retry,bg="Green",fg="White")
    l3.place(x=150,y=150)
    l4=tk.Button(winnerWindow,text="EXIT",font=("Ariel",10,BOLD),width=10,command=destruct,bg="Orange",fg="White")
    l4.place(x=150,y=190)
    
def checkWinner():
    if (board[0][0]==board[0][1]==board[0][2]=="X" or board[1][0]==board[1][1]==board[1][2]=="X" or board[2][0]==board[2][1]==board[2][2]=="X" or
        board[0][0]==board[1][0]==board[2][0]=="X" or board[0][1]==board[1][1]==board[2][1]=="X" or board[0][2]==board[1][2]==board[2][2]=="X" or
        board[0][0]==board[1][1]==board[2][2]=="X" or board[0][2]==board[1][1]==board[2][0]=="X"):
            main_window.destroy()
            displayWinner(pX)
    elif (board[0][0]==board[0][1]==board[0][2]=="O" or board[1][0]==board[1][1]==board[1][2]=="O" or board[2][0]==board[2][1]==board[2][2]=="O" or
          board[0][0]==board[1][0]==board[2][0]=="O" or board[0][1]==board[1][1]==board[2][1]=="O" or board[0][2]==board[1][2]==board[2][2]=="O" or
          board[0][0]==board[1][1]==board[2][2]=="O" or board[0][2]==board[1][1]==board[2][0]=="O"):
            main_window.destroy()
            displayWinner(pO)
    elif count==9:
        main_window.destroy()
        displayWinner(" NONE! ")

def changeVal(button,boardValRow,boardValCol):
    global count
    if button["text"]=="":
        if count%2==0:
            button["text"]="X"
            l1=tk.Label(main_window,text=f"PLAYER O: {pO}",height=3,font=("Ariel",10,BOLD),bg="Red",fg="White").grid(row=0,column=0)
            board[boardValRow][boardValCol]="X"
        else:
            button["text"]="O"
            l1=tk.Label(main_window,text=f"PLAYER X: {pX}",height=3,font=("Ariel",10,BOLD),bg="Red",fg="White").grid(row=0,column=0)
            board[boardValRow][boardValCol]="O"
        count=count+1
        if count>=5:
            checkWinner()
    else:
        messagebox.showerror("Error","This box already has a value!")

def TicTacToeGUI(playerX,playerO):
    global main_window,pX,pO
    main_window=tk.Tk()
    main_window.title("TIC TAC TOE")
    main_window.configure(bg="Red")
    pX=playerX
    pO=playerO
    l1=tk.Label(main_window,text=f"PLAYER X: {pX}",height=3,font=("Ariel",10,BOLD),bg="Red",fg="White")
    l1.grid(row=0,column=0)

    exitButton=tk.Button(main_window,text="Quit",command=Quit,font=("Ariel",10,BOLD),bg="green",fg="White",width=10)
    exitButton.grid(row=0,column=2)

    b1=tk.Button(main_window,text="",height=4,width=8,bg="White",activebackground="Red",fg="Red",font="Ariel 30 bold",command=lambda: changeVal(b1,0,0))
    b2=tk.Button(main_window,text="",height=4,width=8,bg="White",activebackground="Red",fg="Red",font="Ariel 30 bold",command=lambda: changeVal(b2,0,1))
    b3=tk.Button(main_window,text="",height=4,width=8,bg="White",activebackground="Red",fg="Red",font="Ariel 30 bold",command=lambda: changeVal(b3,0,2))
    b4=tk.Button(main_window,text="",height=4,width=8,bg="White",activebackground="Red",fg="Red",font="Ariel 30 bold",command=lambda: changeVal(b4,1,0))
    b5=tk.Button(main_window,text="",height=4,width=8,bg="White",activebackground="Red",fg="Red",font="Ariel 30 bold",command=lambda: changeVal(b5,1,1))
    b6=tk.Button(main_window,text="",height=4,width=8,bg="White",activebackground="Red",fg="Red",font="Ariel 30 bold",command=lambda: changeVal(b6,1,2))
    b7=tk.Button(main_window,text="",height=4,width=8,bg="White",activebackground="Red",fg="Red",font="Ariel 30 bold",command=lambda: changeVal(b7,2,0))
    b8=tk.Button(main_window,text="",height=4,width=8,bg="White",activebackground="Red",fg="Red",font="Ariel 30 bold",command=lambda: changeVal(b8,2,1))
    b9=tk.Button(main_window,text="",height=4,width=8,bg="White",activebackground="Red",fg="Red",font="Ariel 30 bold",command=lambda: changeVal(b9,2,2))
    b1.grid(row=2,column=0)
    b2.grid(row=2,column=1)
    b3.grid(row=2,column=2)
    b4.grid(row=3,column=0)
    b5.grid(row=3,column=1)
    b6.grid(row=3,column=2)
    b7.grid(row=4,column=0)
    b8.grid(row=4,column=1)
    b9.grid(row=4,column=2)
    main_window.mainloop()

def pregame():
    global count,board
    count=0
    board=[['','','',],
           ['','','',],
           ['','','',]]
    pre_window=tk.Tk()
    pre_window.title("TIC TAC TOE")
    pre_window.geometry("500x300")
    pre_window.resizable(FALSE,FALSE)
    pre_window.config(bg="Red")
    l0=tk.Label(pre_window,text="",bg="Red")
    l0.pack()
    l1=tk.Label(pre_window,text="TIC-TAC-TOE",font=("Ariel",18,BOLD),bg="Red",fg="White")
    l1.pack()
    s_1=tk.Label(pre_window,text="Player X :",font=("ariel",12,BOLD),fg="white",bg="Red")
    s_1.place(x=30,y=100)
    s_2=tk.Entry(pre_window,font="ariel",width=30)
    s_2.place(x=130,y=100)
    s_3=tk.Label(pre_window,text="Player O :",font=("ariel",12,BOLD),fg="white",bg="Red")
    s_3.place(x=30,y=150)
    s_4=tk.Entry(pre_window,font="ariel",width=30)
    s_4.place(x=130,y=150)

    def to_proceed():
        playerX=s_2.get()
        playerO=s_4.get()
        if playerX=="" or playerO=="":
            messagebox.showwarning("WARNING","Please enter both playerX and playerO")
        else:
            pre_window.destroy()
            TicTacToeGUI(playerX,playerO)

    s_6=tk.Button(pre_window,text="Proceed",font=("ariel",10,BOLD),fg="white",bg="green",width=20,command=to_proceed)
    s_6.place(x=170,y=200)

    def to_exit():
        msg=messagebox.askquestion("Confirm","Are you sure you want to Exit?")
        if msg=='yes':
            pre_window.destroy()

    s_7=tk.Button(pre_window,text="Exit",font=("ariel",10,BOLD),fg="white",bg="Orange",width=20,command=to_exit)
    s_7.place(x=170,y=240)

    pre_window.mainloop()

pregame()