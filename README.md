# cyberpad

this is a macro pad inspired by the cyber truck . it has 4 keys , a rotary encoder with a 3d printed knob and a small oled screen . it runs on a xiao rp2040

<!-- ![cyberpad](images/cyberpad.jpg) -->
(image here - finished pad)

## what it does

right now the keys are just w a s d , the knob changes the volume and if you press the knob it mutes . the oled shows the name and what the keys do

the firmware is kmk so you dont have to compile anything , you just edit main.py and save it

## pictures

<!-- ![schematic](images/schematic.png) -->
(image here - schematic)

<!-- ![pcb](images/pcb.png) -->
(image here - pcb)

<!-- ![case](images/case.png) -->
(image here - case)

<!-- ![assembly](images/assembly.jpg) -->
(image here - inside the case)

## key layout

    W  A     knob
    S  D     oled

## parts

- 1 xiao rp2040
- 4 mx switches
- 4 1u keycaps
- 1 ec11 rotary encoder (the one with the push button)
- 1 0.91 inch oled , 128x32 , i2c , ssd1306
- 5 1n4148 diodes , through hole
- 1 pcb
- 1 3d printed case
- 1 3d printed knob
- 3 m3 screws

theres also a BOM.csv from kicad if you want it

## pins

| xiao pin | goes to |
|---|---|
| D0 | col 1 (SW1 , SW4) |
| D1 | col 0 (SW2 , SW3) |
| D2 | row 1 |
| D3 | row 0 |
| D4 | oled SDA |
| D5 | oled SCL |
| D7 | encoder B |
| D8 | encoder A |
| D9 | encoder button |
| 3V3 | oled VCC |
| GND | oled and encoder GND |

the encoder button is part of the key matrix , it goes through D5 to row 0

## how to make it

**pcb**

upload gerbers/cyberpad-gerbers.zip to jlcpcb or where ever you want . its 2 layers , 1.6mm and 72 x 60mm so the normal settings should be fine

**case**

the files are case.step and knob.step in the cad files folder . export them to stl and print them , pla is fine

<!-- ![printed parts](images/printed-parts.jpg) -->
(image here - printed parts)

**soldering**

do the diodes first , the black line goes to the square pad with the K on it . then solder the xiao on the front with the usb facing the edge of the board . after that do the oled (check the pin order matches first) and the encoder . leave the switches till last

<!-- ![soldered pcb](images/soldered.jpg) -->
(image here - soldered pcb)

**firmware**

theres more detail in firmware/README.md but basicly

1. hold boot and plug in the xiao , then put the circuitpython uf2 for the xiao rp2040 on the RPI-RP2 drive
2. copy the kmk folder from https://github.com/KMKfw/kmk_firmware onto the CIRCUITPY drive
3. copy adafruit_display_text and adafruit_displayio_ssd1306.mpy into CIRCUITPY/lib
4. copy firmware/main.py onto the drive

**putting it together**

put the pcb in the case , screw it in with the m3 screws , then put on the keycaps and the knob

## changing the keys

the keys are in keyboard.keymap in firmware/main.py and the knob is in encoder_handler.map . the board restarts when you save

    keyboard.keymap = [
        [
            KC.W,    KC.D,    KC.MUTE,
            KC.A,    KC.S,    KC.NO,
        ],
    ]

the order looks wrong but thats just how the matrix is wired , the comments in main.py explain it

## folders

- pcb - the kicad project
- gerbers - files for the pcb manufacturer
- firmware - the kmk code
- cad files - case , knob and the full assembly
- images - pictures for this readme

## journal

my build log and timelapses are in [journal.md](journal.md)
