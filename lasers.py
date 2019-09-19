
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

lasers = []

def create_lasers():
    global lasers

    laser4 = Laser("Sr+ S1/2 - P1/2", "Britton", "Zone L", "Description goes here")
    laser4.add_beam_stage(BeamStage("stage 1", 422, 0.08))
    laser4.add_beam_stage(BeamStage("stage 2", 422, 0.064))
    lasers.append(laser4)

    laser5 = Laser("Sr PI D1", "Britton", "Zone L", "Description goes here")
    laser5.add_beam_stage(BeamStage("stage 1", 461, 0.112))
    laser5.add_beam_stage(BeamStage("stage 2", 461, 0.0896))
    lasers.append(laser5)

    laser6 = Laser("Sr+ D5/2 - P3/2", "Britton", "Zone L", "Description goes here")
    laser6.add_beam_stage(BeamStage("stage 1", 1033, 0.24))
    laser6.add_beam_stage(BeamStage("stage 1", 1033, 0.192))
    lasers.append(laser6)

    laser7 = Laser("Sr+ D3/2 - P1/2", "Britton", "Zone L", "Description goes here")
    laser7.add_beam_stage(BeamStage("stage 1", 1092, 0.137))
    laser7.add_beam_stage(BeamStage("stage 1", 1033, 0.1096))
    lasers.append(laser7)

    laser8 = Laser("Sr PI 2nd", "Britton", "Zone L", "I-Beam Smart")
    laser8.add_beam_stage(BeamStage("stage 1", 407, 0.1))
    laser8.add_beam_stage(BeamStage("stage 1", 407, 0.1))
    lasers.append(laser8)



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

    laser9 = Laser("Yb+ D1", "Britton", "Zone B", "Description goes here")
    laser9.add_beam_stage(BeamStage("stage 1", 369, 0.0225))
    laser9.add_beam_stage(BeamStage("stage 2", 369, 0.523))
    lasers.append(laser9)

    laser10 = Laser("Yb PI D1", "Britton", "Zone B", "Description goes here")
    laser10.add_beam_stage(BeamStage("stage 1", 399, 0.028))
    laser10.add_beam_stage(BeamStage("stage 2", 399, 0.528))
    lasers.append(laser10)

    laser11 = Laser("Missing Name", "Britton", "Zone B", "Description goes here")
    laser11.add_beam_stage(BeamStage("stage 1", 493, 0.035))
    laser11.add_beam_stage(BeamStage("stage 2", 493, 0.535))
    lasers.append(laser11)

    laser12 = Laser("Yb+ F7/2 - [5/2] 5/2", "Britton", "Zone B", "Description goes here")
    laser12.add_beam_stage(BeamStage("stage 1", 635, 0.055))
    laser12.add_beam_stage(BeamStage("stage 2", 635, 0.555))
    lasers.append(laser12)

    laser13 = Laser("Ba+ D3/2 - P1/2", "Britton", "Zone B", "Description goes here")
    laser13.add_beam_stage(BeamStage("stage 1", 650, 0.04))
    laser13.add_beam_stage(BeamStage("stage 2", 650, 0.54))
    lasers.append(laser13)

    laser14 = Laser("Yb+ D3/2 - [3/2] 1/2", "Britton", "Zone B", "Description goes here")
    laser14.add_beam_stage(BeamStage("stage 1", 935, 0.095))
    laser14.add_beam_stage(BeamStage("stage 2", 935, 0.595))
    lasers.append(laser14)

    laser15 = Laser("Yb+ D3/2 - P3/2", "Britton", "Zone B", "Description goes here")
    laser15.add_beam_stage(BeamStage("stage 1", 1650, 0.04))
    laser15.add_beam_stage(BeamStage("stage 2", 1650, 0.54))
    lasers.append(laser15)


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
