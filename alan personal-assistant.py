import sys
import pyttsx3 as pytts
import speech_recognition as sr_rec
import webbrowser
import subprocess
import os
from datetime import datetime


# Text-to-Speech (TTS) Function
def er_tts(text):
    engine = pytts.init()
    engine.say(text)
    engine.runAndWait()

def er_print(message):
    print(message)

# Speech Recognition Function
def takeCommand():
    r = sr_rec.Recognizer()
    with sr_rec.Microphone() as source:
        r.pause_threshold = 0.6
        print("Listening...")
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
        return query
    except sr_rec.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return "Some error occurred. Sorry."
    except sr_rec.RequestError as e:
        print(f"Could not request results; {e}")
        return "Some error occurred. Sorry."

if __name__ == '__main__':
    # Greeting
    er_tts("Hello, I am Alan, your personal assistant.")
    query = takeCommand()

    # Sites to open
    sites = [["youtube", "https://www.youtube.com"],
             ["wiki", "https://www.wikipedia.org"],
             ["instagram", "https://www.instagram.com"],
             ["linkedin", "https://www.linkedin.com"]]

    # Process Query
    for site in sites:
        if f"open {site[0]}".lower() in query.lower():
            er_tts(f"Opening {site[0]} da")
            webbrowser.open(site[1])

    if "what is name" in query:
        er_tts("I am Alan, your personal assistant.")

    if "music" in query:
        music_path = "H:\swethan\python\music\Va Pada Pada Enthan Kannamma - Masstamilan.mp3"
        # Use the os.system method to open the music file
        os.system(f'explorer "{music_path}"')
    if "date and time" in query:
        current_time = datetime.now()
        er_tts(f"Year: {current_time.year}")
        er_tts(f"Month: {current_time.month}")
        er_tts(f"Day: {current_time.day}")
        er_tts(f"Hour: {current_time.hour}")
        er_tts(f"Minute: {current_time.minute}")
        er_tts(f"Second: {current_time.second}")
    if "who is your owner" in query:
        er_tts("It looks like you're asking about the origins of AI like me. I was developed by Swethan and OpenAI, an artificial intelligence. "
               "The development of AI models like me involves contributions from many researchers and engineers over several years, focusing on machine learning,"
               " natural language processing, and other related fields.")
