import math

class ConstantsUnitConversion:
    """
    A singleton class for unit conversion constants.
    """
    
    _instance = None

    def __new__(cls):
        """
        Ensure only one instance of the class exists.
        """
        if cls._instance is None:
            cls._instance = super(ConstantsUnitConversion, cls).__new__(cls)
        return cls._instance

    @property
    def sec2days(self):
        """Seconds to days."""
        return 1 / (24.0 * 3600.0)

    @property
    def mile2m(self):
        """Miles to meters."""
        return 1609.34

    @property
    def m2mile(self):
        """Meters to miles."""
        return 1 / self.mile2m

    @property
    def m2km(self):
        """Meters to kilometers."""
        return 1e-3

    @property
    def W2MW(self):
        """Watts to megawatts."""
        return 1e-6

    @property
    def W2kW(self):
        """Watts to kilowatts."""
        return 1e-3

    @property
    def kE2E(self):
        """Kilo euros to euros."""
        return 1e3

    @property
    def N2mTon(self):
        """Newtons to metric tons."""
        return 1.019716e-4

    @property
    def N2kN(self):
        """Newtons to kilonewtons."""
        return 1e-3

    @property
    def euro2dollar(self):
        """Euros to dollars."""
        return 1.26 * 1.1304

    @property
    def ft2m(self):
        """Feet to meters."""
        return 0.3048

    @property
    def cms2ms(self):
        """Centimeters per second to meters per second."""
        return 1e-2

    @property
    def rads2rpm(self):
        """Radians per second to revolutions per minute."""
        return 60.0 / (2.0 * math.pi)

    @property
    def m32cm3(self):
        """Cubic meters to cubic centimeters."""
        return 1e6

    @property
    def hrs2days(self):
        """Hours to days."""
        return 1 / 24.0