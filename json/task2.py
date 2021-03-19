import requests

apiid = "http://api.openweathermap.org/data/2.5/weather"
city = input("Введите город: ")
appid = "4daddc8f3135afed41c2fe2621f4d471"

params = {"appid": appid, "q": city, 'units': "metric", "lang": "ru"}

request = requests.get(apiid,
  params = params)

data = request.json()
lon = data["coord"]["lon"]
lat = data["coord"]["lat"]



apiUrl = f'https://api.openweathermap.org/data/2.5/onecall?&exclude="daily" '

params = {"appid": appid, "lat": lat, "lon": lon, 'units': "metric", "lang": "ru"}

request = requests.get(apiUrl,
params = params)

data = request.json()



for i in range(0, len(data)):
  print(f"День {i+1}:")



  print("\tТемпература:")
  print("\t\tУтро: ", data["daily"][i]["temp"]["morn"])
  print("\t\tДень: ", data["daily"][i]["temp"]["day"])
  print("\t\tВечер: ",data["daily"][i]["temp"]["eve"])
  print("\t\tНочь: ", data["daily"][i]["temp"]["night"])

  print("\tОщущение:")
  print("\t\tУтро: ", data["daily"][i]["feels_like"]["morn"])
  print("\t\tДень: ", data["daily"][i]["feels_like"]["day"])
  print("\t\tВечер: ",data["daily"][i]["feels_like"]["eve"])
  print("\t\tНочь: ", data["daily"][i]["feels_like"]["night"])

  print("\tОсадки: ", data["daily"][i]["clouds"])

  print("\tСкорость ветра: ", data["daily"][i]["wind_speed"], "м/с")

  print("\tВлажность: ", data["daily"][i]["humidity"], "%")