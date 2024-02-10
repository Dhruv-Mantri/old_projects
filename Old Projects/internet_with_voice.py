import speech_recognition as sr
import pyttsx3 as speaker
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

path = "C:\\Users\mandh\Documents\msedgedriver.exe"
engine = speaker.init()

def speak(stuff):
    engine.say(stuff)
    engine.runAndWait()

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say a noun to search up")
    audio = r.listen(source)

try:
    text = r.recognize_google(audio)
except:
    speak("Can. you. speak better.")
    quit()


print(text)

driver = webdriver.Edge(path)
driver.get("https://www.google.com")

search = driver.find_element(By.NAME,"q")
search.send_keys(text)
search.send_keys(Keys.RETURN)

blurb = driver.find_element(By.CLASS_NAME,"kno-rdesc").text

information = str(blurb)
information = information.replace("Description","")
information = information.replace("Wikipedia","")
driver.quit()

print(information)
speak(information)