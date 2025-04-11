import requests

def get_weather(city):
    api_key = "your_api_key_here"  # Replace with your real API key from OpenWeatherMap or similar service
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        print(f"Current temperature in {city}: {temp}°C")
    else:
        print(f"Failed to get weather data for {city}. Error code: {response.status_code}")

# Example usage
get_weather("Toronto")