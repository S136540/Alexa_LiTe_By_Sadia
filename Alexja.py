import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import smtplib
import pywhatkit
import pyjokes

# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


# Define function for virtual assistant to speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# Define function for virtual assistant to wish user
def wish_me():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("hi i am your  alexa lite. how can i assist you?")


# Define function to take user input
def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Sorry, I did not understand that. Could you please repeat?")
        return "None"
    return query

def send_email():
    speak("Please provide the recipient's email address.")
    receiver_email = input("Recipient's email: ")
    speak("What should be the subject of the email?")
    subject = input("Subject: ")
    speak("What should be the body of the email?")
    body = input("Body: ")

    sender_email = "1801017@iot.bdu.ac.bd"
    password = "Upom@1801017"

    # Create SMTP session
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)

    # Compose email message
    message = f"Subject: {subject}\n\n{body}"

    # Send email
    server.sendmail(sender_email, receiver_email, message)

    # Close SMTP session
    server.quit()
    speak("Email has been sent!")



# Define function for virtual assistant to send a WhatsApp message
def send_whatsapp_message():
    speak("Please provide the phone number of the recipient.")
    phone_number = input("Recipient's phone number (with country code, without '+' sign): ")
    speak("What should be the message?")
    message = input("Message: ")

    # Send WhatsApp message
    pywhatkit.sendwhatmsg(f"+{phone_number}", message, datetime.datetime.now().hour, datetime.datetime.now().minute + 1)
    speak("WhatsApp message has been sent!")





if __name__ == "__main__":
    wish_me()

    while True:
        query = take_command().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Opening YouTube")
            webbrowser.open("youtube.com")
        elif 'youtube' in query:
            song = query.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)

        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("google.com")

        elif 'search' in query:
            speak('What do you want me to search for?')
            search_query = take_command().lower()
            pywhatkit.search(search_query)
            speak(f"Here are the search results for {search_query}")


        elif 'current time and date' in query:
            str_time = datetime.datetime.now().strftime('%I:%M:%p,%B:%d:%Y')
            speak(f"The current time with the date  is {str_time}")


        elif "let's hangout" in query:
            speak('Oh sorry! I have Artificial Intelligence Lab Final Exam Today')

        elif "here is our teachers" in query:
            speak('Assalamualikum Habib sir and Nipa maam')


        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'send email' in query:
            send_email()

        elif 'send whatsapp message' in query:
            send_whatsapp_message()

        elif 'bye alexa' in query:
            speak("Goodbye!")
            break
