import speech_recognition as sr
import pywhatkit

# Initialize the speech recognizer
r = sr.Recognizer()

# Define the function that sends a WhatsApp message
def send_whatsapp_message(message, recipient):
    pywhatkit.sendwhatmsg_instantly(recipient, message)

# Define the address book
address_book = {
    "Nikhila": "+917982104155",
    "Sreehari": "+919623763978",
    "Jisha": "+919447102990",
    "Anil sir": "+919447477577",
    "Anju miss": "+919605216106",
    "HOD": "+919487274466"
}

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

        # If the voice command is 'send message'
        if 'send message' in command:
            # Ask for the message to send and the recipient
            print("What message do you want to send?")
            with sr.Microphone() as source:
                audio = r.listen(source)
                message = r.recognize_google(audio)

            # Ask for the recipient's name
            print("To whom you want to send message?")
            with sr.Microphone() as source:
                audio = r.listen(source)
                recipient_name = r.recognize_google(audio)

            # Look up the recipient's phone number in the address book
            recipient_number = address_book.get(recipient_name)

            # If the recipient is not in the address book, prompt the user to enter the phone number
            if not recipient_number:
                print(f"{recipient_name} is not in your address book.")
                print("Please enter the recipient's phone number:")
                recipient_number = input()

            send_whatsapp_message(message, recipient_number)
            print("Message sent!")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

# Start listening for the voice command
while True:
    listen_for_command()
