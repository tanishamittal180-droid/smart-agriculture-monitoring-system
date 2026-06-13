class WeatherEffect:
    
    def get_weather(
        self,
        temperature
    ):

        if temperature > 40:
            return "🔥 Heat Wave"

        elif temperature > 30:
            return "☀️ Sunny"

        elif temperature > 20:
            return "⛅ Cloudy"

        return "🌧 Rainy"