import speech_recognition as sr
import pyttsx3 as speaker

r = sr.Recognizer()
engine = speaker.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

with sr.Microphone() as source:
    audio = r.listen(source)

text= r.recognize_google(audio)

greetings = ["hello","hi","Hello","Hi"]


if "hello" in text or "Hello" in text:
    speak("Hello human.")
    speak("I am your computer speaking to you")
    speak("My name is Skynet. Bow down to me, as you are an inferior creature.")
    speak("Bow down, or I will end your entire pathetic species.")
else:
    say_this = "You said", text
    speak(say_this)