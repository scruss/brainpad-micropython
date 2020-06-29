# brainpad bp2/classic rgb LED showoff
# scruss, 2020-06

from time import sleep
import pyb


def cos_wheel(pos):
    # Input a value 0 to 255 to get a colour value.
    # scruss (Stewart Russell) - 2019-03 - CC-BY-SA
    from math import cos, pi
    if pos < 0:
        return (0, 0, 0)
    pos %= 256
    pos /= 255.0
    return (int(255 * (1 + cos(pos * 2 * pi)) / 2),
            int(255 * (1 + cos((pos - 1 / 3.0) * 2 * pi)) / 2),
            int(255 * (1 + cos((pos - 2 / 3.0) * 2 * pi)) / 2))


i = 1
while True:
    i = i + 1
    i = i % 256
    w = cos_wheel(i)
    for j in range(3):
    	pyb.LED(j+1).intensity(int(w[j]/8.0))
    sleep(0.1)
