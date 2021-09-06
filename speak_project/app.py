from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO
import Jerry

app = Flask(__name__)
socketio = SocketIO(app,cors_allowed_origins="*")

#Home
@app.route('/')
def home() :
    return render_template("home.html")

# @app.route('/toMain', methods = ['POST'])
# def to_main() :
#     command = request.form['data']
#     Jerry.Speak(command)
#     return redirect(url_for('home'))

@socketio.on('to_main')
def to_main(data) :
    while True :
        query = Jerry.Listen()
        
        if "wake up" in query or "jerry" == query :
            Jerry.Speak("yes boss, i am awake, Jerry one point o reporting in your service boss, how are you.")
        elif "how are you" in query :
            Jerry.Speak("i am fine sir, what about you")
        elif "fine" in query or "good" in query or "great" in query :
            Jerry.Speak("it's good to know that you are fine.")
        elif "help" in query or "favour" in query :
            Jerry.Speak("Yes boss, how may i help you.")
        elif "i am sad" in query or "not fine" in query or "not good" in query or "not well" in query :
            Jerry.Speak("It's ok boss, sometime situation becomes worst but we have to be strong, so be positive and face your all problems with smile.")
        elif "thank you" in query :
            Jerry.Speak("your welcome sir, i am glad that you are happy with my service")
        elif "made you" in query or "created you" in query or "your creater" in query :
            Jerry.Speak("I was created by Mister Prajwal Sharma and Mister Ayush Rana.")
        elif "your name" in query :
            Jerry.Speak("My name is jerry one point o, I am a virtual assistant.")
        # start elif from here
        # elif "open google" in query :
        #     Jerry.Speak("Opening google")
        #     wb.open('www.google.com')
        elif "exit" in query :
            Jerry.Speak("Thanks boss for your time, Closing me, three, two, one, bye boss.")
            # exit()
            socketio.emit('something', msg = "done")

if __name__ == '__main__' :
    socketio.run(app, debug=True)