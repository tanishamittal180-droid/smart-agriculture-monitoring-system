import sqlite3
import random
import time

while True:

    soil = random.randint(30, 90)
    temp = random.randint(20, 45)
    humidity = random.randint(40, 85)
    water = random.randint(20, 100)
    light = random.randint(200, 900)

    conn = sqlite3.connect("database/farm_data.db")
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO sensor_data
    (
        soil_moisture,
        temperature,
        humidity,
        water_tank,
        light_intensity,
        pump_status
    )
    VALUES (?, ?, ?, ?, ?, ?)
    """,
    (
        soil,
        temp,
        humidity,
        water,
        light,
        "OFF"
    ))

    conn.commit()
    conn.close()

    print("New Sensor Data Added")

    time.sleep(5)