#!/usr/bin/env python3
#-- coding: utf-8 --#
import os
import time
import busio
import sys
from PIL import Image, ImageDraw, ImageOps
import digitalio
from board import SCK, MOSI, MISO, CE0, D24, D25
import board
from adafruit_rgb_display import color565
from adafruit_rgb_display.st7789 import ST7789


BUTTON_NEXT = board.D17
BUTTON_PREVIOUS = board.D22

def init_button(pin):
    button = digitalio.DigitalInOut(pin)
    button.switch_to_input()
    button.pull = digitalio.Pull.UP
    return button


# pylint: disable=too-few-public-methods
class Frame:
    def __init__(self, duration=0):
        self.duration = duration
        self.image = None


# pylint: enable=too-few-public-methods


class AnimatedGif:
    def __init__(self, display, width=None, height=None, folder=None):
        self._frame_count = 0
        self._loop = 0
        self._index = 0
        self._duration = 0
        self._gif_files = []
        self._frames = []

        if width is not None:
            self._width = width
        else:
            self._width = display.width
        if height is not None:
            self._height = height
        else:
            self._height = display.height
        self.display = display
        self.advance_button = init_button(BUTTON_NEXT)
        self.back_button = init_button(BUTTON_PREVIOUS)
        if folder is not None:
            self.load_files(folder)
            self.run()

    def advance(self):
        self._index = (self._index + 1) % len(self._gif_files)

    def back(self):
        self._index = (self._index - 1 + len(self._gif_files)) % len(self._gif_files)

    def load_files(self, folder):
        gif_files = [f for f in os.listdir(folder) if f.endswith(".gif")]
        for gif_file in gif_files:
            gif_file = os.path.join(folder, gif_file)
            image = Image.open(gif_file)
            # Only add animated Gifs
            if image.is_animated:
                self._gif_files.append(gif_file)

        print("Found", self._gif_files)
        if not self._gif_files:
            print("No Gif files found in current folder")
            exit()  # pylint: disable=consider-using-sys-exit

    def preload(self):
        image = Image.open(self._gif_files[self._index])
        print("Loading {}...".format(self._gif_files[self._index]))
        if "duration" in image.info:
            self._duration = image.info["duration"]
        else:
            self._duration = 0
        if "loop" in image.info:
            self._loop = image.info["loop"]
        else:
            self._loop = 1
        self._frame_count = image.n_frames
        self._frames.clear()
        for frame in range(self._frame_count):
            image.seek(frame)
            # Create blank image for drawing.
            # Make sure to create image with mode 'RGB' for full color.
            frame_object = Frame(duration=self._duration)
            if "duration" in image.info:
                frame_object.duration = image.info["duration"]
            frame_object.image = ImageOps.pad(  # pylint: disable=no-member
                image.convert("RGB"),
                (self._width, self._height),
                method=Image.LANCZOS,
                color=(0, 0, 0),
                centering=(0.5, 0.5),
            )
            self._frames.append(frame_object)

    def play(self):
        self.preload()

        _prev_advance_btn_val = self.advance_button.value
        _prev_back_btn_val = self.back_button.value
        # Check if we have loaded any files first
        if not self._gif_files:
            print("There are no Gif Images loaded to Play")
            return False
        while True:
            for frame_object in self._frames:
                start_time = time.monotonic()
                self.display.image(frame_object.image)
                _cur_advance_btn_val = self.advance_button.value
                _cur_back_btn_val = self.back_button.value
                if not _cur_advance_btn_val and _prev_advance_btn_val:
                    self.advance()
                    return False
                if not _cur_back_btn_val and _prev_back_btn_val:
                    self.back()
                    return False

                _prev_back_btn_val = _cur_back_btn_val
                _prev_advance_btn_val = _cur_advance_btn_val
                while time.monotonic() < (start_time + frame_object.duration / 1000):
                    pass

            if self._loop == 1:
                return True
            if self._loop > 0:
                self._loop -= 1

    def run(self):
        while True:
            auto_advance = self.play()
            if auto_advance:
                self.advance()
# Configuration for CS and DC pins:
CS_PIN = CE0
DC_PIN = D24
RESET_PIN = D25
BAUDRATE = 24000000

# Setup SPI bus using hardware SPI:
spi = busio.SPI(clock=SCK, MOSI=MOSI, MISO=MISO)

# Create the ST7789 display:
disp = ST7789(
    spi,
    rotation=90,
    width=240,
    height=320,
    x_offset=0,
    y_offset=0,
    baudrate=BAUDRATE,
    cs=0,
    dc=digitalio.DigitalInOut(DC_PIN),
    rst=digitalio.DigitalInOut(RESET_PIN))

if disp.rotation % 180 == 90:
    disp_height = disp.width  # we swap height/width to rotate it to landscape!
    disp_width = disp.height
else:
    disp_width = disp.width
    disp_height = disp.height


gif_player = AnimatedGif(disp, width=disp_width, height=disp_height, folder="./GIFHumeurs/Clindoeuil")
