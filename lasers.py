
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

lasers = []

def create_lasers():
    global lasers

    laser1 = Laser("laser1", "Britton", "cry system ablation laser")
    laser1.add_beam_stage(BeamStage("stage 1", 300, 30))
    laser1.add_beam_stage(BeamStage("stage 2", 400, 30))
    lasers.append(laser1)

    laser2 = Laser("laser2", "Britton", "cry system ablation laser")
    laser2.add_beam_stage(BeamStage("stage 1", 500, 30))
    laser2.add_beam_stage(BeamStage("stage 2", 600, 30))
    lasers.append(laser2)

# ====================== Classes ===========================
class BeamStage:
    def __init__(self, name:str, wavelength:float, avg_power:float):
        # Need to add other parameters here
        self.name = name
        self.wavelength = wavelength
        self.avg_power = avg_power

class Laser:
        def __init__(self, name:str, lca:str, description:str=None):
            self.name = name
            self.lca = lca
            self.description = description
            self.stages = []
            self.gui_elements = []

        def add_beam_stage(self, beam_stage:BeamStage):
            self.stages.append(beam_stage)



create_lasers()
