import pyttsx3 as sr
import speech_recognition as sr_rec
import webbrowser

def er(text):
    engine = sr.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr_rec.Recognizer()
    with sr_rec.Microphone() as source:
        r.pause_threshold = 1
        print("Listening...")
        audio = r.listen(source)
    try:
        query= r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
        return query
    except sr_rec.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return " some error occured.sorry"
    except sr_rec.RequestError as e:
        print(f"Could not request results; {e}")
        return query

if __name__ == '__main__':
    print(er)
    er("Hello, I am alan your personal assistant.")
    query = takeCommand()
    query = "open youtube"


if "open youtube".lower() in query.lower():
    print("Opening YouTube")
    webbrowser.get('C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s').open("https://www.youtube.com")

            #er(query)


