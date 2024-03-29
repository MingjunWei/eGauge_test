# eGauge open source Python code

This repository is a collection of Python packages that have been
released by eGauge Systems LLC as open source (MIT license).  These
are released in the hope that they may be useful for other developers.
Please see LICENSE for details.  eGauge Systems LLC also reserved the
rights to add, modify, or remove code from this repository or the
entire repository without notice.

## Example Programs

Example programs can be found in the `examples` subdirectory.  If you
want to run these programs, ensure that all dependencies are installed
by running the command:

```sh
pip install egauge-python[examples]
```

Before running these programs, set the following environment variables
for your preferred test device:

 * EGDEV: URL of the test device (e.g., "http://eGaugeXXXXX.local" or
   "http://eGaugeXXXX.d.egauge.net")
 * EGUSR: Username to authenticate with (e.g., "owner")
 * EGPWD: Password to authenticate with (e.g., "super-secret-pw")

## Overview of available modules

### egauge.webapi

The classes in this module provide access to eGauge web services.  The
APIs may be available on eGauge devices and/or as cloud-based web
services.

### egauge.webapi.device

The classes in this module provide access to APIs implemented on
eGauge devices.

### egauge.webapi.cloud

The classes in this module provide access to APIs implemented by
eGauge cloud services.

### egauge.ctid

The classes in this module support manufacturing CTid® sensors.  CTid®
is patented technology and shall be used in accordance with the
licensing agreements governing its use.

### egauge.pyside2

The classes in this module support QT5-based graphical
user-interfaces.

## Source Code Conventions

Source code should be formatted with ``black`` using a maximum line-length
of 79 characters.  Black can be installed with ``pip install black``.
If the resulting output is inadequate for some reason, such as manually
formatted data tables, you can make judicious use of ``# fmt: off`` and
``# fmt: on`` to disable formatting for the relevant lines.

Source code should be syntax checked with pylint.  Pylint can be
installed with ``pip install pylint``.  You can make judicious use
of ``# pylint: disable=``\ *warning-name* to temporarily disable
warnings that can safely be ignored.
