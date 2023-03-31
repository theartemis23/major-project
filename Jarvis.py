from Body.Speak import Speak
from Body.Listen import Listen

def MainExe():

    while True:

        query = Listen()

        if "hello" in query:
            Speak("Hi! I am CYBORG!")

        elif "bye" in query:
            Speak("Have a good day!")