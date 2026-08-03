import time

def is_clear_intersection(digital):
    return all(digital)


def is_left_90_candidate(digital):
    return digital[0] and digital[1] and not digital[3] and not digital[4]


def is_right_90_candidate(digital):
    return digital[3] and digital[4] and not digital[0] and not digital[1]


def is_gap(reading):
    return not reading["line_detected"]


def center_stays_on_line_during_short_forward(motors, line_sensor):
    start_time = time.monotonic()

    while time.monotonic() - start_time < 0.25:
        motors.left.move(30)
        motors.right.move(30)

        reading = line_sensor.get_data()
        digital = reading["digital"]

        if not digital[2]:
            return False

        time.sleep(0.01)

    return True


def handle_left_90(motors, line_sensor):
    center_count = 0

    while center_count < 3:
        motors.left.move(-30)
        motors.right.move(40)

        reading = line_sensor.get_data()
        digital = reading["digital"]

        if digital[2]:
            center_count += 1
        else:
            center_count = 0

        time.sleep(0.01)


def handle_right_90(motors, line_sensor):
    center_count = 0

    while center_count < 3:
        motors.left.move(40)
        motors.right.move(-30)

        reading = line_sensor.get_data()
        digital = reading["digital"]

        if digital[2]:
            center_count += 1
        else:
            center_count = 0

        time.sleep(0.01)


def handle_intersection(motors):
    motors.left.move(35)
    motors.right.move(35)
    time.sleep(0.4)


def handle_left_candidate(motors, line_sensor):
    center_stayed = center_stays_on_line_during_short_forward(motors, line_sensor)

    if center_stayed:
        handle_intersection(motors)
    else:
        handle_left_90(motors, line_sensor)


def handle_right_candidate(motors, line_sensor):
    center_stayed = center_stays_on_line_during_short_forward(motors, line_sensor)

    if center_stayed:
        handle_intersection(motors)
    else:
        handle_right_90(motors, line_sensor)


def follow_line(reading, motors, pid, base_speed):
    position = reading["position"]

    correction = pid.calculate(position)

    left_speed = base_speed + correction
    right_speed = base_speed - correction

    left_speed = max(-100, min(100, left_speed))
    right_speed = max(-100, min(100, right_speed))

    motors.left.move(left_speed)
    motors.right.move(right_speed)


def handle_gap(motors):
    motors.left.move(30)
    motors.right.move(30)
    time.sleep(0.1)
