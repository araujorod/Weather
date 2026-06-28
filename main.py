# from src.extract_data import extract_weather_data
# from src.extract_data_2 import extract_weather_data
# from src.load_data import load_weather_data
# from src.transform_data import data_transformations

from extract_data import extract_weather_data

# from extract_data_2 import extract_weather_data
from load_data import load_weather_data
from transform_data import data_transformations

import os
from pathlib import Path
from dotenv import load_dotenv

import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

env_path = Path(__file__).resolve().parent.parent / "config" / ".env"
load_dotenv(env_path)

API_KEY = os.getenv("api_key")

url = f"https://api.openweathermap.org/data/2.5/weather?q=Sao Paulo,BR&units=metric&appid={API_KEY}"
