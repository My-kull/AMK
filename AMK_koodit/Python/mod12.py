import requests

# Tehtävä 12.1

response = requests.get("https://api.chucknorris.io/jokes/random")
response_json = response.json()

print(response_json["value"])


# Tehtävä 12.2


def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city_name, "appid": api_key}
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None


def kelvin_to_celsius(kelvin_temp):
    return kelvin_temp - 273.15


def main():
    api_key = "2e4d4cd53a2c8e4b0129a75e4fb106ec"
    city_name = input("Anna paikkakunnan nimi: ")
    weather_data = get_weather(city_name, api_key)

    if weather_data is None or weather_data.get("cod") != 200:
        print("Paikkakuntaa ei löytynyt.")
        return

    weather_description = weather_data["weather"][0]["description"]
    temperature_kelvin = weather_data["main"]["temp"]
    temperature_celsius = kelvin_to_celsius(temperature_kelvin)

    print(f"Säätila: {weather_description}")
    print(f"Lämpötila: {temperature_celsius:.2f} °C")


if __name__ == "__main__":
    main()
