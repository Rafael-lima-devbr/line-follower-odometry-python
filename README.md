# Follow-Line

A Python project for controlling a line-following robot.

The robot uses a line sensor, PID control, motor movement, and odometry to follow a path and handle different track situations.

## Project Structure

```text
follow-line/
├── scripts/
│   ├── calibrate_sensor.py
│   └── test_sensor.py
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

Contains helper functions for line detection and special track situations, such as:

* Intersections
* Line gaps
* Possible 90-degree turns
* Line recovery

## Scripts

### `calibrate_sensors.py`

Used to calibrate the line sensor before running the robot.

### `test_sensor.py`

Used to test sensor readings separately from the main robot program.

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
git clone https://github.com/YOUR_USERNAME/follow-line.git
```

Enter the project folder:

```bash
cd follow-line
```

Run the main file:

```bash
python src/main.py
```

The robot hardware and Open-RDK modules must be configured before running the project.

## Utility Scripts

Calibrate the line sensor:

```bash
python scripts/calibrate_sensors.py
```

Test the sensor readings:

```bash
python scripts/test_sensor.py
```

## Status

This project is currently under development.

## Author

Rafael Lima
