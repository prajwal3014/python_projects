import Jerry
import webbrowser as wb

print("\nSay 'wake up jerry' after 'Listening...' to start this virtual assistant\n")
while True :
    query = Jerry.Listen()
    
    if "wake up" in query :
        Jerry.Speak("yes boss, i am awake, Jerry one point o reporting in your service boss.")
    elif "good morning" in query :
        Jerry.Speak("good morning boss, how are you")
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

# a={
#     "wake up jerry" : "yes boss, i am awake, Jerry one point o reporting in your service boss.",
#     "good morning" : "good morning boss, how are you",
#     "how are you" : "I am fine sir, what about you",
#     "fine" : "It's good to know that you are fine. How may I help you",
#     "good" : "It's good to know that you are fine. How may I help you",
#     "great" : "It's good to know that you are fine. How may I help you",
#     "help" : "yes boss, how may i help you.",
#     "small sister" : "your small sister name is Mahi sharma, she is very cute.",
#     "small sisters" : "your small sister name is Mahi sharma, she is very cute.",
#     "mother" : "your mother name is kalpana sharma",
#     "father" : "your father name is yadab sharma",
#     "made you" : "I was created by Mister Prajwal Sharma.",
#     "created you" : "I was created by Mister Prajwal Sharma.",
#     "your name" : "My name is jerry one point o, a virtual assistant.",
#     "thank you" : "your welcome sir, i am glad that you are happy with my service",
#     "exit" : "Thank you for your time sir, going again for sleep. have a good day sir"
# }