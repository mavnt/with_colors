# coding=utf-8
from colorama import Back as _Back
from colorama import Fore as _Fore
from colorama import Style as _Style
from colorama import init as _init

from .utils import get_platform as _get_platform

if _get_platform() == "Windows":
    _init(convert=True)
else:
    _init()

_background_colors = [
    _Back.BLACK,
    _Back.RED,
    _Back.GREEN,
    _Back.YELLOW,
    _Back.BLUE,
    _Back.MAGENTA,
    _Back.CYAN,
    _Back.WHITE,
]
_foreground_colors = [
    _Fore.BLACK,
    _Fore.RED,
    _Fore.GREEN,
    _Fore.YELLOW,
    _Fore.BLUE,
    _Fore.MAGENTA,
    _Fore.CYAN,
    _Fore.WHITE,
]

black, red, green, yellow, blue, magenta, cyan, white = [str(x) for x in range(8)]
_general_colors = [black, red, green, yellow, blue, magenta, cyan, white]
_mapping = {
    k: v for (k, v) in zip(_general_colors, zip(_foreground_colors, _background_colors))
}

dim, normal, bright = _Style.DIM, _Style.NORMAL, _Style.BRIGHT


class background(object):
    def __init__(self, color_: int):
        self.bg = _mapping[color_][1]

    def __enter__(self):
        print(self.bg, end="")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(_Back.RESET, end="")


class color(object):
    def __init__(self, color_):
        self.color = _mapping[color_][0]

    def __enter__(self):
        print(self.color, end="")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(_Fore.RESET, end="")


class style(object):
    def __init__(self, style_: int):
        self.style_ = style_

    def __enter__(self):
        print(self.style_, end="")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(_Style.RESET_ALL, end="")
