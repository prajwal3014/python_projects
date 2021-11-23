import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from pyttsx3 import speak
from jerry_UI import Ui_Jerry
from Jerry import Listen, Speak
import webbrowser as wb
import wikipedia
import datetime
import os
from ecapture import ecapture as ec
import cv2

class jerry_commands(QThread) :
    def __init__(self) :
        super(jerry_commands, self).__init__()
    
    def run(self) :
        self.take_commands()
    
    def take_commands(self) :
        Speak("Welcome boss")
        while True :
            self.query = Listen()
            if "wake up" in self.query or "jerry" == self.query :
                Speak("yes boss, i am awake, Jerry one point o reporting in your service boss, how are you.")
            elif "how are you" in self.query :
                Speak("i am fine sir, what about you")
            elif "fine" in self.query or "good" in self.query or "great" in self.query :
                Speak("it's good to know that you are fine.")
            elif "help" in self.query or "favour" in self.query :
                Speak("Yes boss, how may i help you.")
            elif "i am sad" in self.query or "not fine" in self.query or "not good" in self.query or "not well" in self.query :
                Speak("It's ok boss, sometime situation becomes worst but we have to be strong, so be positive and face your all problems with smile.")
            elif "thank you" in self.query :
                Speak("your welcome sir, i am glad that you are happy with my service")
            elif "made you" in self.query or "created you" in self.query or "your creater" in self.query :
                Speak("I was created by Mister Prajwal Sharma and Mister Ayush Rana.")
            elif "your name" in self.query :
                Speak("My name is jerry one point o, I am a virtual assistant.")
            elif "open google" in self.query :
                Speak("Opening google")
                wb.open('www.google.com')
            elif "open youtube" in self.query :
                Speak("Opening youtube")
                wb.open('www.youtube.com')
            elif 'wikipedia' in self.query:
                Speak('Searching Wikipedia...')
                self.query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(self.query, sentences = 3)
                Speak("According to Wikipedia")
                print(results)
                Speak(results)
            elif 'open stack overflow' in self.query:
                Speak("Opening stackoverflow")
                wb.open("www.stackoverflow.com")
            elif 'the time' in self.query:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")   
                Speak(f"Sir, the time is {strTime}")
            elif 'play music' in self.query or "play song" in self.query:
                Speak("Playing music")
                music_dir = "C:\\Users\\ayush\\Music"
                songs = os.listdir(music_dir)
                print(songs)   
                random = os.startfile(os.path.join(music_dir, songs[1]))
            elif 'open downloads' in self.query:
                Speak("Opening downloads")
                path=r"C:\\Users\\ayush\\Downloads"
                os.startfile(path)
            elif 'open documents' in self.query:
                Speak("Opening documents")
                path=r"C:\\Users\\ayush\\Documents"
                os.startfile(path)
            elif 'open code blocks' in self.query:
                Speak("Opening codeeblocks")
                path=r"C:\\Program Files\\CodeBlocks\\codeblocks.exe"
                os.startfile(path)
            elif "camera" in self.query or "take a photo" in self.query:
                videoCaptureObject = cv2.VideoCapture(0)
                result = True
                while(result):
                    ret,frame = videoCaptureObject.read()
                    cv2.imwrite("NewPicture.jpg",frame)
                    result = False
                videoCaptureObject.release()
                cv2.destroyAllWindows()
            elif 'search' in self.query:
                self.query = self.query.replace("search", "")        
                wb.open(self.query)
            elif "exit" in self.query :
                Speak("Thanks boss for your time, Closing me, three, two, one, bye boss.")
                exit()

start_jerry = jerry_commands()

class jerry_main(QMainWindow) :
    def __init__(self):
        super().__init__()
        self.ui = Ui_Jerry()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)
    
    def startTask(self) :
        self.ui.movie = QtGui.QMovie("jerry.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("open.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)

        start_jerry.start()
    
    def showTime(self) :
        now_time = QTime.currentTime()
        now_date = QDate.currentDate()
        label_time = now_time.toString('hh:mm:ss')
        label_date = now_date.toString(Qt.ISODate)

        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)

app = QApplication(sys.argv)
jerry = jerry_main()
jerry.show()
exit(app.exec_())