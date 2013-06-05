#!/usr/bin/env python
import Image, ImageDraw, os, sys

# SETTING VARIABLES FROM COMMAND LINE
UP = 'up'
DOWN = 'down'
DIRS = [UP, DOWN]

name        = 'test.jpg'
color       = 'white'
max_opacity = 255.0
min_opacity = 0.0
direction   = UP

try:
    name        = sys.argv[1];
    color       = sys.argv[2];
    max_opacity = min(255., float(sys.argv[3]));
    min_opacity = max(0., float(sys.argv[4]));
except (IndexError, ValueError):
    pass
try:
    direction = sys.argv[5]
    if direction not in DIRS:
        direction = UP2
except (IndexError, ValueError):
    pass

# Actual program starts
im = Image.open(name)

if im.mode != 'RGBA':
    im = im.convert('RGBA')

gradient = Image.new('L', (1, im.size[1]))
height = gradient.size[1] 

if direction == UP:
    for y in range(height):
        gradient.putpixel((0, y), (min_opacity + \
                    (max_opacity - min_opacity) / (height) * (y + 1)))

if direction == DOWN:
    for y in range(height):
        gradient.putpixel((0, y), min_opacity + \
            (max_opacity - min_opacity) / (height) * (height - y - 1))

overlay = gradient.resize(im.size, Image.ANTIALIAS)
alpha = overlay.rotate(180)
im.putalpha(alpha)
background = Image.new('RGBA', im.size, color)
background.paste(im, (0,0), im)
background.show()
# background.save('../flyby/images/flyby-main-gradient.jpg')