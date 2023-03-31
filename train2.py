import requests
import speech_recognition as sr
import pyttsx3
from bs4 import BeautifulSoup

# Initialize the speech recognition and text-to-speech engines
r = sr.Recognizer()
engine = pyttsx3.init()

# Define a function to speak a given text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Define a function to get train details from a train schedule website
def get_train_details(train_name):
    # Send a GET request to the train schedule website
    response = requests.get(f"https://www.railyatri.in/train/{train_name}")

    # Parse the HTML content of the response using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the train details on the webpage
    train_number = soup.find('span', {'class': 'trainNo'}).text.strip()
    train_name = soup.find('h1', {'class': 'trainName'}).text.strip()
    source = soup.find('div', {'class': 'city'}).text.strip()
    destination = soup.find('div', {'class': 'city list-right'}).text.strip()
    departure_time = soup.find('div', {'class': 'time'}).text.strip()
    arrival_time = soup.find('div', {'class': 'time list-right'}).text.strip()

    # Build a string with the train details
    details = f"Train number is {train_number}. Train name is {train_name}. " \
              f"Source station is {source}. Destination station is {destination}. " \
              f"Departure time is {departure_time}. Arrival time is {arrival_time}."

    # Speak the train details
    speak(details)

# Use the microphone as the audio source for speech recognition
with sr.Microphone() as source:
    print("Please say the name of the train:")
    # Listen for the user's input
    audio = r.listen(source)

    try:
        # Recognize the user's speech using Google Speech Recognition
        train_name = r.recognize_google(audio)
        print(f"You said: {train_name}")
        
        # Get the train details and speak them
        get_train_details(train_name)

    except sr.UnknownValueError:
        # Handle speech recognition errors
        speak("Sorry, I did not understand what you said.")

    except sr.RequestError as e:
        # Handle speech recognition errors
        speak(f"Sorry, could not request results from Google Speech Recognition service. Error: {e}")
