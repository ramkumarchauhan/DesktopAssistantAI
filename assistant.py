from modules import applications, internet_search, datetime, music, math_operations, system_control
from modules.speech_recognition_module import get_command, speak
from modules.weather import get_weather
from modules.email import open_email_in_browser
import pyautogui

def main():
    current_voice = 'Quill'

    # Initial greeting based on the selected voice
    initial_greeting = "Hello sir, I'm Quill! How can I assist you today?"
    speak(initial_greeting, voice=current_voice)

    while True:
        command = get_command()

        if command:
            if 'open' in command:
                app_name = command.split(' ', 1)[1]
                applications.open_application(app_name)
                speak(f"Opening {app_name}")
            elif 'close' in command:
                app_name = command.split(' ', 1)[1]
                applications.close_application(app_name)
                speak(f"Closing {app_name}")
            elif 'search' in command:
                query = command.split(' ', 1)[1]
                internet_search.search_web(query)
            elif 'youtube' in command:
                query = command.split(' ', 1)[1]
                internet_search.search_web(query, search_engine='youtube')
            elif 'wikipedia' in command:
                query = command.split(' ', 1)[1]
                internet_search.search_web(query, search_engine='wikipedia')
            elif 'weather' in command or 'tell me the weather' in command or 'how is the weather' in command or 'how is the weather right now' in command or 'what is the weather' in command or 'what is the weather right now' in command or "what about today's weather" in command:
                city = command.split(' ', 1)[1]
                get_weather(city, current_voice)
            elif 'date' in command or 'time' in command:
                datetime.get_date_time()
            elif 'open email' in command:
                open_email_in_browser()
                engine = speak("Opening your email in the browser.", voice=current_voice)
            elif 'play music' in command:
                music.play_music()
            elif 'stop music' in command:
                music.stop_music()
            elif 'solve' in command:
                problem = command.split(' ', 1)[1]
                math_operations.solve_math_problem(problem)
            elif 'restart' in command or 'shutdown' in command or 'sleep' in command:
                system_control.system_control(command)
            elif 'change voice' in command:
                current_voice = 'Navi' if current_voice == 'Quill' else 'Quill'
                confirmation_message = f"Do you want to set {current_voice} voice as the default voice?"
                speak(confirmation_message, voice=current_voice)
                confirmation_command = get_command()
                if confirmation_command and ('yes' in confirmation_command or 'ok' in confirmation_command):
                    # Save the chosen voice as the default voice
                    engine.setProperty('voice', engine.getProperty('voices')[1].id)
                    speak(f"{current_voice.capitalize()} voice set as the default voice.")
                else:
                    speak("Voice change canceled.")
            elif 'split windows' in command:
                # Ask the user where to place the window
                engine = speak("Where would you like to place the window? Left or right?", voice=current_voice)
                response_command = get_command()

                if response_command and ('left' in response_command or 'right' in response_command):
                    # Simulate keyboard shortcut based on user's response
                    if 'left' in response_command:
                        pyautogui.hotkey('winleft', 'left')  # Adjust the keys as needed
                    else:
                        pyautogui.hotkey('winleft', 'right')  # Adjust the keys as needed

                    engine = speak("Splitting windows.", voice=current_voice)
                else:
                    engine = speak("Sorry sir, unable to split right now. Cancelling window splitting command.", voice=current_voice)
            elif 'exit' in command or 'bye' in command:
                speak("Goodbye sir! Hope to see you soon.")
                break
            else:
                speak("Sorry sir, I don't understand that command. Can you please repeat?")

if __name__ == "__main__":
    main()
