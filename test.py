import sensoren.AmerikanischerSensor as as1
import sensoren.AmerikanischerSensor2 as as2
import sensoren.DeutscherSensor as ds
import Anschluss as an
import SensorSockelAdapter as ssa

def test():
    import doctest
    # doctest.IGNORE_EXCEPTION_DETAIL
    doctest.testmod(as1)
    doctest.testmod(as2)
    doctest.testmod(ds)
    doctest.testmod(an)
    doctest.testmod(ssa)
    print("just test doctest")

if __name__ == "__main__":
    test()