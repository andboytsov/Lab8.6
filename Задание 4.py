import requests


cities = [
    'Омск',
    'Калининград',
    'Челябинск',
    'Владивосток',
    'Красноярск',
    'Москва',
    'Екатеринбург'
]


def make_url(city):
    # в URL задаём город, в котором узнаем погоду
    return f'http://wttr.in/{city}'


def make_parameters():
    params = {
        'format': 2,  # погода одной строкой
        'M': ''  # скорость ветра в "м/с"
    }
    return params


def what_weather(city):
    try:
        response = requests.get(make_url(city), params=make_parameters())
        if response.status_code == 200:
            return response.text
        else:
            raise Exception(f"Ошибка на сервере погоды (код {response.status_code})")
    except requests.ConnectionError as e:
        return "<сетевая ошибка>"
    except Exception as e:
        return f"<ошибка на сервере погоды ({e})>"
    
print('Погода в городах:')
for city in cities:
    print(city, what_weather(city))