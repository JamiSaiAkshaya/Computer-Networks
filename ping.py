import os
import platform
import subprocess

def ping(host="google.com", count=4):
    """
    Simple wrapper around the system ping command.
    Works on Windows, Linux, and macOS.
    """
    # Choose command based on OS
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, str(count), host]

    try:
        output = subprocess.check_output(command, universal_newlines=True)
        print(output)
    except Exception as e:
        print(f"Ping failed: {e}")

if _name_ == "_main_":
    ping("8.8.8.8")  # Google DNS by default