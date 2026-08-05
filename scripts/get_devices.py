from openrdk import CommsRuntime 
runtime = CommsRuntime(auto_start=True, enable_webview=True, enable_webview_updates=True)

devices = runtime.list_devices()

print(devices)
