from openrdk import CommsRuntime
from odometria import Odometry

runtime = CommsRuntime(
    auto_start=True,
    enable_webview=True,
    enable_webview_updates=True,
)

devices = runtime.list_devices()
motor = runtime.traction(serial_number)
sensor = runtime.line_sensor(serial_number)
