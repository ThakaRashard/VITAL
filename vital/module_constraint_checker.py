import numpy as np
from vital.constGlobal import ConstantsGlobal
import matplotlib.pyplot as plt
plt.style.use('tableau-colorblind10')

class ConstraintChecker:
    """
    Checks various constraints for turbine and vessel configurations.
    """

    def __init__(self, Radius, CpminFunc, turbineConfig):
        """
        Initialize the ConstraintChecker.

        Args:
            Radius (float): Rotor radius.
            CpminFunc (callable): Function to calculate the pressure coefficient for cavitation (Cpmin).
            turbineConfig (dict): Turbine configuration dictionary.
        """
        self.Radius = Radius
        self.CpminFunc = CpminFunc
        self.GLOBAL = ConstantsGlobal()
        self.rho = self.GLOBAL.rho
        self.g = self.GLOBAL.g
        self.Pvap = self.GLOBAL.Pvap
        self.Patm = self.GLOBAL.Patm
        self.withChain = turbineConfig.get('attachment_method') == 'chain'

    def depth_constraint(self, dHub):
        """
        Calculate depth constraint values.

        Args:
            dHub (np.ndarray): Hub depths.

        Returns:
            np.ndarray: Depth constraint values (must be > 0 to be valid, rotor must be submerged.).
        """
        return dHub - self.Radius

    def check_depth_constraint(self, dHub):
        """
        Check if depth constraint is satisfied.

        Args:
            dHub (np.ndarray): Hub depths.

        Returns:
            bool: True if satisfied, False otherwise.
        """
        return np.all(self.depth_constraint(dHub) > 0)

    def cavitation_constraint(self, TSR, Uinf_adjusted, RotorSpeed, dHub):
        """
        Calculate cavitation constraint values.

        Args:
            TSR (np.ndarray): Tip-speed ratio values.
            Uinf_adjusted (np.ndarray): Adjusted flow speeds.
            RotorSpeed (np.ndarray): Rotor speeds.
            dHub (np.ndarray): Hub depths.

        Returns:
            np.ndarray: Cavitation constraint values (must be > 0 to be valid).
        """
        Vinf = np.sqrt(Uinf_adjusted**2 + (self.Radius * RotorSpeed)**2)
        Pinf = self.Patm + self.rho * self.g * (dHub - self.Radius) # Tip of rotor
        Cpmin = self.CpminFunc(TSR)  # Pressure coefficient for cavitation
        return 0.5 * self.rho * Vinf**2 * Cpmin - (self.Pvap - Pinf)

    def check_cavitation_constraint(self, TSR, Uinf_adjusted, RotorSpeed, dHub):
        """
        Check if cavitation constraint is satisfied.

        Args:
            TSR (np.ndarray): Tip-speed ratio values.
            Uinf_adjusted (np.ndarray): Adjusted flow speeds.
            RotorSpeed (np.ndarray): Rotor speeds.
            dHub (np.ndarray): Hub depths.

        Returns:
            bool: True if satisfied, False otherwise.
        """
        return np.all(self.cavitation_constraint(TSR, Uinf_adjusted, RotorSpeed, dHub) > 0)

    def check_pitch_stiffness_constraint(self, vessel):
        """
        Check if pitch stiffness constraint is satisfied.

        Args:
            vessel (VesselData): Vessel data object.

        Returns:
            bool: True if satisfied, False otherwise.
        """
        return vessel.user_defined or vessel.GM > 0

    def pitch_constraint(self, vessel, Uinf_adjusted, Ft, dHub, number_of_turbines):
        """
        Calculate pitch constraint values.

        Args:
            vessel (VesselData): Vessel data object.
            Uinf_adjusted (np.ndarray): Flow speeds.
            Ft (np.ndarray): Thrust forces.
            dHub (np.ndarray): Hub depths.
            number_of_turbines (int): Number of turbines.

        Returns:
            np.ndarray: Pitch constraint values (must be > 0 to be valid).
        """
        if vessel.user_defined:
            return self.user_defined_pitch_constraint(vessel, Uinf_adjusted, Ft, dHub, number_of_turbines)
        return self.designed_pitch_constraint(vessel, Uinf_adjusted, Ft, number_of_turbines)

    def designed_pitch_constraint(self, vessel, Uinf_adjusted, Ft, number_of_turbines):
        """
        Calculate pitch constraint for a designed vessel.

        Args:
            vessel (VesselData): Vessel data object.
            Uinf_adjusted (np.ndarray): Flow speeds.
            Ft (np.ndarray): Thrust forces.
            number_of_turbines (int): Number of turbines.

        Returns:
            np.ndarray: Pitch constraint values (must be > 0 to be valid).
        """
        theta_m = vessel.theta_m
        Fmoor = (0.25 * vessel.Cd * vessel.height * self.rho * vessel.width * Uinf_adjusted**2 + number_of_turbines * Ft) / np.sin(theta_m)
        Fdrag = 0.5 * self.rho * vessel.Cd * Uinf_adjusted**2 * vessel.width * vessel.h_s
        Fbuoy = self.rho * self.g * vessel.VesselVolume

        MomentEquation = (
            Fmoor * np.cos(theta_m) * vessel.length / 2 +
            number_of_turbines * Ft * vessel.height / 2 +
            Fdrag * (vessel.height / 2 - vessel.h_s / 2) -
            Fbuoy * (vessel.height / 2 - vessel.h_s / 2)
        )

        return vessel.Kphi * vessel.phi - MomentEquation

    def user_defined_pitch_constraint(self, vessel, Uinf_adjusted, Ft, dHub, number_of_turbines):
        """
        Calculate pitch constraint for a user-defined vessel.

        Args:
            vessel (VesselData): Vessel data object.
            Uinf_adjusted (np.ndarray): Flow speeds.
            Ft (np.ndarray): Thrust forces.
            dHub (np.ndarray): Hub depths.
            number_of_turbines (int): Number of turbines.

        Returns:
            np.ndarray: Pitch constraint values (must be > 0 to be valid).
        """
        F_vessel_thrust = 0.5 * self.rho * vessel.Cd * vessel.area * Uinf_adjusted**2
        F_turbine_thrust = number_of_turbines * Ft
        F_total = F_vessel_thrust + F_turbine_thrust

        if self.withChain:
            F_total = F_vessel_thrust  # Only vessel drag for Chain-connected turbines

        ConstraintOut = (
            vessel.Kphi * vessel.phi -
            F_turbine_thrust * dHub -
            F_total * vessel.Xm * np.cos(vessel.theta_m) -
            F_total * vessel.Zm * np.sin(vessel.theta_m)
        )

        # plt.plot(ConstraintOut)
        return ConstraintOut

    def check_pitch_constraint(self, vessel, Uinf_adjusted, Ft, dHub, number_of_turbines):
        """
        Check if pitch constraint is satisfied.

        Args:
            vessel (VesselData): Vessel data object.
            Uinf_adjusted (np.ndarray): Flow speeds.
            Ft (np.ndarray): Thrust forces.
            dHub (np.ndarray): Hub depths.
            number_of_turbines (int): Number of turbines.

        Returns:
            bool: True if satisfied, False otherwise.
        """
        return np.all(self.pitch_constraint(vessel, Uinf_adjusted, Ft, dHub, number_of_turbines) > 0)