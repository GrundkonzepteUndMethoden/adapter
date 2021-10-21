from Sockel import AmerikanischerSensorSockel

#Sensor mit nicht-kompatiblem Sockel
class AmerikanischerTemperaturSensor(AmerikanischerSensorSockel):
    """Test instanciation of AmerikanischerTemperaturSensor.

    >>> type(AmerikanischerTemperaturSensor())
    <class 'sensoren.AmerikanischerSensor.AmerikanischerTemperaturSensor'>

    Test uebertrageDatenAuf10Pins()

    >>> (AmerikanischerTemperaturSensor()).uebertrageDatenAuf10Pins()
    '123'
    """

    def uebertrageDatenAuf10Pins(self):
        inkompatibleDaten = "123"
        return inkompatibleDaten