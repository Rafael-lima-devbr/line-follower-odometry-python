# Follow-Line

A Python project for controlling a line-following robot.

The robot uses a line sensor, PID control, motor movement, and odometry to follow a path and handle different track situations.

## Project Structure

```text
line-follower-odometry-python/
├── scripts/
│   ├── calibrate_line_sensor.py
│   ├── get_devices.py
│   ├── remote_control.py
│   ├── test_line_sensor.py
│   └── walk_straight.py
│
├── src/
│   ├── main.py
│   ├── pid.py
│   ├── odometry.py
│   └── line_functions.py
│
└── README.md
```

## Files

### `main.py`

Contains the main robot control logic.

It is responsible for reading the sensors, controlling the motors, updating odometry, and deciding how the robot should move.

### `pid.py`

Contains the PID controller used to keep the robot aligned with the line.

### `odometry.py`

Contains the logic used to estimate the robot's position and rotation based on wheel movement.

### `line_functions.py`

Contains helper functions related to line detection and special track situations, such as:

* Intersections
* Line gaps
* Possible 90-degree turns
* Line recovery

## Scripts

### `calibrate_line_sensor.py`

Used to calibrate the line sensor before running the robot.

### `get_devices.py`

Lists the devices detected by the Open-RDK `CommsRuntime`.

### `remote_control.py`

Allows manual control of the robot motors using keyboard commands.

### `test_line_sensor.py`

Used to check line sensor readings separately from the main robot program.

### `walk_straight.py`

Used to test straight movement independently from the main control logic.

## Current Features

* PID-based line following
* Line sensor reading
* Motor control
* Odometry
* Intersection detection
* Gap detection
* Detection of possible 90-degree turns
* Controlled straight movement
* Controlled rotation

## Running the Project

Clone the repository:

```bash
git clone https://github.com/Rafael-lima-devbr/line-follower-odometry-python.git
```

Enter the project folder:

```bash
cd line-follower-odometry-python
```

Run the main file:

```bash
python src/main.py
```

The robot hardware and Open-RDK modules must be configured before running the project.

## Utility Scripts

Calibrate the line sensor:

```bash
python scripts/calibrate_line_sensor.py
```

List connected devices:

```bash
python scripts/get_devices.py
```

Test the line sensor:

```bash
python scripts/test_line_sensor.py
```

Control the motors manually:

```bash
python scripts/remote_control.py
```

Test straight movement:

```bash
python scripts/walk_straight.py
```

## Status

This project is currently under development.

## Author

Rafael Lima
