import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening......")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            print("Sorry, my speech service is down.")
            return None

def respond_to_greeting():
    speak("Hello, How can I help you today?")

def tell_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The time is {current_time}")

def tell_date():
    today = datetime.datetime.now().strftime("%A, %B %d, %Y")
    speak(f"Today's date is {today}")

def search_web(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.get().open(url)
    speak(f"Here is what I found for {query} on Google")

def main():
    speak("Starting up the voice assistant.")
    while True:
        command = listen()

        if command is None:
            continue

        if "hello" in command:
            respond_to_greeting()
        elif "time" in command:
            tell_time()
        elif "date" in command:
            tell_date()
        elif "search for" in command:
            query = command.replace("search for", "").strip()
            search_web(query)
        elif "exit" in command or "quit" in command:
            speak("Goodbye!")
            break
        else:
            speak("Sorry,I didn't get that Please try again")

if __name__ == "__main__":
    main()
