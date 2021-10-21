from Sockel import AmerikanischerSensorSockel

#Sensor mit nicht-kompatiblem Sockel
class AmerikanischerTemperaturSensor2(AmerikanischerSensorSockel):
    """Test instanciation of AmerikanischerTemperaturSensor2.

    >>> type(AmerikanischerTemperaturSensor2())
    <class 'sensoren.AmerikanischerSensor2.AmerikanischerTemperaturSensor2'>

    Test uebertrageDatenAuf10Pins()

    >>> (AmerikanischerTemperaturSensor2()).uebertrageDatenAuf10Pins()
    123
    """
    def uebertrageDatenAuf10Pins(self):
        inkompatibleDaten = 0x7B
        return inkompatibleDaten