import common.services.config as cfg
from common.services.weather_provider import WeatherProvider
import common.services.arguments as ap



config = cfg.load()
args = ap.parse()
wp = WeatherProvider(config)
data = wp.fetchWeather()

def run():
  if args.now:
    currentWeather = data['current'].toString()
    print(currentWeather)
    return

  if args.tommorow:
    tommorowWeather = data['daily'][0].toString()
    print(tommorowWeather)
    return

  if args.daily:
    for day in data['daily']:
      print(day.toString())
    return

if __name__ == '__main__':
  run()