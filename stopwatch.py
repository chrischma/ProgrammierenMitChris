import datetime
from datetime import timedelta


def get_time():
    return datetime.datetime.now()


print("Halli Hallo!")
input("Drücke ENTER, um die Messung zu starten!")
timestamp_1 = get_time()


print("Die Stoppuhr läuft!")
input("Drücke ENTER, um die Messung zu beenden!")
timestamp_2 = get_time()

passed_time = round(timedelta.total_seconds(timestamp_2-timestamp_1)) 
print("Es sind", passed_time, "Sekunden vergangen!")
