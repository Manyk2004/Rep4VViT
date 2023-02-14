import requests

city = 'Moscow,RU'
appid = '33344c7d0773f4f21362c8f74a8a665b'

res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                   params={'q':city,'units':'metric','lang':'ru','APPID':appid})
data = res.json()
print("Город:", city)
print("Погодные условия:", data['weather'][0]['description'])
print("Температура:", data['main']['temp'])
print("Минимальная температура:", data['main']['temp_min'])
print("Максимальная температура", data['main']['temp_max'])