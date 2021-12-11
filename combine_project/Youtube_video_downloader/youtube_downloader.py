import tkinter as tk
from tkinter import *
from tkinter.font import BOLD
from PIL import ImageTk, Image
from pytube import YouTube
from tkinter import messagebox, filedialog

def browse():
    download_Directory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH", title="SAVE VIDEO")
    s_4.delete(0,END)
    s_4.insert(0,download_Directory)

def download():
    download_Folder=s_4.get()
    Youtube_link=s_2.get()
    if Youtube_link!="":
        
        try:
            get_video=YouTube(Youtube_link)

            if val.get()=="high":
                try:
                    video_stream=get_video.streams.filter(res="360p").first()
                except:
                    video_stream=get_video.streams.first()
            elif val.get()=="medium":
                try:
                    video_stream=get_video.streams.filter(res="240p").first()
                except:
                    video_stream=get_video.streams.first()
            elif val.get()=="low":
                video_stream=get_video.streams.first()

            video_stream.download(download_Folder)

            if download_Folder=="":
                messagebox.showinfo("showinfo","Downloaded and saved in default user location")
            else:
                messagebox.showinfo("showinfo","Downloaded and saved in :"+download_Folder)

        except:
            messagebox.showinfo("showinfo","Link not found")

    else:
        messagebox.showwarning("WARNING","please enter youtube link")
    download_Folder = s_4.get()

def sub():
    global s_2,s_4,val

    sub_window=tk.Tk()
    sub_window.geometry("520x280")
    sub_window.resizable(False,False)
    sub_window.title("Youtube-video-downloader")
    sub_window.config(background="skyblue")
    head1=tk.Label(sub_window,text="",bg="skyblue")
    head1.pack()
    head=tk.Label(sub_window,text="YOUTUBE VIDEO DOWNLOADER",font=("ariel",18,BOLD),fg="white",bg="skyblue")
    head.pack()
    s_1=tk.Label(sub_window,text="Youtube link :",font=("ariel",12,BOLD),fg="white",bg="skyblue")
    s_1.place(x=10,y=70)
    s_2=tk.Entry(sub_window,font="ariel",width=40)
    s_2.place(x=130,y=70)
    s_3=tk.Label(sub_window,text="Destination :",font=("ariel",12,BOLD),fg="white",bg="skyblue")
    s_3.place(x=10,y=120)
    s_4=tk.Entry(sub_window,font="ariel",width=25)
    s_4.place(x=120,y=120)

    def to_browse():
        browse()

    s_5=tk.Button(sub_window,text="Browse",font=("ariel",10,BOLD),fg="white",bg="orange",width=14,command=to_browse)
    s_5.place(x=370,y=117)

    def to_download():
        download()

    s_6=tk.Button(sub_window,text="Download video",font=("ariel",10,BOLD),fg="white",bg="green",width=20,command=to_download)
    s_6.place(x=170,y=170)
    s_8=tk.Label(sub_window,text="Video-quality",font=("ariel",12,BOLD),fg="white",bg="skyblue")
    s_8.place(x=370,y=170)

    def to_exit():
        if messagebox.askquestion("exit","Are you sure you want to exit ?")=="yes":
            sub_window.destroy()

    s_7=tk.Button(sub_window,text="Exit program",font=("ariel",10,BOLD),fg="white",bg="red",width=20,command=to_exit)
    s_7.place(x=170,y=210)
    val=StringVar()
    val.set("low")
    option_list=["low","medium","high"]
    s_9=tk.OptionMenu(sub_window,val,*option_list)
    s_9.place(x=370,y=210)

    sub_window.mainloop()

def proceed():
    pro_window=tk.Tk()
    pro_window.geometry("600x350")
    pro_window.resizable(False,False)
    pro_window.title("Youtube-video-downloader")
    pro_window.config(background="skyblue")
    head1=tk.Label(pro_window,text="",bg="skyblue")
    head1.pack()
    p_1=tk.Label(text="INFORMATION",font=("ariel",18,BOLD),fg="white",bg="skyblue")
    p_1.pack()
    head1=tk.Label(pro_window,text="",bg="skyblue")
    head1.pack()
    p_2=tk.Label(text="If you are not going to give destination path, ",font=("ariel",12,BOLD),bg="white",fg="red")
    p_2.pack()
    p_5=tk.Label(text="then it will going to save video in default user",font=("ariel",12,BOLD),bg="white",fg="red")
    p_5.pack()
    head1=tk.Label(pro_window,text="",bg="skyblue")
    head1.pack()
    p_3=tk.Label(text="If video is not present in high(360p) or medium(240p) quality, ",font=("ariel",12,BOLD),bg="white",fg="red")
    p_3.pack()
    p_6=tk.Label(text="then it is going to download video in first present quality of video",font=("ariel",12,BOLD),bg="white",fg="red")
    p_6.pack()
    head1=tk.Label(pro_window,text="",bg="skyblue")
    head1.pack()
    head1=tk.Label(pro_window,text="",bg="skyblue")
    head1.pack()

    def to_sub():
        pro_window.destroy()
        sub()

    p_4=tk.Button(text="Proceed",font=("ariel",10,BOLD),fg="white",bg="green",width=15,command=to_sub)
    p_4.pack()

    pro_window.mainloop()

def window_main():
    main_window=tk.Tk()
    main_window.geometry("500x400")
    main_window.resizable(False,False)
    main_window.title("Youtube-video-downloader")
    bg = ImageTk.PhotoImage(Image.open("youtube.jpg"))
    canvas = Canvas(main_window, width = 500,height = 400)
    canvas.pack(fill = "both", expand = True)
    canvas.create_image( 0, 0, image = bg, anchor = "nw")

    def to_proceed():
        main_window.destroy()
        proceed()

    canvas.create_text( 250, 100, text = "Welcome",font=("ariel",75,BOLD),fill="skyblue")
    button=tk.Button(main_window,text="START",bg="skyblue",fg="white",font=("ariel",18,BOLD),width=10,bd=5,command=to_proceed)
    button_canvas = canvas.create_window( 165, 200, anchor = "nw", window = button)

    main_window.mainloop()