import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pywhatkit
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning!")
    elif hour >= 12 and hour < 18:
        speak("good afternoon!")
    else:
        speak("good evening")
    speak("I am kiba ,Your Personal Assistant. Please tell me how may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        print("repeat again...")
        return "None"
    return query

if __name__ == "__main__":

    wishMe()
    while True:
        query = takeCommand().lower()

        if 'who is' in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif 'single' in query:
            speak('sorry , but i am taken')

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'open youtube' in query:
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            webbrowser.open('www.google.co.in')

        elif 'play music' in query:
            music_dir = "C:\\Users\\Puja Agrawal\\Music"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'play' in query:
            song = takeCommand()
            speak('playing ' + song)
            pywhatkit.playonyt(song)

        elif 'time' in query:
            strtime = datetime.datetime.now().strftime("%I:%M:%p")
            print(strtime)
            speak(f"sir , the current time is {strtime}")

        elif 'open chrome' in query:
            chromePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome.lnk"
            os.startfile(chromePath)

        elif 'open brave' in query:
            bravePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Brave.lnk"
            os.startfile(bravePath)

        elif 'open powerpoint' in query:
            powerpointPath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint.lnk"
            os.startfile(powerpointPath)

        elif 'exit' in query:
            exit()