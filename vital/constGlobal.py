class ConstantsGlobal:
    """
    A singleton class for global physical constants.
    """
    
    _instance = None

    def __new__(cls):
        """
        Ensure only one instance of the class exists.
        """
        if cls._instance is None:
            cls._instance = super(ConstantsGlobal, cls).__new__(cls)
        return cls._instance

    @property
    def rho(self):
        """
        Density of seawater (kg/m^3).
        """
        return 1025.0

    @property
    def Patm(self):
        """
        Atmospheric pressure at sea level (Pa).
        """
        return 101325.0

    @property
    def Pvap(self):
        """
        Vapor pressure of seawater at 25°C (Pa).
        """
        return 3063.7485

    @property
    def g(self):
        """
        Acceleration due to gravity (m/s^2).
        """
        return 9.8