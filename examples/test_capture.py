#!/usr/bin/env python3
#
# Copyright (c) 2023 eGauge Systems LLC
#
# See LICENSE file for details.
#
# This test program illustrates how to capture waveform samples from a
# meter using the egauge.webapi.device.Capture class.
#
import sys

from matplotlib import pyplot

import test_common

from egauge.webapi.device import Capture, TriggerMode

cap = Capture(test_common.dev)
print(f"available channels: {cap.available_channels}")

# capture samples for (up to) the first three channels:
if len(cap.available_channels) < 1:
    print(
        "The meter has no channels configured - waveform cannot be acquired."
    )
    sys.exit(1)
elif len(cap.available_channels) > 3:
    cap.channels = cap.available_channels[0:3]
else:
    cap.channels = cap.available_channels

# these settings are only needed for triggered captures:
cap.trigger_mode = TriggerMode.RISING
cap.trigger_channel = "L1"
cap.trigger_level = 0
cap.pretrigger = 0.0083  # how many seconds of data to keep ahead of trigger
cap.trigger_timeout = 1  # number of seconds before auto triggering

data = cap.acquire(duration=0.034)

# show the trigger point sample (if any):
if data.trigger_point is None:
    print("Capture was auto-triggered.")
else:
    print(data.trigger_point)

# plot the data:
_, axis = pyplot.subplots()
for chan in cap.channels:
    axis.plot(data.samples[chan].ts, data.samples[chan].ys, label=chan)
    axis.set(
        xlabel="time [s]",
        ylabel="[" + cap.channel_unit(chan) + "]",
        title="captured waveform data",
    )
axis.grid()
pyplot.legend(loc="upper right")
print("Plotting the waveform - close the plot window when done")
pyplot.show()
