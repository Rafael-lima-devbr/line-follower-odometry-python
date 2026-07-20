from openrdk import CommsRuntime

runtime = CommsRuntime(auto_start=True)

line_sensor = runtime.line_sensor("serial_number")

line_sensor.set_track_type("dark")

print("Calibrando...")

line_sensor.calibrate(duration_ms=5000, wait=True)

print("Calibração finalizada.")
print("Salvando calibração...")

line_sensor.save_calibration()

print("Calibração salva.")
