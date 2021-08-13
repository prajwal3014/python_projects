import Jerry
import os

while True :

    print("\nSay hello Jerry after 'Listening...' to start this virtual assistant\n")

    query = Jerry.Listen()

    if query == "hello jerry" :
        Jerry.Speak("Hello sir, I am a Virtual assistant.")
        Jerry.Speak("may i know who are you")
    elif "prajwal" in query :
        Jerry.Speak("welcome boss, How are you")
    elif "prajwal's" in query :
        Jerry.Speak("welcome sir, how are you")
    elif "fine" in query or "good" in query or "great" in query :
        Jerry.Speak("It's good to know that you are fine")
        Jerry.Speak("How may I help you")
    elif "small sister" in query or "small sisters" in query :
        Jerry.Speak("your small sister name is Mahi sharma, she is very cute.")
    elif "mother" in query :
        Jerry.Speak("your mother name is kalpana sharma")
    elif "father" in query :
        Jerry.Speak("your father name is yadab sharma")
    elif "made you" in query or "created you" in query :
        Jerry.Speak("I was created by Mister Prajwal Sharma.")
    elif "your name" in query :
        Jerry.Speak("My name is jerry one point o, a virtual assistant.")
    elif "open google" in query :
        Jerry.Speak("Opening google just for you boss")
        os.system("C:\Program Files\Google\Chrome\Application\chrome.exe")
        break
    elif "thank you" in query :
        Jerry.Speak("your welcome sir, i am glad that you are happy with my service")
    elif "exit" in query :
        Jerry.Speak("Thank you for your time sir.")
        break