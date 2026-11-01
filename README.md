# CYBERPAD

A sleek, Cybertruck-inspired macro pad with 4 mechanical keys, a rotary encoder with a 3D-printed knob, and a 0.91" OLED screen, powered by a Seeed XIAO RP2040.

<!-- IMAGE: hero shot of the finished CYBERPAD -->
<!-- ![CYBERPAD](images/cyberpad.jpg) -->
> 📷 _Image coming soon: finished CYBERPAD_

## Features

- **4 Cherry MX-compatible keys**: set up as W / A / S / D out of the box
- **EC11 rotary encoder**: turn for volume, press to mute
- **0.91" 128×32 OLED** for status text
- **Seeed XIAO RP2040** running [KMK](https://github.com/KMKfw/kmk_firmware). There's nothing to compile: edit `main.py` and save.
- **3D-printed angular case and knob** inspired by the Cybertruck

## Gallery

<!-- IMAGE: KiCad schematic -->
<!-- ![Schematic](images/schematic.png) -->
> 📷 _Image coming soon: schematic_

<!-- IMAGE: KiCad PCB layout / 3D view -->
<!-- ![PCB](images/pcb.png) -->
> 📷 _Image coming soon: PCB layout_

<!-- IMAGE: case render from Onshape -->
<!-- ![Case](images/case.png) -->
> 📷 _Image coming soon: case render_

<!-- IMAGE: assembled board inside the case -->
<!-- ![Assembly](images/assembly.jpg) -->
> 📷 _Image coming soon: assembly_

## Layout

```
 ┌─────┬─────┐   ◎ knob
 │  W  │  A  │     turn  = volume down / up
 ├─────┼─────┤     press = mute
 │  S  │  D  │
 └─────┴─────┘   [ OLED ]
```

## Bill of materials

| Qty | Part | Notes |
|---|---|---|
| 1 | Seeed XIAO RP2040 | Through-hole, soldered with pin headers or directly |
| 4 | Cherry MX-compatible switches | Any 3-pin or 5-pin MX switch |
| 4 | 1u keycaps | MX stem |
| 1 | EC11 rotary encoder with push switch | |
| 1 | 0.91" 128×32 I²C OLED (SSD1306) | Pin order GND, VCC, SCL, SDA |
| 5 | 1N4148 diodes (DO-35, through-hole) | |
| 1 | CYBERPAD PCB | From `gerbers/cyberpad-gerbers.zip` |
| 1 | 3D-printed case | `cad files/case.step` |
| 1 | 3D-printed knob | `cad files/knob.step` |
| 3 | M3 screws | Mounting holes |

The KiCad parts list is in [`BOM.csv`](BOM.csv).

## Wiring

The keys and the encoder button are in a 2-row diode matrix (diodes point column → row).

| XIAO pin | Signal | Connected to |
|---|---|---|
| D0 | col 1 | SW1, SW4 |
| D1 | col 0 | SW2, SW3 |
| D2 | row 1 | via D2, D4 |
| D3 | row 0 | via D1, D3, D5 |
| D4 | SDA | OLED |
| D5 | SCL | OLED |
| D7 | Encoder B | EC11 |
| D8 | Encoder A | EC11 |
| D9 | Encoder switch | EC11 (through D5 to row 0) |
| 3V3 | OLED VCC | OLED |
| GND | GND | OLED, encoder common |

## Building one

### 1. Order the PCB
Upload [`gerbers/cyberpad-gerbers.zip`](gerbers/cyberpad-gerbers.zip) to any PCB fab (JLCPCB, PCBWay, etc.). The default settings work: 2 layers, 1.6 mm, 72 × 60 mm.

### 2. Print the case and knob
Export `cad files/case.step` and `cad files/knob.step` to STL and print. PLA works fine.

<!-- IMAGE: printed parts -->
<!-- ![Printed parts](images/printed-parts.jpg) -->
> 📷 _Image coming soon: printed parts_

### 3. Solder
1. **Diodes D1–D5**: the black stripe (cathode) goes to the square pad marked **K**.
2. **XIAO RP2040**: solder it flat on the front, USB facing the board edge.
3. **OLED**: check the pin order (GND, VCC, SCL, SDA) matches the silkscreen.
4. **Rotary encoder**
5. **Switches**: last, so they sit flush with the case plate.

<!-- IMAGE: soldered PCB -->
<!-- ![Soldered PCB](images/soldered.jpg) -->
> 📷 _Image coming soon: soldered PCB_

### 4. Flash the firmware
Full steps are in [`firmware/README.md`](firmware/README.md). Short version:
1. Hold **BOOT**, plug in the XIAO, and drop the CircuitPython `.uf2` for the XIAO RP2040 onto the `RPI-RP2` drive.
2. Copy the `kmk/` folder from [KMK](https://github.com/KMKfw/kmk_firmware) onto the `CIRCUITPY` drive.
3. Copy `adafruit_display_text/` and `adafruit_displayio_ssd1306.mpy` into `CIRCUITPY/lib/`.
4. Copy [`firmware/main.py`](firmware/main.py) onto the drive.

### 5. Assemble
Put the PCB in the case, screw it down with M3 screws, then fit the keycaps and push the knob onto the encoder.

## Customizing

Keys are set in `keyboard.keymap` in `firmware/main.py`. Knob actions are in `encoder_handler.map`. Save the file and the board restarts with the new layout.

```python
keyboard.keymap = [
    [
        KC.W,    KC.D,    KC.MUTE,
        KC.A,    KC.S,    KC.NO,
    ],
]
```

## Repo layout

| Folder | What's in it |
|---|---|
| `pcb/` | KiCad project (schematic, PCB, XIAO RP2040 footprint library). Open `macro pad cyber.kicad_pro`. |
| `gerbers/` | Manufacturing files. Upload `cyberpad-gerbers.zip` to your PCB fab. |
| `firmware/` | KMK firmware for the XIAO RP2040. See `firmware/README.md`. |
| `cad files/` | 3D case, knob and full assembly (STEP). |
| `BOM.csv` | Parts list. |

## Build log

The full design journal, with timelapses, is in [`journal.md`](journal.md).
