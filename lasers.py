from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

"""
.. module:: lagona
    :platform: Unix
    :synopsis: Automated laser goggles nagging
"""

lasers = []


class LaserContainmentArea:
    """Class to hold information about Laser Containment Areas (LCA) in the lab.
    A single LaserBeamPath can span multiple LCAs.
    Personal Protective Equipment (PPE) will be computed for each LCA.

    :param name: LCA name
    :param namev: verbose LCA name
    """

    def __init__(self, name: str, namev: str = None):
        self.name = name
        self.namev = namev


class LaserGlassesRange:
    """Class to hold optical attenuation data for laser glasses in a particular wavelength range.

    :param low: lower wavelength in meters
    :param high: upper wavelength in meters
    :param lbd: is continuous wave (t > 0.25 s)
    :param lbi: is pulsed mode (1 us < t < 0.25 s)
    :param lbr: is giant pulsed mode (1 ns < t < 1 us)
    :param lbm: is mode locked (t < 1 ns)
    :param lbod: optical density

    cf: https://www.thorlabs.com/newgrouppage9.cfm?objectgroup_id=762
    """

    def __init__(self, low: int, high: int, lbd: bool, lbi: bool, lbr: bool, lbm: bool, lbod: bool):
        self.low = low
        self.high = high
        self.lbd = lbd
        self.lbi = lbi
        self.lbr = lbr
        self.lbm = lbm
        self.lbod = lbod


class LaserGlasses:
    """Class to hold data about laser glasses.

    :param name: name
    :param mfg: manufacturer
    :param pn: part number

    """

    def __init__(self, name: str, mfg: str, pn: str):
        self.name = name
        self.mfg = mfg
        self.pn = pn
        self.bands = []

    def add_band(self, range: LaserGlassesRange):
        """Add glasses performance in particular wavelength range.
    """
        self.bands.append(range)


# ====================== Classes ===========================

class PathElement:
    """Class to hold data about a segment of a laser beam path.

    :param name: path element name (eg f0, f2 for fundamental, second harmonic)
    :param lca: laser containment area
    :param wavelength: center wavelength in meters
    :param avg_power: time-average power in watts
    :param diameter_collimated: laser beam diameter when collimated in meters
    :param pulse_t: pulse duration in seconds, None if CW
    :param pulse_f_min: minimum repetition rate in Hertz, None if CW
    :param pulse_f_max: maximum repetition rate in Hertz, None if CW
    :param maker: manufacturer or maker of the laser path element
    :param model: model number
    """

    def __init__(self, name: str, lca: str, wavelength: float, avg_power: float, diameter_collimated: float = None,
                 pulse_t_min: float = None, pulse_t_max: float = None, pulse_f_min: float = None,
                 pulse_f_max: float = None,
                 maker: str = None, model: str = None):
        self.name = name
        self.lca = lca
        self.wavelength = wavelength
        self.avg_power = avg_power

        self.diameter_collimated = diameter_collimated
        self.pulse_t_min = pulse_t_min
        self.pulse_t_max = pulse_t_max
        self.pulse_f_min = pulse_f_min
        self.pulse_f_max = pulse_f_max
        self.maker = maker
        self.model = model


class Laser:
    def __init__(self, name: str, lca: str, zone: str, description: str = None):
        self.name = name
        self.lca = lca
        self.description = description
        self.stages = []
        self.gui_elements = []
        self.zone = zone

    def add_path_element(self, element: PathElement):
        self.stages.append(element)


def create_lasers():
    global lasers

    laser1 = Laser("Ablation", "Britton", "Zone B", "This is the ablation laser")
    laser1.add_path_element(
        PathElement(
            name="Laser head",
            wavelength=1064,
            lca="Zone B",
            avg_power=30,
            diameter_collimated=2e-3,
            pulse_t_min=1e-9,
            pulse_t_max=100e-9,
            pulse_f_min=4000,
            pulse_f_max=2e6,
            maker="Spectra-Physics",
            model="VPFL-ISP-POD-20-0062"))
    laser1.add_path_element(
        PathElement(
            name="Doubler box 1",
            wavelength=1064,
            lca="Zone B",
            avg_power=30,
            diameter_collimated=2e-3,
            pulse_t_min=1e-9,
            pulse_t_max=100e-9,
            pulse_f_min=4000,
            pulse_f_max=2e6,
            maker="Andrew",
            model="Circa 2019"))
    laser1.add_path_element(
        PathElement(
            name="Doubler box 2",
            wavelength=1064,
            lca="Zone B",
            avg_power=30,
            diameter_collimated=2e-3,
            pulse_t_min=1e-9,
            pulse_t_max=100e-9,
            pulse_f_min=4000,
            pulse_f_max=2e6,
            maker="Andrew",
            model="Circa 2019"))
    laser1.add_path_element(
        PathElement(
            name="Hucul West",
            wavelength=1064,
            lca="Zone B",
            avg_power=30,
            diameter_collimated=2e-3,
            pulse_t_min=1e-9,
            pulse_t_max=100e-9,
            pulse_f_min=4000,
            pulse_f_max=2e6,
            maker="Conner",
            model="Circa 2019"))
    lasers.append(laser1)

    laser16 = Laser("Rb wavemeter ref", "Britton", "Zone B", "What is exact Rb line???")
    laser16.add_path_element(
        PathElement(
            name="Laser head",
            wavelength=780,
            lca="Zone B",
            avg_power=150e-3,
            diameter_collimated=1e-3,
            maker="Toptica",
            model="Circa 2017"))
    laser16.add_path_element(
        PathElement(
            name="RB saturated absorption setup",
            wavelength=780,
            lca="Zone B",
            avg_power=100e-3,
            diameter_collimated=1e-3,
            maker="Joe Britton",
            model="Circa 2017"))
    laser16.add_path_element(
        PathElement(
            name="Wavemeter",
            wavelength=780,
            lca="Zone B",
            avg_power=150e-3,
            diameter_collimated=1e-3,
            maker="Joe Britton",
            model="Circa 2017"))
    laser16.add_path_element(
        PathElement(
            name="SLS Quad Cavity",
            wavelength=780,
            lca="Zone L",
            avg_power=200e-6,
            diameter_collimated=1e-3,
            maker="Wance Wang",
            model="Circa 2017"))
    lasers.append(laser16)

    laser4 = Laser("Sr+ S1/2 - P1/2", "Britton", "Zone L", "Description goes here")
    laser4.add_path_element(PathElement(name="stage 1", wavelength=422, lca="Zone L", avg_power=0.08))
    laser4.add_path_element(PathElement(name="stage 1", wavelength=422, lca="Zone L", avg_power=0.064))
    lasers.append(laser4)

    laser5 = Laser("Sr PI D1", "Britton", "Zone L", "Description goes here")
    laser5.add_path_element(PathElement(name="stage 1", wavelength=461, lca="Zone L", avg_power=0.0112))
    laser5.add_path_element(PathElement(name="stage 2", wavelength=461, lca="Zone L", avg_power=0.0896))
    lasers.append(laser5)

    laser6 = Laser("Sr+ D5/2 - P3/2", "Britton", "Zone L", "Description goes here")
    laser6.add_path_element(PathElement(name="stage 1", wavelength=1033, lca="Zone L", avg_power=0.137))
    laser6.add_path_element(PathElement(name="stage 2", wavelength=1033, lca="Zone L", avg_power=0.1096))
    lasers.append(laser6)

    laser7 = Laser("Sr+ D3/2 - P1/2", "Britton", "Zone L", "Description goes here")
    laser7.add_path_element(PathElement(name="stage 1", wavelength=1092, lca="Zone L", avg_power=0.137))
    laser7.add_path_element(PathElement(name="stage 2", wavelength=1092, lca="Zone L", avg_power=0.1096))
    lasers.append(laser7)

    laser8 = Laser("Sr PI 2nd", "Britton", "Zone L", "I-Beam Smart")
    laser8.add_path_element(PathElement(name="stage 1", wavelength=407, lca="Zone L", avg_power=0.1))
    laser8.add_path_element(PathElement(name="stage 2", wavelength=407, lca="Zone L", avg_power=0.1))
    lasers.append(laser8)

    laser3 = Laser("Paladin", "Britton", "Zone L", "Paladin 355 for Raman")
    laser3.add_path_element(PathElement(name="stage 1", wavelength=355, lca="Zone L", avg_power=4))
    lasers.append(laser3)

    laser2 = Laser("Rb D1", "Britton", "Zone B", "Wavemeter reference")
    laser2.add_path_element(PathElement(name="stage 1", wavelength=780, lca="Zone B", avg_power=0.08))
    laser2.add_path_element(PathElement(name="stage 2", wavelength=780, lca="Zone B", avg_power=0.08))
    lasers.append(laser2)

    laser9 = Laser("Yb+ D1", "Britton", "Zone B", "Description goes here")
    laser9.add_path_element(PathElement(name="stage 1", wavelength=369, lca="Zone B", avg_power=0.0225))
    laser9.add_path_element(PathElement(name="stage 2", wavelength=369, lca="Zone B", avg_power=0.523))
    lasers.append(laser9)

    laser10 = Laser("Yb PI D1", "Britton", "Zone B", "Description goes here")
    laser10.add_path_element(PathElement(name="stage 1", wavelength=399, lca="Zone B", avg_power=0.028))
    laser10.add_path_element(PathElement(name="stage 2", wavelength=399, lca="Zone B", avg_power=0.528))
    lasers.append(laser10)

    laser12 = Laser("Yb+ F7/2 - [5/2] 5/2", "Britton", "Zone B", "Description goes here")
    laser12.add_path_element(PathElement(name="stage 1", wavelength=636, lca="Zone B", avg_power=0.055))
    laser12.add_path_element(PathElement(name="stage 2", wavelength=635, lca="Zone B", avg_power=0.555))
    lasers.append(laser12)

    laser13 = Laser("Ba+ D3/2 - P1/2", "Britton", "Zone B", "Description goes here")
    laser13.add_path_element(PathElement(name="stage 1", wavelength=650, lca="Zone B", avg_power=0.04))
    laser13.add_path_element(PathElement(name="stage 2", wavelength=650, lca="Zone B", avg_power=0.54))
    lasers.append(laser13)

    laser14 = Laser("Yb+ D3/2 - [3/2] 1/2", "Britton", "Zone B", "Description goes here")
    laser14.add_path_element(PathElement(name="stage 1", wavelength=935, lca="Zone B", avg_power=0.095))
    laser14.add_path_element(PathElement(name="stage 2", wavelength=935, lca="Zone B", avg_power=0.595))
    lasers.append(laser14)

    laser15 = Laser("Yb+ D3/2 - P3/2", "Britton", "Zone B", "Description goes here")
    laser15.add_path_element(PathElement(name="stage 1", wavelength=1650, lca="Zone B", avg_power=0.04))
    laser15.add_path_element(PathElement(name="stage 2", wavelength=1650, lca="Zone B", avg_power=0.54))
    lasers.append(laser15)

    g = []

    g.append(LaserGlasses('LG6', 'Thorlabs', 'LG6'))
    g[-1].add_band(LaserGlassesRange(190e-9, 315e-9, True, False, False, False, 7))
    g[-1].add_band(LaserGlassesRange(190e-9, 315e-9, False, True, True, True, 4))
    g[-1].add_band(LaserGlassesRange(315e-9, 398e-9, True, True, True, True, 3))
    g[-1].add_band(LaserGlassesRange(9000e-9, 11000e-9, True, True, False, False, 3))

    g.append(LaserGlasses('LG7', 'Thorlabs', 'LG7'))
    g[-1].add_band(LaserGlassesRange(180e-9, 315e-9, True, False, False, False, 6))
    g[-1].add_band(LaserGlassesRange(180e-9, 315e-9, False, False, True, False, 4))
    g[-1].add_band(LaserGlassesRange(615e-9, 660e-9, True, True, True, False, 3))


create_lasers()
