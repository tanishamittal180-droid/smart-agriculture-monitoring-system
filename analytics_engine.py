# analytics/analytics_engine.py

import sqlite3


class AnalyticsEngine:

    def __init__(self):
        self.connection = sqlite3.connect(
            "database/farm_data.db"
        )

        self.cursor = self.connection.cursor()

    # ------------------------------
    # Average Temperature
    # ------------------------------

    def average_temperature(self):

        self.cursor.execute(
            """
            SELECT AVG(temperature)
            FROM sensor_data
            """
        )

        result = self.cursor.fetchone()[0]

        return round(result, 2) if result else 0

    # ------------------------------
    # Average Humidity
    # ------------------------------

    def average_humidity(self):

        self.cursor.execute(
            """
            SELECT AVG(humidity)
            FROM sensor_data
            """
        )

        result = self.cursor.fetchone()[0]

        return round(result, 2) if result else 0

    # ------------------------------
    # Average Soil Moisture
    # ------------------------------

    def average_soil_moisture(self):

        self.cursor.execute(
            """
            SELECT AVG(soil_moisture)
            FROM sensor_data
            """
        )

        result = self.cursor.fetchone()[0]

        return round(result, 2) if result else 0

    # ------------------------------
    # Average Water Tank
    # ------------------------------

    def average_water_tank(self):

        self.cursor.execute(
            """
            SELECT AVG(water_tank)
            FROM sensor_data
            """
        )

        result = self.cursor.fetchone()[0]

        return round(result, 2) if result else 0

    # ------------------------------
    # Pump Usage Count
    # ------------------------------

    def pump_usage_count(self):

        self.cursor.execute(
            """
            SELECT COUNT(*)
            FROM sensor_data
            WHERE pump_status='ON'
            """
        )

        return self.cursor.fetchone()[0]

    # ------------------------------
    # Total Records
    # ------------------------------

    def total_records(self):

        self.cursor.execute(
            """
            SELECT COUNT(*)
            FROM sensor_data
            """
        )

        return self.cursor.fetchone()[0]

    # ------------------------------
    # Farm Health Score
    # ------------------------------

    def farm_health_score(self):

        soil = self.average_soil_moisture()
        water = self.average_water_tank()
        temp = self.average_temperature()

        score = 100

        if soil < 40:
            score -= 20

        if water < 30:
            score -= 20

        if temp > 40:
            score -= 10

        return max(score, 0)

    # ------------------------------
    # Generate Report
    # ------------------------------

    def generate_report(self):

        return {
            "Average Temperature": self.average_temperature(),
            "Average Humidity": self.average_humidity(),
            "Average Soil Moisture": self.average_soil_moisture(),
            "Average Water Tank": self.average_water_tank(),
            "Pump Usage Count": self.pump_usage_count(),
            "Total Records": self.total_records(),
            "Farm Health Score": self.farm_health_score()
        }

    # ------------------------------
    # Close Database
    # ------------------------------

    def close(self):
        self.connection.close()