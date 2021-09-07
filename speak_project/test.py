import tkinter
from tkinter import *
from PIL import ImageTk, Image

window = Tk()
# window.geometry("500x500")
window.title("Jerry")

canvas = Canvas(window, width = 500, height = 500)
canvas.pack()

my_image = PhotoImage(file='F:\\Prajwal_Desktop\\python_projects\\speak_project\\open.gif')
canvas.create_image(0, 0, anchor = NW, image=my_image)

# img=PhotoImage(file='open.gif')
# Label(window, image=img, bg="black").pack()

# l = Label(window, text="Jerry")
# l.pack()

window.mainloop()