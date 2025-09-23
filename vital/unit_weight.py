# unit_weight.py

def RotorWeight(Radius):
    """
    Calculate the weight of the rotor based on its radius.

    Parameters:
        Radius (float): The radius of the rotor in meters.

    Returns:
        float: The calculated weight of the rotor in kilograms.
    """
    Weight = 11.19999928 * Radius**2 + 16.37714233 * Radius - 7.44
    return Weight

def PTOWeight(Prated):
    """
    Calculate the weight of the PTO (Power Take-Off) based on its rated power.

    Parameters:
        Prated (float): The rated power of the PTO in kilowatts.

    Returns:
        float: The calculated weight of the PTO in kilograms.
    """
    Weight = 0.01501693 * Prated + 1.51674108
    return Weight

def UnitWeight(Radius, Prated):
    """
    Calculate the total unit weight by summing the rotor weight and PTO weight.

    Parameters:
        Radius (float): The radius of the rotor in meters.
        Prated (float): The rated power of the PTO in kilowatts.

    Returns:
        float: The total unit weight in kilograms.
    """
    Weight = RotorWeight(Radius) + PTOWeight(Prated)
    return Weight