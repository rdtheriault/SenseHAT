## button.py
from picamera import PiCamera
from time import sleep
import sense_hat

camera = PiCamera()
sense = sense_hat.SenseHat()

pressed = sense_hat.ACTION_PRESSED
stop = 0

camera.start_preview(alpha=192)
events = sense.stick.get_events()

while stop == 0:
  events = sense.stick.get_events()
  if events:
    for e in events:
      if e.action == pressed:
        stop = 1
		sleep(3)
		camera.capture("/home/pi/Desktop/Classes/#/button.jpg")  #change file name as needed
		camera.stop_preview()
