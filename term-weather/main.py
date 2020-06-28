import common.services.weather_provider as wp
from common.models.weather import Weather 

w = Weather(wp.getWeatherForCity('Szczecin'))
print(w.toString())