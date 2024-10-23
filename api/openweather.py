
import requests

city = input("Введите название населенного пункта: ")
key = '7fe1d51d3760f56be31f7feb6ee33bc4'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric'
response = requests.get(url).json()

def temp(city, desc, t, wind, clouds, humidity ):
    return rf"""    Населенный пункт: {city}
    Погода: {desc}
    Температура: {t}
    Влажность: {humidity}%
    Скорость ветра: {wind}ms
    Облачно: {clouds}%
"""
try:
    print("""
    ===============================
             OpenWeather
    ===============================
    """)
    print(
        temp(
            city,
            response['weather'][0]['description'],
            response['main']['temp'],
            response['wind']['speed'],
            response['clouds']['all'],
            response['main']['humidity']
        )
    )
except:
    print("Вы неверно указали населенный пункт. Перезапустите программу)")
