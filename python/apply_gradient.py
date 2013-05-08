#!/usr/bin/env python
import Image, ImageDraw, os, sys

USAGE = "Usage: ./apply_gradient.py <image> <mask_color> " + \
          "<max_mask_opacity (0-255)> <min_mask_opacity (0-255)>" + \
          " <direction (up, down)>"
UP = "up"
DOWN = "down"
DIRS = [UP, DOWN]

try:
    name        = sys.argv[1];
    color       = sys.argv[2];
    max_opacity = min(255., float(sys.argv[3]));
    min_opacity = max(0., float(sys.argv[4]));
except (IndexError, ValueError):
    print USAGE
    exit()

try:
    direction = sys.argv[5]
    if direction not in DIRS:
        raise ValueError
except IndexError:
    direction = UP
except ValueError:
    print USAGE
    exit()


im = Image.open(name)

if im.mode != 'RGBA':
    im = im.convert('RGBA')

gradient = Image.new('L', (1, im.size[1]), color)
height = gradient.size[1]
if direction == UP:
    for y in range(height):
        print min_opacity + (max_opacity - min_opacity) / (height) * y
        gradient.putpixel((0, y), (min_opacity + \
                    (max_opacity - min_opacity) / (height) * y))

if direction == DOWN:
    for y in range(height):
        gradient.putpixel((0, y), min_opacity + \
            (max_opacity - min_opacity) / (height) * (height - y))

alpha = gradient.resize(im.size, Image.ANTIALIAS)
im.paste(alpha, (0, 0), alpha)
im.show()