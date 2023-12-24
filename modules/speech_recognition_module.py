import speech_recognition as sr
import pyttsx3

def get_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that.")
        return None
    except sr.RequestError as e:
        print(f"Error connecting to Google Speech Recognition service: {e}")
        return None

def speak(text, voice='Quill'):
    engine = pyttsx3.init()

    # Set the voice based on the user command
    if voice == 'Navi':
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)  # Index 1 is usually a female voice, but it may vary

    engine.say(text)
    engine.runAndWait()

    return engine  # Return the engine to use in the main script
