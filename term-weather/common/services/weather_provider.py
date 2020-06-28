import requests
from common.models.weather import Weather

class WeatherProvider:
  def __init__(self, config):
    self.apiKey = config['apiKey']
    self.location = config['location']
    self.apiUrl = config['apiUrl']
  
  def fetchWeather(self):
    lat, lon = self.location['lat'], self.location['lon']
    req = f'{self.apiUrl}?lat={lat}&lon={lon}&exclude=minutely,hourly&appid={self.apiKey}'
    res = requests.get(req)
    data = res.json()

    return {
      'current': Weather(
        data['current']['temp'],
        data['current']['feels_like'],
        data['current']['weather'][0]['main'],
        data['current']['weather'][0]['description']
      ),
      'daily': [
        Weather(
          day['temp']['max'],
          day['feels_like']['day'],
          day['weather'][0]['main'],
          day['weather'][0]['description'] 
        ) for day in data['daily'][1:]
      ]
    }








    
