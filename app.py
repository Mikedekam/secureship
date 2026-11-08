from config import WEATHER_API_KEY, CITY


def get_weather(city):
    # A real app would send WEATHER_API_KEY to a weather service here.
    if not WEATHER_API_KEY:
        return "Error: WEATHER_API_KEY is not set."
    return f"Weather for {city}: 31C and sunny (demo data)"


if __name__ == "__main__":
    print(get_weather(CITY))
