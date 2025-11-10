from Models.Dynamics import Patient

class Controller:
    def __init__(self, patient: Patient, Kp: float, Ki: float, Kd: float): # PID controller parameters set at initialisation
        self.patient = patient
        self.Kp = Kp  # Proportional gain
        self.Ki = Ki  # Integral gain
        self.Kd = Kd  # Derivative gain
        self.integral = 0
        self.previous_error = 0

    def compute_action(self):
        # Placeholder for controller algorithm
        # This would involve decision-making algorithms
        pass