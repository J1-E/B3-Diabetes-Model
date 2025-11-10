from dataclasses import dataclass
import numpy as np

from Models.Controller import Controller

class Patient: 
    def __init__(self):
        # Initialize parameters we care about
        self.glucose_conc = 0 # in mmol/L
        self.dgdt = 0  # rate of change of glucose concentration
        self.insulin_conc = 0  # in U/mL
        self.glucagon_conc = 0  # in pg/mL
        self.dt=1 # time step in minutes for sampling

    def plant(self):
        # Placeholder for plant model of how glucose, insulin, glucagon interact using numerical methods to model ODEs
        pass 


class ClosedLoop:
    def __init__(self, plant: Patient, controller: Controller):
        self.plant = plant
        self.controller = controller

    def update_dynamics(self):
        # Placeholder for dynamics update logic
        # This would involve complex physiological models
        pass