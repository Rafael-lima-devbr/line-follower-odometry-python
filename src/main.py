from openrdk import CommsRuntime
from openrdk import Motors
from odometry import Odometry
from pid import PID
import time

base_speed = 50

runtime = CommsRuntime(
    auto_start=True,
    enable_webview=True,
    enable_webview_updates=True,
)

motor_r = runtime.traction("98:3D:AE:43:50:50")
motor_l = runtime.traction("10:20:BA:AA:E7:28")
line_sensor = runtime.line_sensor("10:20:BA:AC:F4:B0")

motores = Motors(right = motor_r, left = motor_l)

pid = PID()
odometry = Odometry()

while True:
    reading = line_sensor.get_data()
    position = reading["position"]
    correction = pid.calculate(position)

    left_speed = base_speed + correction
    right_speed = base_speed - correction

    left_speed = max(-100, min(100, left_speed))
    right_speed = max(-100, min(100, right_speed))

    motores.right.move(right_speed)
    motores.left.move(left_speed)

    time.sleep(0.01)
