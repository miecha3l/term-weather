import json
import os

default_cfg = {
  'location': {
    'lat': 53.428543,
    'lon': 14.552812
  },
  'apiUrl': 'https://api.openweathermap.org/data/2.5/onecall',
  'apiKey': 'f0a930a15fadfa174f7dc45d4b736537'
}


def load():
  cfg_path = os.path.join(os.path.expanduser('~'), os.path.join('.term_weather'))
  if not os.path.exists(cfg_path):
    os.makedirs(cfg_path)

    with open(os.path.join(cfg_path, 'config.json'), 'w') as config_file:
      config_file.write(json.dumps(default_cfg))

  with open(os.path.join(cfg_path, 'config.json'), 'r') as config_file:
    return json.load(config_file)


def update(key, value):
  config = load()
  config[key] = value

  cfg_path = os.path.join(os.path.expanduser('~'), os.path.join('.term_weather'))

  with open(os.path.join(cfg_path, 'config.json'), 'w') as config_file:
    config_file.write(json.dumps(config))