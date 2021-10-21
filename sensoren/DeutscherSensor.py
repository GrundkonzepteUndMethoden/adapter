from Sockel import DeutscherSensorSockel

#Sensor mit kompatiblem Sockel
class DeutscherTemperaturSensor(DeutscherSensorSockel):
    """Test instanciation of DeutscherTemperaturSensor.

    >>> type(DeutscherTemperaturSensor())
    <class 'sensoren.DeutscherSensor.DeutscherTemperaturSensor'>

    Test uebertrageDatenAuf5Pins()

    >>> (DeutscherTemperaturSensor()).uebertrageDatenAuf5Pins()
    123
    """
    def uebertrageDatenAuf5Pins(self):
        daten = 123
        return daten