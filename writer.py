#!/usr/bin/env python
# Display a runtext with double-buffering.
from signbase import SignBase
from rgbmatrix import graphics
import time
import socket
from datetime import datetime


class Writer(SampleBase):
    def __init__(self):
        super(Writer, self).__init__()

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

    def write(self, text, continuous=False):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("an_oddly_specific_font_mono.bdf")
        textColor = graphics.Color(255, 0, 0)
        pos = offscreen_canvas.width - 20
        my_text = text.upper()

        graphics.DrawText(offscreen_canvas, font, pos, 9, textColor, my_text)
        offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
        time.sleep(2)


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
