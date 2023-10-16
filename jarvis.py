import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

#defining the speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#defining the Wish me function
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif  hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Hey! I am JARVIS. How may I help you?")

#defining the take command function
def takeCommand():
    #It takes microphone input from the user and returns string output.
    r=sr.Recognizer()
    with sr.Microphone as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,Language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Pardon please...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    if 1:
        query = takeCommand().lower()
        #Logic for executing tasks based on query

        #task 1: search something on wikipedia
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query=query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        #task 2: open youtube
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        #task 3: tell time
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is: {strTime}")
        