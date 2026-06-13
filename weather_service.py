import requests


class WeatherService:

    def get_weather(self):

        url = (
            "https://api.open-meteo.com/v1/forecast"
            "?latitude=31.63"
            "&longitude=74.87"
            "&current_weather=true"
        )

        response = requests.get(url)

        data = response.json()

        return data["current_weather"]