import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--now', 'display only current weather')
parser.add_argument('--tommorow', 'display only tommorow weather')
parser.add_argument('--daily', 'display forecast for next 7 days')