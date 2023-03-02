import os

from egauge import webapi

#
# You can edit the values below directly or use environment variables
# EGDEV, EGUSR, and EGPWD to set the device URL, username, and
# password, respectively.
#
meter_dev = os.getenv("EGDEV", "http://egauge-dut")
meter_user = os.getenv("EGUSR", "dmo")
meter_password = os.getenv("EGPWD", "secret password")

print(f"Using meter {meter_dev} (logging in as user {meter_user})")

dev = webapi.device.Device(
    meter_dev, webapi.JWTAuth(meter_user, meter_password)
)
