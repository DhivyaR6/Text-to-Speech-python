import pyttsx3
from pyttsx3 import engine
engine = pyttsx3.init() 
voices = engine.getProperty("voices")
voices = engine.setProperty("voice",voices[1].id)

text = input("Enter your text:")

def speek(text):
    engine.say(text)
    engine.runAndWait()
speek(text)