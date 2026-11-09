config.py
import os
from dotenv import load_dotenv
load_dotenv() # copies the values from .env into environment variables
WEATHER_API_KEY = os.environ.get("WEATHER_API_KEY")
CITY = os.environ.get("CITY", "Accra")
