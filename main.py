import pyttsx3 as p
import speech_recognition as sr


engine=p.init()
rate=engine.getProperty('rate')
engine.setProperty('rate',200)
print(rate)
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
print(voices)
def speak(text):
    engine.say(text)
    engine.runAndWait()
r=sr.Recognizer() # initialising the recognizer
speak("hello sir , i am your voice assistant how are you")
with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("Listening...")
    audio=r.listen(source)
    text=r.recognize_google(audio)
    print(text)
if "what" and "about" and "you" in text:
    speak("i am also having a good day")
speak("how can i help you")
with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("listening...")
    audio=r.listen(source)
    text2=r.recognize_google(audio)
if "information" in text2:
    speak("you need info of which topic")
with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("Listening...")
    audio=r.listen(source)
    text=r.recognize_google(audio)
speak("searching {} in wikipedia".format(information))
assist=infow()
assist.get_info("stars")
    











