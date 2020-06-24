# hardware platform: Brainpad
# read the temperature value with the onboard mcp9701a sensor
# might be reading a bit high
# scruss, 2020-06

from pyb import ADC,Pin
from time import sleep
adc0 = ADC(Pin('B0'))

while True:
    volts = 3.3 * adc0.read() / 4096
    degC = (volts - 0.427) / 0.0195
    print('%7.1f degC (%7.3f V)' % (degC, volts))
    sleep(0.5)
