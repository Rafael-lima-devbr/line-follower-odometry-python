from openrdk import CommsRuntime
from odometria import Odometry
import time

velocidade_base = 0
KP = 0
KI = 0
KD = 0

runtime = CommsRuntime(
    auto_start=True,
    enable_webview=True,
    enable_webview_updates=True,
)

motor_right = runtime.traction(serial_number)
motor_left = runtime.traction(serial_number)
line_sensor = runtime.line_sensor(serial_number)

class PID:
    def __init__ (self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.last_error = None
        self.integral = 0
        self.last_time = None
    
    def limitar_velocidade(valor):
        return max(-100, min(100, valor))
