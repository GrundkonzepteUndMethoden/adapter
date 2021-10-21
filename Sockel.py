from abc import abstractmethod, ABC

#kompatibler Sockel
class DeutscherSensorSockel(ABC):
    @abstractmethod
    def uebertrageDatenAuf5Pins(self):
        pass

#inkompatibler Sockel
class AmerikanischerSensorSockel(ABC):
    @abstractmethod
    def uebertrageDatenAuf10Pins(self):
        pass