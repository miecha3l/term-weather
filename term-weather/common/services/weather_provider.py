import requests
from common.models.weather import Weather

class WeatherProvider:
  def __init__(self, config):
    self.apiKey = config['apiKey']
    self.location = config['location']
    self.apiUrl = 'https://api.openweathermap.org/data/2.5/weather'

  def getCurrentWeather(self):
    reqUrl = f'{self.apiUrl}?q={self.location}&appid={self.apiKey}'
    res = requests.get(reqUrl)
    return Weather(res.json())

    
