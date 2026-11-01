# CYBERPAD firmware (KMK)

## Install
1. Hold BOOT on the XIAO RP2040, plug it in, and drag the CircuitPython `.uf2` for
   "Seeed XIAO RP2040" (from circuitpython.org) onto the `RPI-RP2` drive.
2. The board reappears as `CIRCUITPY`. Download KMK from
   https://github.com/KMKfw/kmk_firmware and copy its `kmk/` folder onto the drive.
3. From the Adafruit CircuitPython library bundle (matching your CircuitPython
   version), copy into `CIRCUITPY/lib/`:
   - `adafruit_display_text/`
   - `adafruit_displayio_ssd1306.mpy`
4. Copy `main.py` onto the drive. The board restarts and runs it.

## Layout
```
[ W ] [ A ]   (knob: turn = volume, press = mute)
[ S ] [ D ]
```
Edit `keyboard.keymap` in `main.py` to change keys.

## Tuning
- Knob runs backwards: change `False` to `True` in `encoder_handler.pins`.
- Volume changes every second click or twice per click: set `encoder_handler.divisor = 2`
  (or 4) before `encoder_handler.pins`.
- Blank OLED: some modules use address `0x3D` instead of `0x3C`.

## PCB notes
- The keymap assumes the fixed board: SW2 pad 1 on `col 0`, SW1 pad 1 on `col 1`.
- The OLED is powered from the XIAO's 3V3 pin.
- U1 uses Seeed's `XIAO-RP2040-DIP` footprint from the project's `xiao.pretty` library.
