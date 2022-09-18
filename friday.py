import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import random

# contacts = {'Ankit':'ankitbhansingh2020@gmail.com','Manish':'mawatwalmanish1997@gmail.com','lekhraj':'lekhrajsaini1403@gmail.com'}

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good morning')
    elif hour>=12 and hour<18:
        speak('Good Afternoon')
    else:
        speak('Good Evening')
    speak("Friday at you service sir")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        audio = r.listen(source)
    
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language = 'en-in')
        print(f'User said:{query}\n')
    except Exception as e:
        print('Please repeat...')
        return 'None'
    return query

if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()
        #logic for executing task
        if 'wikipedia' in query:
            speak('Searching in wikipedia...')
            query = query.replace('wikipedia','')
            results = wikipedia.summary(query, sentences = 2)
            speak('According to wikipedia')
            speak(results)
        elif 'visit' in query:
            query = query.replace('visit ','')
            query = query+'.com'
            webbrowser.open(query)
        elif 'play music' in query:
            music_dir = 'E:\\songs'
            songs = os.listdir(music_dir)
            n = len(songs)
            r = random.randint(0,n-1)
            os.startfile(os.path.join(music_dir, songs[r]))
        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime('%H hours %M minutes %S seconds')
            speak(f'Sir, the time is {strtime}')
        elif 'goodbye' in query:
            break
        