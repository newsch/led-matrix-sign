#!/usr/bin/env python
# Display a runtext with double-buffering.
from signbase import SampleBase
from rgbmatrix import graphics
import time
import socket
from datetime import datetime


class Writer(SampleBase):
    def __init__(self):
        super(Writer, self).__init__()
        # self.args = self.parser.parse_args()
        #
        # options = RGBMatrixOptions()
        #
        # if self.args.led_gpio_mapping != None:
        #   options.hardware_mapping = self.args.led_gpio_mapping
        # options.rows = self.args.led_rows
        # options.chain_length = self.args.led_chain
        # options.parallel = self.args.led_parallel
        # options.pwm_bits = self.args.led_pwm_bits
        # options.brightness = self.args.led_brightness
        # options.pwm_lsb_nanoseconds = self.args.led_pwm_lsb_nanoseconds
        # if self.args.led_show_refresh:
        #   options.show_refresh_rate = 1
        #
        # if self.args.led_slowdown_gpio != None:
        #     options.gpio_slowdown = self.args.led_slowdown_gpio
        # if self.args.led_no_hardware_pulse:
        #   options.disable_hardware_pulsing = True
        #
        # self.matrix = RGBMatrix(options = options)

    def addToQueue(self, message):
        self.queue.append(message)

    def writeAllFromQueue(self):
        pass
        # i = 0
        # while i < len(self.queue):
        #     self.write(queue[i])
        #     if (i)

    def writeLatestFromQueue():
        pass

    def run(self):
        self.write('HEYO')

    def write(self, text, timeLength=4, justification='CENTER'):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("an_oddly_specific_font_mono.bdf")
        textColor = graphics.Color(255, 0, 0)
        my_text = text.upper()

        # hacky way to get length with mono font
        letter_width = 7
        letter_spacing = 2
        text_length = len(my_text) * (letter_width + letter_spacing)
        pos = offscreen_canvas.width - text_length

        graphics.DrawText(offscreen_canvas, font, pos, 9, textColor, my_text)
        print('Writing text: ' + text)
        offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
        time.sleep(timeLength)
        print('Stopping')
        # rebase test comment


        # stopWriting = False
        # while not stopWriting:
        #     self.offscreen_canvas.Clear()
        #     len = graphics.DrawText(offscreen_canvas, font, pos, 9, textColor, my_text)
        #     pos -= 1
        #     if continuous and pos == offscreen_canvas.width - len:
        #         stopWriting = True
        #     if (pos + len < 0):
        #         stopWriting = True
        #
        #     time.sleep(0.02)
        #     offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)

if __name__ == '__main__':
    writer = Writer()
    if not writer.process():
        print('neat')
    else:
        print('finished running.')
        # writer.write('Welcome Candidates!')

# exec_time = datetime(2017,2,17,1,46)
# while True:
#     if time.localtime() > exec_time:
#         welcome_message()
#
#     sleep(60)

# welcome_message()
