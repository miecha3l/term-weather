class Weather:
  def __init__(self, real, feel, main, desc):
    self.real = int(real - 273.15)
    self.feel = int(feel - 273.15)
    self.main = main
    self.desc = desc
    self.icon = getWeatherIcon(self.main)

  def toString(self):
    return f'{self.desc} {self.icon} {self.real}°C'


def getWeatherIcon(name):
  if name == 'Clouds': return '☁'
  if name == 'Clear': return '☀'
  if name == 'Rain': return '🌧'
  if name == 'Thunderstorm': return '⛈'
  if name == 'Drizzle': return '🌦'
  else: return ''

