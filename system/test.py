import time

from djitellopy import tello

me = tello.Tello()
me.connect()
me.takeoff()
time.sleep(3)
me.land()
