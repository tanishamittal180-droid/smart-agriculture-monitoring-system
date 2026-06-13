class RainPredictor:
    
    def predict_rain(
        self,
        humidity,
        temperature
    ):

        if humidity > 80 and temperature < 30:

            return "Rain Expected"

        return "No Rain Expected"