from simulation.farm_simulator import SmartFarm

from alerts.alert_manager import AlertManager

from database.database_manager import DatabaseManager

import time


farm = SmartFarm()

alert_manager = AlertManager()

db = DatabaseManager()


for cycle in range(30):

    farm.update_time(cycle)

    farm.simulate_environment()

    farm.control_pump()

    db.insert_data(farm)

    alert_manager.generate_alerts(farm)

    farm.display_status()

    alert_manager.display_alerts()

    time.sleep(2)


db.close_connection()