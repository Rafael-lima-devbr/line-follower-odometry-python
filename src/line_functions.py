import time
import math

def is_clear_intersection(digital):
    return all(digital)

def is_left_90_candidate(digital):
    return digital[0] and digital[1] and not digital[3] and not digital[4]


def is_right_90_candidate(digital):
    return digital[3] and digital[4] and not digital[0] and not digital[1]


def is_gap(reading):
    return not reading["line_detected"]

def update_odometry_motors(odometry, motors):
    right_deg = motors.right.get_position_telemetry()
    left_deg = motors.left.get_position_telemetry()

    odometry.update(right_deg, left_deg)

def turn_right(motors, odometry, target_angle_rad):
    update_odometry_motors(odometry, motors)
    start_theta = odometry.theta

    while True:
        motors.left.move(30)
        motors.right.move(-30)

        update_odometry_motors(odometry, motors)

        turned_angle = odometry.angle_difference(odometry.theta, start_theta)

        if turned_angle >= target_angle_rad:
            break

        time.sleep(0.01)

    motors.stop()

def turn_left(motors, odometry, target_angle_rad):
    update_odometry_motors(odometry, motors)
    start_theta = odometry.theta

    while True:
        motors.left.move(-30)
        motors.right.move(30)

        update_odometry_motors(odometry, motors)

        turned_angle = odometry.angle_difference(odometry.theta, start_theta)

        if turned_angle <= -target_angle_rad:
            break

        time.sleep(0.01)

    motors.stop()

def move_straight_for(motors, odometry, duration, speed):
    start_time = time.monotonic()

    while time.monotonic() - start_time < duration:
        motors.move(speed)

        update_odometry_motors(odometry, motors)

        time.sleep(0.01)

    motors.stop()


def center_stays_on_line_during_short_forward(motors, line_sensor, odometry):
    start_time = time.monotonic()

    while time.monotonic() - start_time < 0.25:
        motors.move(30)

        update_odometry_motors(odometry, motors)

        reading = line_sensor.get_data()
        digital = reading["digital"]

        if not digital[2]:
            motors.stop()
            return False

        time.sleep(0.01)

    motors.stop()
    return True


def handle_intersection(motors, odometry):
    move_straight_for(motors, odometry, 0.35, 35)


def handle_left_candidate(motors, line_sensor, odometry):
    center_stayed = center_stays_on_line_during_short_forward(motors, line_sensor, odometry)

    if center_stayed:
        handle_intersection(motors, odometry)
    else:
        turn_left(motors, odometry, math.radians(90))


def handle_right_candidate(motors, line_sensor, odometry):
    center_stayed = center_stays_on_line_during_short_forward(motors, line_sensor, odometry)

    if center_stayed:
        handle_intersection(motors, odometry)
    else:
        turn_right(motors, odometry, math.radians(90))


def follow_line(reading, motors, pid, base_speed):
    position = reading["position"]

    correction = pid.calculate(position)

    left_speed = base_speed - correction
    right_speed = base_speed + correction

    left_speed = max(-40, min(40, left_speed))
    right_speed = max(-40, min(40, right_speed))

    motors.left.move(left_speed)
    motors.right.move(right_speed)


def try_cross_gap(motors, line_sensor, odometry):
    start_time = time.monotonic()

    while time.monotonic() - start_time < 3.0:
        motors.move(30)

        update_odometry_motors(odometry, motors)

        reading = line_sensor.get_data()

        if reading["line_detected"]:
            motors.stop()
            return True

        time.sleep(0.01)

    forward_time = time.monotonic() - start_time

    move_straight_for(motors, odometry, forward_time, -30)
    return False

def is_obstacle(distance_sensor):
    distance = distance_sensor.get_distance_cm()

    if distance is None:
        return False

    return distance < 15

def handle_lost_line(motors, line_sensor, last_position, odometry):
    center_count = 0

    if last_position < 0:
        left_speed = 15
        right_speed = 30
    else:
        left_speed = 30
        right_speed = 15

    while True:
        motors.left.move(left_speed)
        motors.right.move(right_speed)
        
        update_odometry_motors(odometry, motors)

        reading = line_sensor.get_data()
        digital = reading["digital"]

        if reading["line_detected"] and digital[2]:
            center_count += 1
        else:
            center_count = 0

        if center_count >= 3:
            motors.stop()
            return True

        time.sleep(0.01)

def handle_obstacle(motors, line_sensor, odometry):
    motors.stop()
    time.sleep(0.2)

    move_straight_for(motors, odometry, 0.15, -20)

    turn_right(motors, odometry, math.radians(90))
    move_straight_for(motors, odometry, 0.45, 30)

    turn_left(motors, odometry, math.radians(90))
    move_straight_for(motors, odometry, 0.50, 30)

    turn_left(motors, odometry, math.radians(90))
    move_straight_for(motors, odometry, 0.45, 30)

    turn_right(motors, odometry, math.radians(90))
    time.sleep(0.1)
