from email import message
from subprocess import TimeoutExpired
from urllib import request
from weakref import ProxyTypes
# from subprocess import TimeoutExpired
# from urllib import request
# from weakref import ProxyTypes
import pyttsx3 # text data into speech
import datetime # date and time
import speech_recognition as sr # speech from mic to text
rate = engine.getProperty("rate")
    engine.setProperty("rate",190)
    if voice ==1: # male
        engine.setProperty("voice",voices[0].id)
        engine.setProperty("voice",voices[1].id)
        speak("hello , this is jarvis")
    if voice ==2: # female
        engine.setProperty("voice", voices[1].id)
        engine.setProperty("voice", voices[0].id)
        speak("hello , this is friday")
      try :
                    speak("searching...")
                    query = query.replace("wikipedia","") #replacing with empty string
                    result = wikipedia.summary(query,sentences = 4) # read 4 sentences
                    result = wikipedia.summary(query,sentences = 2) # read 4 sentences
                    print(result)
                    speak(result)
