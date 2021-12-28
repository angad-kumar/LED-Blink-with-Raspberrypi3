import RPi.GPIO as io
import time
io.setmode(io.BOARD)
io.setup(3,io.OUT)
while True:
    io.output(3,True)
    time.sleep(1)
    io.output(3,False)
    time.sleep(1)

