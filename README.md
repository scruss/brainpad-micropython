# brainpad-micropython
Micropython examples for the BrainPad Classic/BP2  from GHI electronics

In order to use these examples you need to flash the BrainPad with the micropython firmware. You can do that by following the tutorial made by the GHI electronics:

https://www.youtube.com/watch?v=u6MoDpUNQDc&t=433s

## Building/installing Micropython for BrainPad Classic

First, download [micropython/micropython: MicroPython - a lean and efficient Python implementation for microcontrollers and constrained systems](https://github.com/micropython/micropython)

Next, follow the instructions at [dhylands/BRAINPAD: MicroPython board files for the GHI Electronics BrainPad 2 board.](https://github.com/dhylands/BRAINPAD). You can put the board into DFU mode by holding down BOOT0, press and release RESET, then release BOOT0. You should be able to see the device using `dfu-util --list`.

## BrainPad BP2 Schematic

https://drive.google.com/file/d/1eBu7C1-xEknoyc5uRQRy6RmQF5GUclvN/view

(Note that there is another document floating around claiming to be the "BrainPad NetMF" schematic. This is not the same)
