from Sockel import DeutscherSensorSockel

#Anschluss an den Sensoren angeschlossen werden sollen
class TemperaturSensorAnschluss:
    """Test instanciation of TemperaturSensorAnschluss.

    >>> from sensoren.DeutscherSensor import DeutscherTemperaturSensor
    >>> type(TemperaturSensorAnschluss(DeutscherTemperaturSensor()))
    <class 'Anschluss.TemperaturSensorAnschluss'>

    Test sendeDatenAnSmartHomeStation()

    >>> from sensoren.DeutscherSensor import DeutscherTemperaturSensor
    >>> (TemperaturSensorAnschluss(DeutscherTemperaturSensor())).sendeDatenAnSmartHomeStation()
    123
    """
    def __init__(self, sensor: DeutscherSensorSockel):
        self.sensor = sensor

    def sendeDatenAnSmartHomeStation(self):
        daten = self.sensor.uebertrageDatenAuf5Pins()
        return daten