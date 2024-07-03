import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    instruct = ""  # Initialize instruct to an empty string
    try:
        with sr.Microphone() as data_taker:
            print("Say something...")
            voice = listener.listen(data_taker)
            instruct = listener.recognize_google(voice)
            instruct = instruct.lower()
            if 'max' in instruct:
                instruct = instruct.replace('max', '')
                print(instruct)
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
    except sr.RequestError:
        print("Could not request results; check your network connection.")
    except Exception as e:
        print(f"Error: {e}")
    return instruct

def run_max():
    instruct = take_command()
    if 'play' in instruct:
        song = instruct.replace('play', '').strip()
        talk('playing ' + song)
        print('Playing:', song)
        try:
            pywhatkit.playonyt(song)
        except Exception as e:
            print(f"Error playing song: {e}")
            talk("Sorry, I could not play the song.")
    elif 'time' in instruct:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        print(current_time)
        talk('current time is ' + current_time)
    elif 'tell me about' in instruct:
        thing = instruct.replace('tell me about', '').strip()
        info = wikipedia.summary(thing, sentences=4)
        print(info)
        talk(info)
    elif 'mail' in instruct:
        print("mail")
    elif 'who are you' in instruct:
        talk('I am your personal assistant Max')
    elif 'what can you do for me' in instruct:
        talk('I can play songs, tell time, and help you search Wikipedia')
    else:
        talk('I did not understand, can you repeat that?')

while True:
    run_max()
