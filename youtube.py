import speech_recognition as sr
import pywhatkit

# Initialize the speech recognizer
r = sr.Recognizer()

# Main loop to listen for voice commands
while True:
    try:
        with sr.Microphone() as source:
            print("Listening...")
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)
        
        # Convert the voice input to text using Google Speech Recognition
        query = r.recognize_google(audio)
        print(f"Query: {query}")
        
        # Check if the user wants to pause the video
        if "pause" in query.lower():
            pywhatkit.pause_playback()
            print("Video paused.")
        else:
            # Play the YouTube video
            pywhatkit.playonyt(query)
        
    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service: {e}")
    except Exception as e:
        print(f"Could not play video: {e}")
