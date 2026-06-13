import sqlite3

connection = sqlite3.connect(
    "database/farm_data.db"
)

cursor = connection.cursor()

cursor.execute(
    "SELECT * FROM sensor_data"
)

records = cursor.fetchall()

for record in records:

    print(record)

connection.close()