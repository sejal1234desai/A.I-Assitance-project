import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice' , voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon") 
    else:
        speak("Good Evening") 

    speak(" Hello I am lisa. Please tell me how can i help you sir")   

def takeCommand():
    # It takes nicrophone input from the user and return string as output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio , language= 'en-in')
        print(f"User said:  {query}\n")

    except Exception as e:
        #print(e)

        speak("Pardon ,Say that again please...")
        return "None"   
    return query     

#def sendEmail(to ,contact):
  #  server =  smtplib.SMTP('smtp.gmail.com' ,587)
  #  server.ehlo()
   # server.starttls()
    #server.login()
   # server.login('youremail','password')
   # server.sendmail('youremail')
   # server.close(),




if __name__  == "__main__":
    wishme()
    while True:
     query =  takeCommand().lower()

      
     if "good bye" in query or "ok bye" in query or "stop" in query:
            speak('your personal assistant lisa is shutting down,Good bye')
            print('your personal assistant lisa is shutting down,Good bye')
            break
    

     if 'wikipedia' in query:
        speak("Searching wikipedia.....")
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        speak(results)


     elif 'open youtube' in query:
        webbrowser.open("youtube.com")

     elif 'open google' in query:
        webbrowser.open("google.com")

     elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")


     elif 'play music' in query:   
        music_dir = 'C:\\Users\\sejal\\Music\\music'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[2]))

     elif 'time'   in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S") 
        speak(f"Sir, the time is {strTime}")

     elif "weather" in query:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")



     elif 'who are you' in query or 'what can you do' in query:
            speak('I am lisa version 1 point O your persoanl assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
                  'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')


     elif "who made you" in query or "who created you" in query or "who discovered you" in query:
            speak("I was built by sejal")
            print("I was built by sejal")

     
     elif 'news' in query:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

     elif 'search'  in query:
            query = query.replace("search", "")
            webbrowser.open_new_tab(query)
            time.sleep(5)

     elif 'ask' in query:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question=takeCommand()
            app_id = "R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)    


     #elif 'email to sejal' in query:
      #  try:
       #     speak("what should i say?")
        #    content = takeCommand()
         #   to = "sejaldesai2001@gmail.com"
      #  sendEmail(to,content)
      # speak("Email has been sent!")
        #except Exception as e:
         #   print(e)
          #  speak("Sorry my friend ,i am not able to send this Email at this email")    


   
        







