from pprint import pprint
import requests
import json

API = '6418b539e0697f54de8a3df65ebe9444'

parameters = {
    'appid': API,
    'units': 'metric',
    'lang': 'eng'
}

while True:
    city_name = input('Shaxar nomini kiriting: ')

    try:
        parameters['q'] = city_name
        requests = requests.get('https://api.openweathermap.org/data/2.5/weather?',
                                params=parameters).json()

        name = requests['name']
        description = requests['weather'][0]['description']
        temp = requests['main']['temp']
        wind_speed = requests['wind']['speed']
        sunrise = requests['sys']['sunrise']
        sunset = requests['sys']['sunset']
        timezone = requests['timezone']
        clouds = requests['clouds']['all']
        lon = requests['coord']['lon']
        lat = requests['coord']['lat']
        weather_id = requests['weather'][0]['id']
        main = requests['weather'][0]['main']
        icon = requests['weather'][0]['icon']
        base = requests['base']
        feels_like = requests['main']['feels_like']
        temp_min = requests['main']['temp_min']
        temp_max = requests['main']['temp_max']
        pressure = requests['main']['pressure']
        humidity = requests['main']['humidity']
        sea_level = requests['main']['sea_level']
        grnd_level = requests['main']['grnd_level']
        visibility = requests['visibility']
        deg = requests['wind']['deg']
        gust = requests['wind']['gust']
        rain_1h = requests['rain']['1h']
        dt = requests['dt']


        print(f"""{name} shaxrida ob-xavo {description}
Havo xarorati: {temp} °C
Shamol tezligi: {wind_speed} m/s
Quyosh chiqishi: {sunrise}
Quyosh botishi: {sunset}
Vaqt: {timezone}
Bulutlar: {clouds}
Lon: {lon}
Lat: {lat}
Ob-xavo id: {weather_id}
Main: {main}
Icon: {icon}
Base: {base}
Tuyilishi: {feels_like}
Minimal tezligi: {temp_min}
Maximal tezligi: {temp_max}
Bosim: {pressure}
Namlik: {humidity}
Dengiz sathi: {sea_level}
Zamin darajasi: {grnd_level}
Ko'rinish: {visibility}
Deg: {deg}
Shamol: {gust}
1h: {rain_1h}
dt: {dt}
""")

    except Exception as e:
        print('Xatolik yuzaga keldi!')