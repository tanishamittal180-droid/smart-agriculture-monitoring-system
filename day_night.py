from datetime import datetime

class DayNight:

    def get_phase(self):

        hour = datetime.now().hour

        if hour < 12:
            return "🌅 Morning"

        elif hour < 17:
            return "☀️ Afternoon"

        elif hour < 20:
            return "🌇 Evening"

        return "🌙 Night"