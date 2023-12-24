from modules.speech_recognition_module import speak
import requests

# Replace 'YOUR_OPENWEATHERMAP_API_KEY' with your actual API key
OPENWEATHERMAP_API_KEY = 'c731c17ce68fa3da70ffb93637d4e423'

def get_weather(city, current_voice):
    try:
        # Make a request to OpenWeatherMap API
        api_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHERMAP_API_KEY}'
        response = requests.get(api_url)
        data = response.json()

        # Extract relevant weather information
        temperature = data['main']['temp']
        description = data['weather'][0]['description']

        # Speak the weather information
        speak(f"The weather in {city} is {description} with a temperature of {temperature} degrees Celsius.", voice=current_voice)
    except Exception as e:
        speak(f"Sorry, I couldn't fetch the weather information for {city}. Please try again later.", voice=current_voice)
