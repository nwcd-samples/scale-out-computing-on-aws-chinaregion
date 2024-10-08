#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import annotations

from .colored import Colored
from .colored import fore_rgb as foreground_rgb
from .colored import back_rgb as background_rgb


def cprint(text: str,
           fore_256: int | str = '',
           back_256: int | str = '',
           fore_rgb: tuple = (255, 255, 255),
           back_rgb: tuple = (0, 0, 0),
           formatting: int | str = '',
           line_color: int | str = '',
           reset=True,
           **kwargs) -> None:
    """ Looks like a patch to a built-in python print() function that allows
    to pass colored text and style, to this function.

    Args:
        text: String type text.
        fore_256: Sets the foreground color.
        back_256: Sets the background color.
        fore_rgb: Sets the foreground color.
        back_rgb: Sets the background color.
        formatting: Sets the style of the text.
        line_color: Sets the underline color.
        reset: Resets the formatting style after print, default is True.
    """
    fore_color: str = Colored(fore_256).foreground()
    back_color: str = Colored(back_256).background()
    styling: str = Colored(formatting).attribute(line_color)
    terminator: str = Colored('reset').attribute() if reset else ''

    if not fore_256:
        fR, fG, fB = fore_rgb
        fore_color: str = foreground_rgb(fR, fG, fB)

    if not back_256:
        bR, bG, bB = back_rgb
        back_color: str = background_rgb(bR, bG, bB)

    print(f'{styling}{back_color}{fore_color}{text}{terminator}', **kwargs)
