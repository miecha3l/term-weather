import common.services.weather_provider as wp

class Weather:
  def __init__(self, json):
    self.real = int(json['main']['temp'] - 273.15)
    self.feel = int(json['main']['feels_like'] - 273.15)
    self.main = json['weather'][0]['main']
    self.desc = json['weather'][0]['description']

  def toString(self):
    return f'It is {self.feel}°C {wp.getWeatherIcon(self.main)}\n{self.desc}'




