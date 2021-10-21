from Anschluss import TemperaturSensorAnschluss
from sensoren.DeutscherSensor import DeutscherTemperaturSensor
from sensoren.AmerikanischerSensor import AmerikanischerTemperaturSensor
from sensoren.AmerikanischerSensor2 import AmerikanischerTemperaturSensor2

from SensorSockelAdapter import SensorSockelAdapter, SensorSockelAdapter2

if __name__ == "__main__":
    #Deutscher Sensor
    sensor_d = DeutscherTemperaturSensor()
    anschluss = TemperaturSensorAnschluss(sensor_d)
    print(anschluss.sendeDatenAnSmartHomeStation())

    #Amerikanischer Sensor
    sensor_a = AmerikanischerTemperaturSensor()
    adapter1 = SensorSockelAdapter(sensor_a)
    anschluss2 = TemperaturSensorAnschluss(adapter1)
    print(anschluss2.sendeDatenAnSmartHomeStation())

    #Amerikanischer Sensor 2
    sensor_a2 = AmerikanischerTemperaturSensor2()
    adapter2 = SensorSockelAdapter(sensor_a2)
    anschluss3 = TemperaturSensorAnschluss(adapter2)
    print(anschluss3.sendeDatenAnSmartHomeStation())

    #Mit Klassenadapter
    adapter3 = SensorSockelAdapter2()
    anschluss4 = TemperaturSensorAnschluss(adapter3)
    print(anschluss4.sendeDatenAnSmartHomeStation())