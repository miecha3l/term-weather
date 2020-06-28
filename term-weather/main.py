import common.services.config as cfg
from common.services.weather_provider import WeatherProvider

config = cfg.load()
wp = WeatherProvider(config)

data = wp.fetchWeather()