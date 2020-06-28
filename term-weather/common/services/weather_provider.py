import requests


def getWeatherForCity(cityName):
  apiKey = 'f0a930a15fadfa174f7dc45d4b736537'
  url = f'https://api.openweathermap.org/data/2.5/weather?q={cityName},PL&appid={apiKey}'
  res = requests.get(url)
  return res.json()

def getWeatherIcon(name):
  if name == 'Clouds': return '☁'
  if name == 'Clear': return '☀'
  if name == 'Rain': return '🌧'
  if name == 'Thunderstorm': return '⛈'
  if name == 'Drizzle': return '🌦'
  else: return ''