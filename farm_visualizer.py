class FarmVisualizer:
    
    def get_crop_icon(self, moisture):

        if moisture > 80:
            return "🌾🌾🌾"

        elif moisture > 60:
            return "🌿🌿🌿"

        elif moisture > 40:
            return "🌱🌱🌱"

        return "🥀🥀🥀"

    def get_weather_icon(self, temperature):

        if temperature > 40:
            return "🔥"

        elif temperature > 30:
            return "☀️"

        elif temperature > 20:
            return "⛅"

        return "🌧"

    def get_pump_icon(self, status):

        if status == "ON":
            return "🚿💦💦💦"

        return "🚿"