import sqlite3
import joblib

# -----------------------------
# LOAD MODEL
# -----------------------------

model = joblib.load(
    "ml_model/crop_yield_model.pkl"
)

# -----------------------------
# GET LATEST DATA
# -----------------------------

connection = sqlite3.connect(
    "database/farm_data.db"
)

cursor = connection.cursor()

cursor.execute(
    """
    SELECT
    soil_moisture,
    temperature,
    humidity,
    water_tank

    FROM sensor_data

    ORDER BY id DESC

    LIMIT 1
    """
)

record = cursor.fetchone()

connection.close()

if record:

    prediction = model.predict(
        [list(record)]
    )

    print(
        f"\nPredicted Crop Yield: {prediction[0]:.2f}%"
    )

else:

    print(
        "No data found in database."
    )