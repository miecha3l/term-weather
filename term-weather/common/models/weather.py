class Weather:
  def __init__(self, json):
    self.real = int(json['main']['temp'] - 273.15)
    self.feel = int(json['main']['feels_like'] - 273.15)
    self.main = json['weather'][0]['main']
    self.desc = json['weather'][0]['description']
    self.icon = getWeatherIcon(self.main)

  def toString(self):
    return f'{self.desc} {self.icon} {self.feel}°C'


def getWeatherIcon(name):
  if name == 'Clouds': return '☁'
  if name == 'Clear': return '☀'
  if name == 'Rain': return '🌧'
  if name == 'Thunderstorm': return '⛈'
  if name == 'Drizzle': return '🌦'
  else: return ''

