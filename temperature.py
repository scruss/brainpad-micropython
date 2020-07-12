# hardware platform: Brainpad Classic/BP2
# read the temperature value with the onboard mcp9701a sensor
# not super accurate: I see Vs around 3.15 V, so indicates ~+2 °C at room temp for me
# scruss, 2020-06

from pyb import ADC,Pin
from time import sleep
adc0 = ADC(Pin('B0'))

while True:
    volts = 3.3 * adc0.read() / 4095
    degC = (volts - 0.4) / 0.019
    print('%7.1f degC (%7.3f V)' % (degC, volts))
    sleep(0.5)
