# alerts/alert_manager.py

class AlertManager:

    def __init__(self):

        self.alerts = []

        self.alert_history = []

    def generate_alerts(self, farm):

        current_alerts = []

        if farm.soil_moisture < 35:

            current_alerts.append(
                "🚨 Dry Soil Alert"
            )

        if farm.temperature > 40:

            current_alerts.append(
                "🔥 High Temperature Alert"
            )

        if farm.water_tank < 20:

            current_alerts.append(
                "💧 Low Water Tank Alert"
            )

        if farm.water_tank < 10:

            current_alerts.append(
                "⚠️ Critical Water Level"
            )

        if farm.pump_status == "ON":

            current_alerts.append(
                "🚿 Pump Activated"
            )

        self.alerts = current_alerts

        for alert in current_alerts:

            self.alert_history.append(alert)

        return current_alerts

    def display_alerts(self):

        print("\n========== ALERT CENTER ==========")

        if len(self.alerts) == 0:

            print("✅ No Active Alerts")

        else:

            for alert in self.alerts:

                print(alert)

        print("==================================\n")

    def display_alert_history(self):

        print("\n======= ALERT HISTORY =======")

        if len(self.alert_history) == 0:

            print("No Alert History")

        else:

            for alert in self.alert_history:

                print(alert)

        print("=============================\n")