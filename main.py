from openrdk import CommsRuntime
from odometria import Odometry
from pid import PID
import time

base_speed = 50

runtime = CommsRuntime(
    auto_start=True,
    enable_webview=True,
    enable_webview_updates=True,
)

motor_right = runtime.traction(serial_number)
motor_left = runtime.traction(serial_number)
line_sensor = runtime.line_sensor(serial_number)

pid = PID()
odometry = Odometry()

while True:
    reading = line_sensor.get_position()
    position = reading["position"]
    correction = pid.calculate(position)

    left_speed = base_speed + correction
    right_speed = base_speed - correction

    left_speed = max(-100, min(100, left_speed))
    right_speed = max(-100, min(100, right_speed))

    motor_right.move(right_speed)
    motor_left.move(left_speed)

    time.sleep(0.01)
