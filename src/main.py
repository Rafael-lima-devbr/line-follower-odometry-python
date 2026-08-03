from openrdk import CommsRuntime
from openrdk import Motors
from odometria import Odometry
from pid import PID
from line_functions import (
    is_clear_intersection,
    is_left_90_candidate,
    is_right_90_candidate,
    is_gap,
    handle_left_candidate,
    handle_right_candidate,
    handle_intersection,
    handle_gap,
    follow_line,
)
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

motors = Motors(right = motor_r, left = motor_l)

pid = PID()
odometry = Odometry()

try:
    while True:
        reading = line_sensor.get_data()
        digital = reading["digital"]

        if is_clear_intersection(digital):
            handle_intersection(motors)
            continue

        if is_left_90_candidate(digital):
            handle_left_candidate(motors, line_sensor)
            continue

        if is_right_90_candidate(digital):
            handle_right_candidate(motors, line_sensor)
            continue

        if is_gap(reading):
            handle_gap(motors)
            continue

        follow_line(reading, motors, pid, base_speed)

        time.sleep(0.01)

finally:
    motors.stop()
