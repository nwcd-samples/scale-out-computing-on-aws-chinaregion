#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .colored import (
    Colored,
    fore, back, style,
    fore_rgb, back_rgb,
    fg, bg, attr, stylize,
    stylize_interactive, set_tty_aware
)

from .cprint import cprint
from .foreground import Fore
from .background import Back
from .attributes import Style
from .controls import Controls


__version__: str = '2.2.3'
