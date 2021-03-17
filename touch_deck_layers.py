from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control_code import ConsumerControlCode

MEDIA = 1
KEY = 2

touch_deck_config = {
    "layers":[
        {
            "name": "Youtube Controls",
            "shortcuts": [
                {
                    "label": "Play",
                    "icon": "touch_deck_icons/pr_play.bmp",
                    "actions": (KEY, [Keycode.K])
                },
                {
                    "label": "Pause",
                    "icon": "touch_deck_icons/pr_pause.bmp",
                    "actions": (KEY, [Keycode.K])
                },
                {
                    "label": "Rewind",
                    "icon": "touch_deck_icons/pr_rewind.bmp",
                    "actions": (KEY, [Keycode.LEFT_ARROW])
                },
                {
                    "label": "FastForward",
                    "icon": "touch_deck_icons/pr_ffwd.bmp",
                    "actions": (KEY, [Keycode.RIGHT_ARROW])
                },
                {
                    "label": "Previous",
                    "icon": "touch_deck_icons/pr_previous.bmp",
                    "actions": (KEY, [Keycode.RIGHT_SHIFT, Keycode.P])
                },
                {
                    "label": "Next",
                    "icon": "touch_deck_icons/pr_next.bmp",
                    "actions": (KEY, [Keycode.RIGHT_SHIFT, Keycode.N])
                },
                {
                    "label": "Vol -",
                    "icon": "touch_deck_icons/pr_voldown.bmp",
                    "actions": (MEDIA, ConsumerControlCode.VOLUME_DECREMENT)
                },
                {
                    "label": "Vol +",
                    "icon": "touch_deck_icons/pr_volup.bmp",
                    "actions": (MEDIA, ConsumerControlCode.VOLUME_INCREMENT)
                },
                                {
                    "label": "Fullscreen",
                    "icon": "touch_deck_icons/pr_fullscreen.bmp",
                    "actions": (KEY, [Keycode.F])
                },
                {
                    "label": "Slow",
                    "icon": "touch_deck_icons/pr_slow.bmp",
                    "actions": (KEY, [Keycode.RIGHT_SHIFT, Keycode.COMMA])
                },
                {
                    "label": "Fast",
                    "icon": "touch_deck_icons/pr_fast.bmp",
                    "actions": (KEY, [Keycode.RIGHT_SHIFT, Keycode.PERIOD])
                },
                {
                    "label": "Mute",
                    "icon": "touch_deck_icons/pr_mute.bmp",
                    "actions": (KEY, [Keycode.M])
                }
            ]
        },
        {
            "name": "Test Second Layer",
            "shortcuts": [
                {
                    "label": "Test (T)",
                    "icon": "touch_deck_icons/test48_icon.bmp",
                    "actions": (KEY, [Keycode.T])
                },
                {
                    "label": "Test (E)",
                    "icon": "touch_deck_icons/test48_icon.bmp",
                    "actions": (KEY, [Keycode.E])
                },
                {
                    "label": "Test (S)",
                    "icon": "touch_deck_icons/test48_icon.bmp",
                    "actions": (KEY, [Keycode.S])
                },
                {
                    "label": "Test (T)",
                    "icon": "touch_deck_icons/test48_icon.bmp",
                    "actions": (KEY, [Keycode.T])
                },
                {
                    "label": "Test [:)]",
                    "icon": "touch_deck_icons/test48_icon.bmp",
                    "actions": (KEY, [Keycode.RIGHT_SHIFT, Keycode.SEMICOLON, Keycode.ZERO])
                }
            ]
        },
        {
            "name": "Test Third Layer",
            "shortcuts": [
                {
                    "label": "Test (3)",
                    "icon": "touch_deck_icons/test48_icon.bmp",
                    "actions": (KEY, [Keycode.THREE])
                },
                {
                    "label": "Test (R)",
                    "icon": "touch_deck_icons/test48_icon.bmp",
                    "actions": (KEY, [Keycode.R])
                },
                {
                    "label": "Test (D)",
                    "icon": "touch_deck_icons/test48_icon.bmp",
                    "actions": (KEY, [Keycode.D])
                },
                {
                    "label": "Test (L)",
                    "icon": "touch_deck_icons/test48_icon.bmp",
                    "actions": (KEY, [Keycode.L])
                },
                {
                    "label": "Test [:)]",
                    "icon": "touch_deck_icons/test48_icon.bmp",
                    "actions": (KEY, [Keycode.RIGHT_SHIFT, Keycode.SEMICOLON, Keycode.ZERO])
                }
            ]
        }
    ]
}