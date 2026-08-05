from openrdk import CommsRuntime
from openrdk import Motors
from odometria import Odometry
from pid import PID
from line_functions import (
    is_clear_intersection,
    is_left_90_candidate,
    is_right_90_candidate,
    is_gap,
    is_obstacle,
    handle_left_candidate,
    handle_right_candidate,
    handle_intersection,
    handle_lost_line,
    handle_obstacle,
    try_cross_gap,
    update_odometry_motors,
    follow_line,
)
import time

base_speed = 50
last_position = 0

runtime = CommsRuntime(
    auto_start=True,
    enable_webview=True,
    enable_webview_updates=True,
)

motor_r = runtime.traction("98:3D:AE:43:50:50")
motor_l = runtime.traction("10:20:BA:AA:E7:28")
line_sensor = runtime.line_sensor("10:20:BA:AC:F4:B0")
distance_sensor = runtime.distance_sensor("SERIAL_DO_SENSOR_DISTANCIA")

motors = Motors(right = motor_r, left = motor_l)

pid = PID()
odometry = Odometry()

try:
    while True:
        reading = line_sensor.get_data()
        update_odometry_motors(odometry, motors)

        if reading["line_detected"]:
            last_position = reading["position"]

        digital = reading["digital"]

        if is_obstacle(distance_sensor):
            handle_obstacle(motors, line_sensor, odometry)
            continue

        if is_clear_intersection(digital):
            handle_intersection(motors, odometry)
            continue

        if is_left_90_candidate(digital):
            handle_left_candidate(motors, line_sensor, odometry)
            continue

        if is_right_90_candidate(digital):
            handle_right_candidate(motors, line_sensor, odometry)
            continue

        if is_gap(reading):
            gap_found = try_cross_gap(motors, line_sensor, odometry)
            if not gap_found:
                handle_lost_line(motors, line_sensor, last_position, odometry)
            continue

        follow_line(reading, motors, pid, base_speed)

finally:
    motors.stop()
