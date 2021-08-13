import pyttsx3 as p
import speech_recognition as sr

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