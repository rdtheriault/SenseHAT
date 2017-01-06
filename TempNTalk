#

#!/usr/bin/env python3

from sense_hat import SenseHat
import time

"""
  Sense HAT Sensors Display - Temp
"""
sense = SenseHat()

#Put colors here
blue=(0, 0, 255)
red=(255,0,0)
yellow=(255, 255, 0)

cold= "it is freezing"
hot= "it his so hot"
perfect= "now it is perfect"

while True:
  temp= sense.temp#change this to humidity
  if temp<10:
    sense.show_message(str(cold),text_colour=blue)
  elif temp>60:
    sense.show_message(str(hot),text_colour=red)
  else:
    sense.show_message(str(perfect),text_colour=yellow)
