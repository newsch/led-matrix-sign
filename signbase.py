import argparse
import time
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/..'))
from rgbmatrix import RGBMatrix, RGBMatrixOptions


class SampleBase(object):
    def __init__(self, *args, **kwargs):
        self.led_rows = 16
        self.led_chain = 6
        self.led_parallel = 1
        self.led_pwm_bits = 11
        self.led_brightness = 100
        self.led_gpio_mapping = 'regular'
        self.led_scan_mode = 1
        self.led_pwm_lsb_nanoseconds = 130
        self.led_show_refresh = False
        self.led_slowdown_gpio = 1
        self.led_no_hardware_pulse = False

    def usleep(self, value):
        time.sleep(value / 1000000.0)

    def run(self):
        print("Running")

    def initialize(self):
        options = RGBMatrixOptions()

        if self.led_gpio_mapping != None:
          options.hardware_mapping = self.led_gpio_mapping
        options.rows = self.led_rows
        options.chain_length = self.led_chain
        options.parallel = self.led_parallel
        options.pwm_bits = self.led_pwm_bits
        options.brightness = self.led_brightness
        options.pwm_lsb_nanoseconds = self.led_pwm_lsb_nanoseconds
        if self.led_show_refresh:
          options.show_refresh_rate = 1

        if self.led_slowdown_gpio != None:
            options.gpio_slowdown = self.led_slowdown_gpio
        if self.led_no_hardware_pulse:
          options.disable_hardware_pulsing = True

        # don't drop privileges
        options.drop_privileges = False

        self.matrix = RGBMatrix(options = options)

    def process(self):

        options = RGBMatrixOptions()

        if self.led_gpio_mapping != None:
          options.hardware_mapping = self.led_gpio_mapping
        options.rows = self.led_rows
        options.chain_length = self.led_chain
        options.parallel = self.led_parallel
        options.pwm_bits = self.led_pwm_bits
        options.brightness = self.led_brightness
        options.pwm_lsb_nanoseconds = self.led_pwm_lsb_nanoseconds
        if self.led_show_refresh:
          options.show_refresh_rate = 1

        if self.led_slowdown_gpio != None:
            options.gpio_slowdown = self.led_slowdown_gpio
        if self.led_no_hardware_pulse:
          options.disable_hardware_pulsing = True

        self.matrix = RGBMatrix(options = options)

        try:
            # Start loop
            print("Press CTRL-C to stop sample")
            self.run()
        except KeyboardInterrupt:
            print("Exiting\n")
            sys.exit(0)

        return True
