import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os

listener = sr.Recognizer()
engine = pyttsx3.init(driverName='espeak')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            audio = listener.listen(source)
            command = listener.recognize_google(audio)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except sr.UnknownValueError:
        pass
    except sr.RequestError:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('Playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'are you single' in command:
        talk('I am in a relationship with Wi-Fi')
    elif 'date' in command:
        talk('Sorry, I have a headache')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'search' in command:
        query = command.replace('search', '')
        talk('Searching for ' + query)
        pywhatkit.search(query)
    elif 'open' in command:
        app = command.replace('open', '')
        talk('Opening ' + app)
        os.system(f'open {app}')
    elif 'shutdown' in command:
        talk('Shutting down the system')
        os.system('shutdown now')
    elif 'restart' in command:
        talk('Restarting the system')
        os.system('restart now')
    elif 'generate code' in command:
        prompt = command.replace('generate code', '')
        code = generate_code(prompt)
        talk('Here is the generated code:')
        talk(code)
    else:
        talk('Please say the command again.')

while True:
    run_alexa()
