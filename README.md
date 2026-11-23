# cyberpad

This is a cyber deck inspired macro pad that has a amazing oled screen , 4 W A S D  cherry mx keys and a rotary encoder with custom knob made to fit in with the theme that can be 3d printed.

<img width="3296" height="2547" alt="full" src="https://github.com/user-attachments/assets/1f96bfa5-c2e6-4d8f-903c-ec38c8e7eb5a" />

## what it does
Each keys maps to w a s d ,starting from the upper left corner at w and so on. The knob changes the volume and if you press the knob it mutes . The oled screen showsthe name and what the keys do , i might improve this later to add animations or you can do this yourself
The firmware is kmk so you dont have to compile anything , you just edit main.py and save it
## pictures

<img width="3508" height="2480" alt="image" src="https://github.com/user-attachments/assets/2cdca063-0177-4aff-a1e6-bac97b4736f6" />


<img width="301" height="253" alt="Screenshot from 2026-11-07 17-52-26" src="https://github.com/user-attachments/assets/560db10d-5095-4beb-811e-bcf3d96ea4a9" />

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

There is BOM.csv as well if you want to see where i sourced my parts from
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





