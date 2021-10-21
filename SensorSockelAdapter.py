from Sockel import AmerikanischerSensorSockel, DeutscherSensorSockel
from sensoren.AmerikanischerSensor import AmerikanischerTemperaturSensor

#Sockel Adapter - Objektadapter
class SensorSockelAdapter(DeutscherSensorSockel):
    """Test instanciation of SensorSockelAdapter.

    >>> from sensoren.AmerikanischerSensor import AmerikanischerTemperaturSensor
    >>> type(SensorSockelAdapter(AmerikanischerTemperaturSensor()))
    <class 'SensorSockelAdapter.SensorSockelAdapter'>

    Test uebertrageDatenAuf5Pin()

    >>> from sensoren.AmerikanischerSensor import AmerikanischerTemperaturSensor
    >>> SensorSockelAdapter(AmerikanischerTemperaturSensor()).uebertrageDatenAuf5Pins()
    123

    Test transformiere10PinZu5Pin()

    >>> from sensoren.AmerikanischerSensor import AmerikanischerTemperaturSensor
    >>> SensorSockelAdapter(AmerikanischerTemperaturSensor()).transformiere10PinZu5Pin(0x7B)
    123

    >>> from sensoren.AmerikanischerSensor import AmerikanischerTemperaturSensor
    >>> SensorSockelAdapter(AmerikanischerTemperaturSensor()).transformiere10PinZu5Pin('123')
    123
    """
    def __init__(self, amerikanischerSensor: AmerikanischerSensorSockel):
        self.sensor = amerikanischerSensor

    #Adapter Methode
    def uebertrageDatenAuf5Pins(self):
        daten = self.transformiere10PinZu5Pin(self.sensor.uebertrageDatenAuf10Pins())
        return daten

    #hier wird transformiert
    def transformiere10PinZu5Pin(self, daten):   
        return int(daten)


#Sockel Adapter - Klassenadapter
class SensorSockelAdapter2(DeutscherSensorSockel, AmerikanischerTemperaturSensor):
    """Test instanciation of SensorSockelAdapter.

    >>> type(SensorSockelAdapter2())
    <class 'SensorSockelAdapter.SensorSockelAdapter2'>

    Test uebertrageDatenAuf5Pin()

    >>> SensorSockelAdapter2().uebertrageDatenAuf5Pins()
    123

    Test transformiere10PinZu5Pin()

    >>> SensorSockelAdapter2().transformiere10PinZu5Pin(0x7B)
    123

    >>> SensorSockelAdapter2().transformiere10PinZu5Pin('123')
    123
    """
    
    #Adapter Methode
    def uebertrageDatenAuf5Pins(self):
        daten = self.transformiere10PinZu5Pin(self.uebertrageDatenAuf10Pins())
        return daten

    #hier wird transformiert
    def transformiere10PinZu5Pin(self, daten):   
        return int(daten)