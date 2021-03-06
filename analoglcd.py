# hardware platform: BrainPad
# example to show analog light value to the oled screen

from pyb import I2C, ADC, Pin
import ssd1306
from time import sleep

adc0 = ADC(Pin('B1'))


i2c = I2C(1, I2C.MASTER, baudrate=100000)
lcd = ssd1306.SSD1306_I2C(128, 64, i2c)
lcd.text("The BrainPad", 0, 0)
lcd.text("From ", 0, 16)
lcd.text("GHI Electronics", 0, 32)
lcd.text("Light Value test", 0, 48)

lcd.show()
sleep(2)

while True:
    light = adc0.read()//10
    lcd.fill(0)
    lcd.text("light value: ", 0, 16)
    lcd.text(str(light), 0, 32)
    lcd.show()
    sleep(0.05)
