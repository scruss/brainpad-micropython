# hardware platform: Brainpad
# blink LED1 using a timer - use `tim.deinit()` to make it stop
# scruss, 2020-06

from pyb import LED
from machine import Timer
tim = Timer(-1)
tim.init(period=1000, mode=Timer.PERIODIC,
	callback=lambda t: LED(1).toggle())

