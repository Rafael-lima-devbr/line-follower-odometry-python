from openrdk import CommsRuntime
import time

runtime = CommsRuntime(auto_start=True)

line_sensor = runtime.line_sensor("serial_number")

while True:
    reading = line_sensor.get_data()

    print("raw:", reading["raw"])
    print("values:", reading["values"])
    print("digital:", reading["digital"])
    print("position:", reading["position"])
    print("strength:", reading["strength"])
    print("line_detected:", reading["line_detected"])
    print("-" * 40)

    time.sleep(0.5)
