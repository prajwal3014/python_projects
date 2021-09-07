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

class jerry_commands(QThread) :
    def __init__(self) :
        super(jerry_commands, self).__init__()
    
    def run(self) :
        self.TaskExecution()
    
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
            # start elif from here
            elif "open google" in self.query :
                Speak("Opening google")
                wb.open('www.google.com')
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