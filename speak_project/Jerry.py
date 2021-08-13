import pyttsx3 as p
import speech_recognition as sr

jerry = p.init('sapi5')
voices = jerry.getProperty('voices')
jerry.setProperty('voices', voices[0].id)
jerry.setProperty("rate", 175)


def speak_jerry(audio) :
    jerry.say(audio)
    jerry.runAndWait()

def listen_jerry() :
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

# while True :

#     print("\nSay hello Jerry after 'Listening...' to start this virtual assistant\n")

#     query = listen_jerry()

#     if query == "hello jerry" :
#         speak_jerry("Hello sir, I am a Virtual assistant.")
#         speak_jerry("may i know who are you")
#     elif "prajwal" in query :
#         speak_jerry("welcome boss, How are you")
#     elif "prajwal's" in query :
#         speak_jerry("welcome sir, how are you")
#     elif "fine" in query or "good" in query or "great" in query :
#         speak_jerry("It's good to know that you are fine")
#         speak_jerry("How may I help you")
#     elif "small sister" in query or "small sisters" in query :
#         speak_jerry("your small sister name is Mahi sharma, she is very cute.")
#     elif "mother" in query :
#         speak_jerry("your mother name is kalpana sharma")
#     elif "father" in query :
#         speak_jerry("your father name is yadab sharma")
#     elif "made you" in query or "created you" in query :
#         speak_jerry("I was created by Mister Prajwal Sharma.")
#     elif "your name" in query :
#         speak_jerry("My name is jerry one point o, a virtual assistant.")
#     elif "open google" in query :
#         speak_jerry("Opening google just for you boss")
#         os.system("C:\Program Files\Google\Chrome\Application\chrome.exe")
#         break
#     elif "thank you" in query :
#         speak_jerry("your welcome sir, i am glad that you are happy with my service")
#     elif "exit" in query :
#         speak_jerry("Thank you for your time sir.")
#         break