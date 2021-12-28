import RPi.GPIO as io
import time
io.setmode(io.BOARD)
io.setup(33,io.IN, pull_up_down=io.PUD_UP)
while True:
        if io.input(33):
                print("Pressed")
        else:
                print("Not Pressed")
