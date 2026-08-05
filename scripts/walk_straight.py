from openrdk import CommsRuntime
from openrdk import Motors

runtime = CommsRuntime(
    auto_start=True,
    enable_webview=True,
    enable_webview_updates=True,
)

motor_r = runtime.traction("98:3D:AE:43:50:50")
motor_l = runtime.traction("10:20:BA:AA:E7:28")

motors = Motors(right=motor_r, left=motor_l)

try:
    while (True):
        motors.move(30)
finally:
    motors.stop()
