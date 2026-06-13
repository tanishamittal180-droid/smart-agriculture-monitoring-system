import paho.mqtt.client as mqtt
import json
import sqlite3

DB = "database/farm_data.db"

def save(data):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO sensor_data
        (soil_moisture, temperature, humidity, water_tank, light_intensity, pump_status)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        data["soil"],
        data["temp"],
        data["hum"],
        50,  # default water tank
        data["light"],
        "OFF"
    ))

    conn.commit()
    conn.close()


def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    print("📡 Received:", data)
    save(data)


client = mqtt.Client()
client.on_message = on_message

client.connect("broker.hivemq.com", 1883, 60)
client.subscribe("agri/farm1/sensor")

print("🌐 IoT Receiver Running...")
client.loop_forever()