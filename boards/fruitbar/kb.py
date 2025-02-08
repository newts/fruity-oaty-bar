import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
# from kmk.quickpin.pro_micro.boardsource_blok import pinout as pins
from kmk.scanners import DiodeOrientation


# GP14,GP15 for the encoder wheel
#
class KMKKeyboard(_KMKKeyboard):
    row_pins = (
#        board.GP17,
#        board.GP18,
#        board.GP19,
#        board.GP20,
#        board.GP21,
#        board.GP22,
        board.GP26,
        board.GP27,
        board.GP28,
    )
    col_pins = (
        board.GP0,
        board.GP1,
        board.GP2,
        board.GP2,
        board.GP3,
        board.GP4,
        board.GP5,
        board.GP6,
        board.GP7,
        # board.GP8,
        # board.GP9,
        # board.GP10,
        # board.GP11,
        # board.GP12,
        # board.GP13,
    )

    # no diodes.  no rollover.
    #    diode_orientation = DiodeOrientation.COLUMNS
    #   led_pin = board.pins[11]

    debug_enabled = True



