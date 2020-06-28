import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--now', action='store_true', help='display only current weather')
parser.add_argument('--tommorow', action='store_true', help='display only tommorow weather')
parser.add_argument('--daily', action='store_true', help='display forecast for next 7 days')

def parse():
  return parser.parse_args()