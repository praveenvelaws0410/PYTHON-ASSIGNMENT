

from urllib import request


def get_weather(city):
    api_key = "c8d0454ffe0ea7501f39f77be344b69d"  
    url = f"https://home.openweathermap.org/api_keysq={city}&appid={api_key}&units=metric"
    
    response = request.get(url)
    data = response.json()
    
    if response.status_code == 200:
        # Extract relevant weather information
        weather = {
            "description": data["weather"][0]["description"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
        }
        return weather
    else:
        return None

def main():
    city = input("Enter the name of a city: ")
    weather = get_weather(city)
    
    if weather:
        print(f"Weather in {city}:")
        print(f"Description: {weather['description']}")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Wind Speed: {weather['wind_speed']} m/s")
    else:
        print("Weather information not available. Please check the city name or try again later.")

if __name__ == "__main__":
    main()

