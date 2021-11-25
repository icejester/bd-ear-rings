# Trinket IO demo
# Welcome to CircuitPython :)

from digitalio import *
from analogio import *
from board import *
import time
import neopixel
import random

# NeoPixel strip (of 16 LEDs) connected on D4
NUMPIXELS = 12

neopixels = neopixel.NeoPixel(D3, NUMPIXELS, brightness=1, auto_write=True, pixel_order=neopixel.GRBW)
DIRECTION = 1 # 1 == "up"
COLOR = 1 # 1 == "flicker" # 2 == "rainbow"

######################### HELPERS ##############################

# Helper to convert analog input to voltage
# def getVoltage(pin):
#     return (pin.value * 3.3) / 65536

# Helper to give us a nice color swirl
def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if (pos < 0):
        return (0, 0, 0)
    if (pos > 255):
        return (0, 0, 0)
    if (pos < 85):
        return (int(pos * 3), int(255 - (pos*3)), 0)
    elif (pos < 170):
        pos -= 85
        return (int(255 - pos*3), 0, int(pos*3))
    else:
        pos -= 170
        return (0, int(pos*3), int(255 - pos*3))

def flicker(idx, rgbVal):
    neopixels.brightness = 1
    neopixels[idx] = rgbVal
    neopixels.brightness = .025

def rainbowPulse(i):
    for p in range(NUMPIXELS):
        idx = int ((p * 256 / NUMPIXELS) + i)
        neopixels[p] = wheel(idx & 255)

def redPulse():
    # print("RED PULSE")
    aPixel = neopixels[0]
    rCur = aPixel[0]
    gCur = aPixel[1]
    bCur = aPixel[2]

    if DIRECTION == 1:
        neopixels.fill((rCur + 10, gCur, bCur))

    if DIRECTION == 2:
        neopixels.fill((rCur - 10, gCur, bCur))

def whitePulse():
    # print("WHITE PULSE!!")
    aPixel = neopixels[0]
    rCur = aPixel[0]
    gCur = aPixel[1]
    bCur = aPixel[2]

    if DIRECTION == 1:
        neopixels.fill((rCur + 15, gCur + 10, bCur + 10))

    if DIRECTION == 2:
        neopixels.fill((rCur - 15, gCur - 10, bCur - 10))

def shiftColors():
    print("In colorChange...")
    print(COLOR)
    if COLOR == 1:
        COLOR = 2
    elif COLOR == 2:
        COLOR = 1
    print(COLOR)

######################### MAIN LOOP ##############################

i = 0;
colorScheme = 1;
while True:
    if colorScheme == 1:
        for x in range(random.randint(15, 25)):
            flicker(random.randint(0, (NUMPIXELS-1)),(199,21,133))
            neopixels.fill((0,0,0))
            time.sleep(0.0125)
        colorScheme = 2
    elif colorScheme == 2:
        rainbowPulse(i)
        time.sleep(0.0125)

    i = (i+30) % 256  # run from 0 to 255

    if random.randint(0, 100) == 71:
        if colorScheme == 1:
            colorScheme=2
        elif colorScheme == 2:
            colorScheme=1
