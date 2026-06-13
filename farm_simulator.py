# simulation/farm_simulator.py

import random


class SmartFarm:

    def __init__(self):

        # Farm Information
        self.farm_name = "AgriSense Farm"
        self.field_size = 5

        # Environmental Parameters
        self.soil_moisture = 80
        self.temperature = 25
        self.humidity = 75
        self.light_intensity = 300
        self.water_tank = 100

        # Pump
        self.pump_status = "OFF"

        # Time
        self.time_of_day = "Morning"

        # Irrigation Threshold
        self.soil_threshold = 40

    # --------------------------------
    # Time Cycle
    # --------------------------------

    def update_time(self, cycle):

        phases = [
            "Morning",
            "Afternoon",
            "Evening",
            "Night"
        ]

        self.time_of_day = phases[
            cycle % len(phases)
        ]

    # --------------------------------
    # Environment Simulation
    # --------------------------------

    def simulate_environment(self):

        # MORNING

        if self.time_of_day == "Morning":

            self.temperature = random.randint(22, 30)

            self.humidity = random.randint(70, 90)

            self.light_intensity = random.randint(
                300,
                600
            )

        # AFTERNOON

        elif self.time_of_day == "Afternoon":

            self.temperature = random.randint(
                35,
                45
            )

            self.humidity = random.randint(
                40,
                65
            )

            self.light_intensity = random.randint(
                800,
                1200
            )

        # EVENING

        elif self.time_of_day == "Evening":

            self.temperature = random.randint(
                25,
                35
            )

            self.humidity = random.randint(
                55,
                80
            )

            self.light_intensity = random.randint(
                200,
                500
            )

        # NIGHT

        elif self.time_of_day == "Night":

            self.temperature = random.randint(
                18,
                26
            )

            self.humidity = random.randint(
                75,
                95
            )

            self.light_intensity = random.randint(
                0,
                50
            )

        # Evaporation

        evaporation = self.temperature / 20

        self.soil_moisture -= evaporation

        # Tank Reduction

        self.water_tank -= random.uniform(
            0.2,
            1.0
        )

        # Safety Limits

        self.soil_moisture = round(
            max(0, min(100, self.soil_moisture)),
            2
        )

        self.water_tank = round(
            max(0, min(100, self.water_tank)),
            2
        )

    # --------------------------------
    # Smart Irrigation Logic
    # --------------------------------

    def control_pump(self):

        # Soil Dry

        if (
            self.soil_moisture < self.soil_threshold
            and self.water_tank > 10
        ):

            self.pump_status = "ON"

            # Watering Effect

            self.soil_moisture += random.uniform(
                8,
                15
            )

            self.water_tank -= random.uniform(
                2,
                5
            )

        else:

            self.pump_status = "OFF"

        # Safety Limits

        self.soil_moisture = round(
            max(0, min(100, self.soil_moisture)),
            2
        )

        self.water_tank = round(
            max(0, min(100, self.water_tank)),
            2
        )

    # --------------------------------
    # Display Status
    # --------------------------------

    def display_status(self):

        print("\n====================================")
        print("       AGRISENSE AI FARM")
        print("====================================")

        print(f"Farm Name       : {self.farm_name}")
        print(f"Field Size      : {self.field_size} Acres")

        print("------------------------------------")

        print(f"Time            : {self.time_of_day}")

        print(f"Soil Moisture   : {self.soil_moisture}%")

        print(f"Temperature     : {self.temperature}°C")

        print(f"Humidity        : {self.humidity}%")

        print(
            f"Light Intensity : {self.light_intensity} Lux"
        )

        print(f"Water Tank      : {self.water_tank}%")

        print("------------------------------------")

        print(f"Pump Status     : {self.pump_status}")

        print("====================================")

    # --------------------------------
    # Return Data
    # --------------------------------

    def get_farm_data(self):

        return {
            "farm_name": self.farm_name,
            "field_size": self.field_size,
            "time_of_day": self.time_of_day,
            "soil_moisture": self.soil_moisture,
            "temperature": self.temperature,
            "humidity": self.humidity,
            "light_intensity": self.light_intensity,
            "water_tank": self.water_tank,
            "pump_status": self.pump_status
        }