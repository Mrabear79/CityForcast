import requests


def getWeather(city):

    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q={city}&appid=52e08cd58041deea8b6b10e4eeb5363c&units=imperial'.format(city=city))
    data = r.json()
    temp = data['main']['temp']
    max_temp = data['main']['temp_max']
    min_temp = data['main']['temp_min']
    print('The Weather In {0} Is {1}'.format(city, data['main']))


def main():
    while True:
        city = input("Type in the city: ")
        weather = getWeather(city)

main()
