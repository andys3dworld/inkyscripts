#!/usr/bin/env python

from PIL import ImageFont
import sys

import inkyphat

objText = open("inkytxt.txt", "r")
lstLines = objText.readlines()
print (lstLines)
objText.close()

colour = "red"
inkyphat.set_colour(colour)

font_file = inkyphat.fonts.FredokaOne

top = 0
left = 0
offset_left = 0

for x in lstLines:
    font_size = 14
    text = x
    font = inkyphat.ImageFont.truetype(font_file, font_size)
    width, height = font.getsize(text)
    inkyphat.text((0, top), text[:3], 2, font=font)
    inkyphat.text((25, top), text[3:], 1, font=font)
    top += height + 1
    left = max(left, offset_left + width)

offset_left = left + 5
top = 0

inkyphat.show()
