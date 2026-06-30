import time
import math

class Odometry:
    def __init__ (self):
        self.x = 0
        self.y = 0
        self.theta = 0
        self.wheel_radius = 0.0229
        self.wheel_base = 0.123
        self.last_right_deg = None
        self.last_left_deg = None
    
    def update (self, right_deg, left_deg):
        if self.last_right_deg is None or self.last_left_deg is None:
            self.last_right_deg = right_deg
            self.last_left_deg = left_deg
            return
    
