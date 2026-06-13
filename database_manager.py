# database/database_manager.py

import sqlite3


class DatabaseManager:

    def __init__(self):

        self.connection = sqlite3.connect(
            "database/farm_data.db"
        )

        self.cursor = self.connection.cursor()

        self.create_table()

    def create_table(self):

        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS sensor_data(

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,

                time_of_day TEXT,

                soil_moisture REAL,

                temperature REAL,

                humidity REAL,

                light_intensity REAL,

                water_tank REAL,

                pump_status TEXT
            )
            """
        )

        self.connection.commit()

    def insert_data(self, farm):

        self.cursor.execute(
            """
            INSERT INTO sensor_data(

                time_of_day,
                soil_moisture,
                temperature,
                humidity,
                light_intensity,
                water_tank,
                pump_status

            )

            VALUES(?,?,?,?,?,?,?)
            """,

            (
                farm.time_of_day,
                farm.soil_moisture,
                farm.temperature,
                farm.humidity,
                farm.light_intensity,
                farm.water_tank,
                farm.pump_status
            )
        )

        self.connection.commit()

    def get_all_records(self):

        self.cursor.execute(
            "SELECT * FROM sensor_data"
        )

        return self.cursor.fetchall()

    def close_connection(self):

        self.connection.close()
    def get_latest_record(self):
    
        self.cursor.execute(
        """
        SELECT *
        FROM sensor_data
        ORDER BY id DESC
        LIMIT 1
        """
    )

        return self.cursor.fetchone()
    def get_total_records(self):
    
        self.cursor.execute(
        """
        SELECT COUNT(*)
        FROM sensor_data
        """
    )

        return self.cursor.fetchone()[0]