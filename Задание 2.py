import requests

url = 'https://wttr.in'

weather_parameters = {
    '0': '',
    'T':'',
    'M': '',  # параметр запроса для скорости ветра в метрах в секунду
    'lang': 'ru',  # параметр запроса для вывода прогноза на русском языке
}

response = requests.get(url, params=weather_parameters)  # передайте параметры в http-запрос

print(response.text)