# CYBERPAD firmware - KMK on Seeed XIAO RP2040
#
# Hardware (from "macro pad cyber.kicad_pcb"):
#   4x Cherry MX keys + EC11 encoder button in a diode matrix
#   EC11 rotary encoder (A/B), 0.91" 128x32 SSD1306 OLED over I2C
#
# Physical layout (looking at the top of the board):
#
#     [ SW2: W ] [ SW3: A ]   (knob)
#     [ SW1: S ] [ SW4: D ]
#
# Knob turn = volume down/up, knob press = mute.

import board
import busio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.display import Display, TextEntry
from kmk.extensions.display.ssd1306 import SSD1306

keyboard = KMKKeyboard()

# ---------------------------------------------------------------- matrix
# Diode anodes sit on the switch/column side and cathodes on the rows,
# so current flows column -> row.
keyboard.col_pins = (
    board.D1,  # col 0 -> SW3, SW2
    board.D0,  # col 1 -> SW4, SW1
    board.D9,  # EC11 switch (S2); S1 goes through D5 to row 0
)
keyboard.row_pins = (
    board.D3,  # row 0
    board.D2,  # row 1
)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# ---------------------------------------------------------------- encoder
encoder_handler = EncoderHandler()
encoder_handler.pins = (
    # pin A, pin B, button (None: the button is in the matrix), inverted
    (board.D8, board.D7, None, False),
)
encoder_handler.map = [
    ((KC.VOLD, KC.VOLU, KC.NO),),  # layer 0
]
keyboard.modules.append(encoder_handler)
keyboard.extensions.append(MediaKeys())

# ---------------------------------------------------------------- OLED
i2c_bus = busio.I2C(board.D5, board.D4)  # SCL, SDA
display = Display(
    display=SSD1306(i2c=i2c_bus, device_address=0x3C),
    width=128,
    height=32,
    brightness=1,
    dim_time=30,
    dim_target=0.2,
    off_time=300,
)
display.entries = [
    TextEntry(text="CYBERPAD", x=64, y=0, x_anchor="M"),
    TextEntry(text="W A S D", x=64, y=12, x_anchor="M"),
    TextEntry(text="knob: volume", x=64, y=24, x_anchor="M"),
]
keyboard.extensions.append(display)

# ---------------------------------------------------------------- keymap
# KMK numbers keys row by row: index = row * 3 + col
#   0 = row0/col0 = SW2 (top-left)       1 = row0/col1 = SW4 (bottom-right)
#   2 = row0/enc  = knob press           3 = row1/col0 = SW3 (top-right)
#   4 = row1/col1 = SW1 (bottom-left)    5 = row1/enc  = (not wired)
keyboard.keymap = [
    [
        KC.W,    KC.D,    KC.MUTE,
        KC.A,    KC.S,    KC.NO,
    ],
]

if __name__ == '__main__':
    keyboard.go()
