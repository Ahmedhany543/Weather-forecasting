import requests

APIkey = "29f58b7b2b3db18b02bf1f5744f81495"


def get_data(place, forecast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?units=metric&q={place}&appid={APIkey}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    no_values = 8 * forecast_days
    filtered_data = filtered_data[:no_values]

    return filtered_data


if __name__ == "__main__":
    print(get_data("Cairo", 5))
