#!/usr/bin/env python3

import os
import signal
import subprocess
import time

print('Starting up')
p = subprocess.run(['exec','sudo','./rpi-rgb-led-matrix/examples-api-use/demo','-D0'], shell=True)
p.stdout
time.sleep(2)
p.terminate()
