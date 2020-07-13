# -*- coding: utf-8 -*-
# brainpad bp2 temperature sensor vs core temperature
# scruss, 2020-07


from pyb import ADC, Pin, ADCAll
from time import sleep
from math import log

tmp = ADC(Pin('B0'))            # MCP9701A on PB0
adc = ADCAll(12, 0x70000)       # enable internal sensors

while True:
    vref = adc.read_vref()
    degC = ((vref * tmp.read() / 4095) - 0.4) / 0.01953
    print('mcu: %5.1f degC :: sensor: %5.1f degC' %
          (adc.read_core_temp(), degC))
    sleep(1.2)
