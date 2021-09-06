import pyttsx3 as p
import speech_recognition as sr
import webbrowser as wb

jerry = p.init('sapi5')
voices = jerry.getProperty('voices')
jerry.setProperty('voices', voices[0].id)
jerry.setProperty("rate", 173)

def Speak(audio) :
    jerry.say(audio)
    jerry.runAndWait()

def Listen() :
    command = sr.Recognizer()
    with sr.Microphone() as source :
        print("Listening...!")
        command.pause_threshold = 1
        audio = command.listen(source)
        
        try :
            print("\nRecognizing...!")
            print("It may take some time.")
            query = command.recognize_google(audio, language='en-in')
            print(f"\nYou said : {query}")
        except Exception as e :
            return "none"
            
        return query.lower()

print("\nSay 'wake up jerry' after 'Listening...' to start this virtual assistant\n")
while True :
    query = Listen()
    if "wake up" in query or "jerry" == query :
        Speak("yes boss, i am awake, Jerry one point o reporting in your service boss, how are you.")
    elif "how are you" in query :
        Speak("i am fine sir, what about you")
    elif "fine" in query or "good" in query or "great" in query :
        Speak("it's good to know that you are fine.")
    elif "help" in query or "favour" in query :
        Speak("Yes boss, how may i help you.")
    elif "i am sad" in query or "not fine" in query or "not good" in query or "not well" in query :
        Speak("It's ok boss, sometime situation becomes worst but we have to be strong, so be positive and face your all problems with smile.")
    elif "thank you" in query :
        Speak("your welcome sir, i am glad that you are happy with my service")
    elif "made you" in query or "created you" in query or "your creater" in query :
        Speak("I was created by Mister Prajwal Sharma and Mister Ayush Rana.")
    elif "your name" in query :
        Speak("My name is jerry one point o, I am a virtual assistant.")
    # start elif from here
    elif "open google" in query :
        Speak("Opening google")
        wb.open('www.google.com')
    elif "exit" in query :
        Speak("Thanks boss for your time, Closing me, three, two, one, bye boss.")
        exit()