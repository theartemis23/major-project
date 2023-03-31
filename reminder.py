import speech_recognition as sr
import time
import datetime
import pyttsx3

# Initialize the speech recognizer
r = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Define the function that creates a reminder and sets an alarm
def set_reminder(reminder_text, alarm_time):
    # Get the current time
    now = datetime.datetime.now()

    # Calculate the time delta until the alarm time
    time_delta = datetime.datetime.strptime(alarm_time,"%I:%M %P") - now

    # Calculate the total seconds until the alarm time
    total_seconds = time_delta.total_seconds()

    # Sleep until the alarm time
    time.sleep(total_seconds)
     # Speak the reminder text aloud
    engine.say(reminder_text)
    engine.runAndWait()

    # Send confirmation text
    confirmation_text = f"Reminder set for {alarm_time} to {reminder_text}"
    print(confirmation_text)


# Define the function that listens for the voice command
def listen_for_command():
    with sr.Microphone() as source:
        print("Say something!")
        r.adjust_for_ambient_noise(source)  # Optional: adjust for ambient noise

        audio = r.listen(source)

    try:
        # Use the Google Speech Recognition API to transcribe the audio
        command = r.recognize_google(audio)
        print("Google Speech Recognition thinks you said " + command)

        # If the voice command is 'set reminder'
        if 'set reminder' in command:
            # Ask for the reminder text and the alarm time
            print("What do you want to be reminded of?")
            with sr.Microphone() as source:
                audio = r.listen(source)
                reminder_text = r.recognize_google(audio)

            print("When do you want to be reminded?")
            with sr.Microphone() as source:
                audio = r.listen(source)
                alarm_time = r.recognize_google(audio)

            # Set the reminder and alarm
            set_reminder(reminder_text, alarm_time)

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

# Start listening for the voice command
while True:
    listen_for_command()
