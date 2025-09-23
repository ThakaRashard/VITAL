Background
=======================

Cavitation Constraints
-----------------------

The minimum pressure coefficient (:math:`C_{p,\text{min}}`) corresponds to the lowest pressure on the blade, typically near the leading edge or suction side, where velocity is highest due to Bernoulli's principle. It is defined as:

.. math::

    C_{p,\text{min}} = \frac{P - P_\infty}{\frac{1}{2} \rho V_\infty^2}

Here, :math:`P` is the local pressure on the blade surface, :math:`P_\infty` is the freestream pressure, :math:`\rho` is the fluid density, and :math:`V_\infty` is the effective velocity at the blade tip. The effective velocity is calculated as:

.. math::

    V_\infty = \sqrt{U_{\text{inf\_adjusted}}^2 + (r \cdot \omega)^2}

where :math:`U_{\text{inf\_adjusted}}` is the adjusted flow speed, :math:`r` is the rotor radius, and :math:`\omega` is the rotational speed of the rotor.

To avoid cavitation, the pressure at the blade surface must remain above the vapor pressure of water:

.. math::

    P_{\text{min}} > P_{\text{vapor}}

Using the pressure equation:

.. math::

    P = P_{\text{atm}} + \rho g h

where :math:`P_{\text{atm}}` is the atmospheric pressure, :math:`\rho g h` is the hydrostatic pressure due to the depth of the turbine below the water surface, and :math:`h` is the depth. The depth :math:`h` is calculated as:

.. math::

    h = d - r

Here, :math:`d` is the hub depth (distance from the water surface to the hub of the rotor), and :math:`r` is the rotor radius. This accounts for the fact that the blade tip is located at a depth :math:`d - r`, which is above than the hub depth.

Substituting :math:`h = d - r` into the cavitation condition gives:

.. math::

    P_{\text{atm}} + \rho g (d - r) + \frac{1}{2} \rho V_\infty^2 C_{p,\text{min}} > P_{\text{vapor}}


To express the cavitation constraint in Python's standard inequality format (:math:`h(x) \geq 0`), the equation is rearranged as:

.. math::

    h(x) = P_{\text{atm}} + \rho g (d - r) + \frac{1}{2} \rho V_\infty^2 C_{p,\text{min}} - P_{\text{vapor}}

Here, :math:`h(x)` is the cavitation constraint function, which must satisfy :math:`h(x) \geq 0` to ensure no cavitation occurs. If :math:`h(x) < 0`, cavitation occurs, as the pressure at the blade surface drops below the vapor pressure.

