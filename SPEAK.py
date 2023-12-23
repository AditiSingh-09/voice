import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import requests
from bs4 import BeautifulSoup
from playsound import playsound
import datefinder
import winsound
import calendar


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[1].id)

def speak(audio): #defines functions with proper argumentss to use again and again.also can add return value to save in a variable
    engine.say(audio)
    engine.runAndWait()

def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<15:
        speak("Good afternoon!")
    elif hour>=15 and hour<=20:
        speak("Good Evening!")

    speak("Hello! I am your assisant  Zira How may I help you?")

def Alarm(audio):
        date = datefinder.find_dates(audio)
        for mat in date:
            print (mat)
            
            string= str(mat)
            time = string[11:]
            hour= time[:-6]
            hour=int(hour)
            minute= time[3:-3]
            minute= int(minute)
            speak(f"Setting an alarm for {hour} hours and {minute}minutes")
        while True:
            if hour== datetime.datetime.now().hour:
                if minute== datetime.datetime.now().minute:
                    winsound.PlaySound("alarm2.wav",winsound.SND_FILENAME)
                   
                
                    

def TakeCommand():
    """It takes microphone input from the user and returns string output"""

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1.2
        audio=r.listen(source)
    try:
        print("Recognizing\n")
        query = r.recognize_google(audio, language='en-us')
        print(f"User said:{query}\n")
    
    except Exception as e:
        print("Say that again please...\n")  
        return "None"
    return query   

        
if __name__== "__main__": 
    WishMe()
    
    X=0
    while X==0:

        query = TakeCommand().lower()
        

        if 'what can you do' in query:
            speak("You can say- Open Youtube  or  What's the weather today?")

        elif " weather " in query:
            city="New Delhi"
            url = "https://www.google.com/search?q="+"weather"+city
            html = requests.get(url).content
            soup = BeautifulSoup(html, 'html.parser')
            temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
            speak(f"It is {temp} right now outside.")
            
        elif ("hey" or "hello" or "hi") in query:
            speak("Hello. Good to hear from you")

        elif "know me" in query:
            speak("Yes,Of course. Your name is Aditi.")
            print("Yes,Of course. You name is Aditi.")

        elif "how are you" in query:
            speak("Better than you!")
            print("Better than you!")

        elif "your name"in query:
            speak("My name is Zira, here to help you.")
            print("My name is Zira.")

        elif "who are you" in query:
            speak("I am your virtual assistant Zira, how can I help you?")
            print("I am your virtual assistant Zira.")

        
        elif "time" in query:
            Time = datetime.datetime.now().strftime("%H:%M:%S")   
            speak(f"Right now it is {Time}")
        
        elif "day" in query:
            date=datetime.date.today().strftime("%B %d, %Y")
            day= calendar.day_name[datetime.datetime.strptime(date, '%B %d, %Y').weekday()]
            print(day)
            speak("Today is", day)

        elif "date" in query:
            date=datetime.date.today().strftime("%B %d, %Y")
            print(date)
            speak(date)

        elif "calendar" in query:
            num=[]
            x=query.split()
            for i in x:
                if i.isnumeric():
                    num.append(int(i))
            print(calendar.calendar(num[0]))

        elif "not fine" in query:
            speak("What can I do to make up your mood?")

        elif 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            Results=wikipedia.summary(query,sentences=2)
            speak("According to Wikepedia,")
            print(Results)
            speak(Results)
            X=1

        elif 'youtube' in query:
            Ask=speak("What do you want to search?")
            S= TakeCommand().lower()
            Chrome='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(Chrome).open("www.youtube.com/results?search_query="+S)
            X=1

        elif 'google' in query:
            Ask=speak("What do you want to search?")
            S= TakeCommand().lower()
            Chrome='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            speak("Searching" + S + "on Google")
            webbrowser.get(Chrome).open("www.google.com/search?q="+S)
            X=1

        elif "open spotify" in query:
            Spotify="C:\\Users\\Admin\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(Spotify)
            X=1

        elif "where is" in query:
            Chrome='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            query=query.replace("where is","")
            speak(f"User asked to locate {query}")
            webbrowser.open("https://www.google.nl//maps//place//"+query)

        elif (" morning" or "evening" or " afternoon") in query:
            speak(f"A very {query}")
            speak("I hope you're having fun today")

        elif "night" in query:
            speak("Good Night. See you later.")
            X=1

       

        elif "bye" in query:
            speak("See you, Had a great time talking to you! ")
            exit()



        elif "alarm" in query:
        
            '''print("Say- For example-Set an alarm for 3:55 pm")
            speak("Say- For example-Set an alarm for 3:55 pm")'''
            Alarm(query)
            speak("Setting an alarm for")
            
            
                        



