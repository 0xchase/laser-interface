#!/bin/python

"""
.. module:: lagona
	:platform: Unix
	:synopsis: Automated laser goggles nagging
"""

class LaserContainmentArea:
	"""Class to hold information about Laser Containment Areas (LCA) in the lab.
	A single LaserBeamPath can span multiple LCAs.
	Personal Protective Equipment (PPE) will be computed for each LCA. 

	:param name: LCA name
	:param namev: verbose LCA name 
	"""
	def __init__(self, name:str, namev:str=None):
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
	def __init__(self, low:int, high:int , lbd:bool, lbi:bool, lbr:bool , lbm:bool, lbod:bool):
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
	def __init__(self, name:str, mfg:str, pn:str):
		self.name = name
		self.mfg = mfg 
		self.pn = pn
		self.bands = []

	def add_band(self, range:LaserGlassesRange):
		"""Add glasses performance in particular wavelength range.
		"""
		self.bands.append(range)

class LaserBeamPathElement:
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
	def __init__(self, name:str, lca:LaserContainmentArea, wavelength:float, avg_power:float, diameter_collimated:float=None, 
		pulse_t_min:float=None, pulse_t_max:float=None, 
		pulse_f_min:float=None, pulse_f_max:float=None, 
		maker:str=None, model:str=None):

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

class LaserBeamPath:
	"""Class to hold data about a laser.
	:param name: laser system name
	:param namev: verbose laser system name
	"""
	def __init__(self, name:str, namev:str=None):
		self.name = name
		self.namev = namev
		self.path = []

	def add_path_element(self, path_element:LaserBeamPathElement):
		self.path.append(path_element)


# following should go in a separate configuration file 
# eg lagona_atlantic_b0225_config.py

g = []

g.append(LaserGlasses('LG6', 'Thorlabs', 'LG6'))
g[-1].add_band(LaserGlassesRange(190e-9,  	315e-9,	True,	False, 	False, 	False, 	7))
g[-1].add_band(LaserGlassesRange(190e-9,  	315e-9,	False,	True, 	True, 	True, 	4))
g[-1].add_band(LaserGlassesRange(315e-9,  	398e-9,	True,	True, 	True, 	True, 	3))
g[-1].add_band(LaserGlassesRange(9000e-9,	11000e-9,	True,	True,	False,	False,	3))

g.append(LaserGlasses('LG7', 'Thorlabs', 'LG7'))
g[-1].add_band(LaserGlassesRange(180e-9,	315e-9,	True,	False,	False,	False,	6))
g[-1].add_band(LaserGlassesRange(180e-9,	315e-9,	False,	False,	True,	False,	4))
g[-1].add_band(LaserGlassesRange(615e-9,	660e-9,	True,	True,	True,	False,	3))
# ...


lcab = LaserContainmentArea(name="B", namev="Britton Lab")
lcal = LaserContainmentArea(name="L", namev="Linke Lab")
paths = []
paths.append(LaserBeamPath('ablation', namev="cryo system ablation laser"))
paths[-1].add_path_element(
	LaserBeamPathElement(
		name = 'laser head',
		lca = lcab, 
		wavelength = 1064e-9,
		avg_power = 30,
		diameter_collimated = 2e-3,
		pulse_t_min = 1e-9, pulse_t_max = 100e-9,
		pulse_f_min = 4000, pulse_f_max = 2e6,
		maker = 'Spectra-Physics', model = 'VPFL-ISP-POD-20-0062')
	)
paths[-1].add_path_element(
	LaserBeamPathElement(
		name = 'doubler_box',
		lca = lcab, 
		wavelength = 1064e-9,
		avg_power = 30,
		diameter_collimated = 2e-3,
		pulse_t_min = 1e-9, pulse_t_max = 100e-9,
		pulse_f_min = 4000, pulse_f_max = 2e6,
		maker = 'Andrew Laugharn', model = 'circa 2019')
	)
paths[-1].add_path_element(
	LaserBeamPathElement(
		name = 'doubler_box',
		lca = lcab, 		
		wavelength = 532e-9,
		avg_power = 6,
		diameter_collimated = 2e-3,
		pulse_t_min = 1e-9, pulse_t_max = 100e-9,
		pulse_f_min = 4000, pulse_f_max = 2e6,
		maker = 'Andrew Laugharn', model = 'circa 2019')
	)
paths[-1].add_path_element(
	LaserBeamPathElement(
		name = 'Hucul West',
		lca = lcab, 
		wavelength = 532e-9,
		avg_power = 5,
		diameter_collimated = 1e-3,
		pulse_t_min = 1e-9, pulse_t_max = 100e-9,
		pulse_f_min = 4000, pulse_f_max = 2e6,
		maker = 'Connor Goham', model = 'circa 2019')
	)

paths.append(LaserBeamPath('Rb wavemeter ref', namev="what is exact Rb line??"))
paths[-1].add_path_element(
	LaserBeamPathElement(
		name = 'laser head',
		lca = lcab,
		wavelength = 780e-9,
		avg_power = 150e-3,
		diameter_collimated = 1e-3,
		maker = 'Toptica', model = 'DL Pro')
	)
paths[-1].add_path_element(
	LaserBeamPathElement(
		name = 'Rb saturated absorption setup',
		lca = lcab, 
		wavelength = 780e-9,
		avg_power = 100e-3,
		diameter_collimated = 1e-3,
		maker = 'Joe Britton', model = 'circa 2017')
	)
paths[-1].add_path_element(
	LaserBeamPathElement(
		name = 'wavemeter',
		lca = lcab, 
		wavelength = 780e-9,
		avg_power = 1e-3,
		diameter_collimated = 1e-3,
		maker = 'Joe Britton', model = 'circa 2017')
	)
paths[-1].add_path_element(
	LaserBeamPathElement(
		name = 'SLS quad cavity',
		lca = lcal, 
		wavelength = 780e-9,
		avg_power = 200e-6,
		diameter_collimated = 1e-3,
		maker = 'Wance Wang', model = 'circa 2019')
	)
