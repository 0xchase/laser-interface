
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

lasers = []

def create_lasers():
    global lasers

    laser3 = Laser("Paladin", "Britton", "Zone L", "Paladin 355 for Raman")
    laser3.add_beam_stage(BeamStage("stage 1", 355, 4))
    lasers.append(laser3)

    laser1 = Laser("Ablation", "Britton", "Zone B", "This is the ablation laser")
    laser1.add_beam_stage(BeamStage("stage 1", 1064, 30))
    laser1.add_beam_stage(BeamStage("stage 2", 532, 30))
    laser1.add_beam_stage(BeamStage("stage 3", 532, 1.5))
    lasers.append(laser1)

    laser2 = Laser("Rb D1", "Britton", "Zone B", "Wavemeter reference")
    laser2.add_beam_stage(BeamStage("stage 1", 780, .1))
    laser2.add_beam_stage(BeamStage("stage 2", 780, 0.08))
    lasers.append(laser2)


# ====================== Classes ===========================
class BeamStage:
    def __init__(self, name:str, wavelength:float, avg_power:float):
        # Need to add other parameters here
        self.name = name
        self.wavelength = wavelength
        self.avg_power = avg_power

class Laser:
        def __init__(self, name:str, lca:str, zone:str, description:str=None):
            self.name = name
            self.lca = lca
            self.description = description
            self.stages = []
            self.gui_elements = []
            self.zone = zone

        def add_beam_stage(self, beam_stage:BeamStage):
            self.stages.append(beam_stage)



create_lasers()
