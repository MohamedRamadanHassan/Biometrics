import time
import RPi.GPIO as MYGPIO

MYGPIO.setmode (MYGPIO.BOARD)
MYGPIO.setup(7,MYGPIO.OUT)
MYGPIO.output(7,MYGPIO.HIGH)
time.sleep(1)
MYGPIO.output(7,MYGPIO.LOW)
time.sleep(1)
MYGPIO.cleanup()
