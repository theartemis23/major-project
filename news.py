import speech_recognition as sr
import pyttsx3
import requests
import json

# Initialize the speech recognizer and voice engine
r = sr.Recognizer()
engine = pyttsx3.init()

# Set the News API URL and parameters
url = 'https://newsapi.org/v2/top-headlines'
api_key = 'dfdbff5f890f4e58b7ebb4edae712d8b'

# Set the voice engine configuration
engine.setProperty('rate', 140)  # set the voice speed to 70% of the default

# Function to fetch and read out the news articles
def read_news_articles(num_articles):
    # Set the parameters for the News API request
    parameters = {'country': 'in', 'apiKey': api_key, 'pageSize': num_articles}
    
    # Make the request to the News API and parse the response
    response = requests.get(url, params=parameters)
    news_data = json.loads(response.text)
    articles = news_data['articles']
    
    # Read out the news article titles using the voice engine
    for i, article in enumerate(articles):
        title = article['title']
        print(f"News {i+1}: {title}")
        engine.say(title)
    
    engine.runAndWait()

# Main loop to listen for voice commands
while True:
    try:
        with sr.Microphone() as source:
            print("Listening...")
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)
        
        # Convert the voice command to text using Google Speech Recognition
        command = r.recognize_google(audio)
        print(f"Command: {command}")
        
        # Check if the command contains a number
        num_articles = None
        for word in command.split():
            if word.isdigit():
                num_articles = int(word)
                break
        
        # If a number is found, read out that many news articles
        if num_articles:
            read_news_articles(num_articles)
        else:
            print("Please specify a number of articles.")
        
    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service: {e}")