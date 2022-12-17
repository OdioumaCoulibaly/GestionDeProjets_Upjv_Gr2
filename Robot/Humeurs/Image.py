#!/usr/bin/env python3
#-- coding: utf-8 --#
#!/usr/bin/env python3
#-- coding: utf-8 --#
import time
import busio
import sys
from PIL import Image, ImageDraw
import digitalio
from board import SCK, MOSI, MISO, CE0, D24, D25

from adafruit_rgb_display import color565
from adafruit_rgb_display.st7789 import ST7789


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

if len(sys.argv) < 2:
    print("Usage: {} <image_file>".format(sys.argv[0]))
    sys.exit(1)

image_file = sys.argv[1]

if disp.rotation % 180 == 90:
    height = disp.width  # we swap height/width to rotate it to landscape!
    width = disp.height
else:
    width = disp.width  # we swap height/width to rotate it to landscape!
    height = disp.height
image = Image.new("RGB", (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image)

image = Image.open("./GIFHumeurs/Base/Base6.gif")



# Load an image.
print('Loading gif: {}...'.format(image_file))

print('Drawing gif, press Ctrl+C to exit!')

frame = 0

while True:
    try:
        image.seek(frame)
        image.convert("RGB")
        disp.image(image.resize((width, height)))
        frame += 1
        time.sleep(0.05)

    except EOFError:
        frame = 0