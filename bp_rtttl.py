# hardware platform: Brainpad
# play RTTTL, familiar to owners of certain S. Korean appliances
# scruss, 2020-06
# requires rtttl.py from https://github.com/dhylands/upy-rtttl

import pyb
from rtttl import RTTTL

tune = RTTTL('LG:d=4,o=5,b=100:c#6,77p,13f#6,213p,13f6,213p,13d#6,213p,c#6,77p,a#,77p,13b,213p,13a#,213p,13b,213p,13g#,213p,13a#,213p,13b,213p,a#,77p,c#6,77p,c#6,77p,13f#6,213p,13f6,213p,13d#6,213p,c#6,77p,f#6,77p,13f#6,213p,13g#6,213p,13f#6,213p,13f6,213p,13d#6,213p,13f6,213p,1f#6')

# brainpad specific
# STM32F401RE buzzer pin PB8 is usable with Timer 4, Channel 3
buz_tim = pyb.Timer(4, freq=440)
buz_ch = buz_tim.channel(
    3, pyb.Timer.PWM, pin=pyb.Pin.board.BUZZER, pulse_width=0)

pwm = 30  # reduce this to reduce the volume


def play_tone(freq, msec):
    # general purpose play tone of freq for msec milliseconds
    # only plays for 90% of msec so there are spaces between notes
    # print('freq = {:6.1f} msec = {:6.1f}'.format(freq, msec))
    if freq > 0:
        buz_tim.freq(freq)
        buz_ch.pulse_width_percent(pwm)
    pyb.delay(int(msec * 0.9))
    buz_ch.pulse_width_percent(0)
    pyb.delay(int(msec * 0.1))


def play(tune):
    try:
        for freq, msec in tune.notes():
            play_tone(freq, msec)
    except KeyboardInterrupt:
        play_tone(0, 0)


play(tune)
