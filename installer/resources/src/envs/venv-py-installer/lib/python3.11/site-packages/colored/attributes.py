#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import annotations

from .library import Library
from .utilities import Utilities
from .exceptions import InvalidStyle


class MetaStyle(type):
    """ Overrides AttributeError when __getattr__ called. """
    def __getattr__(cls, color: str):
        raise InvalidStyle(f'{InvalidStyle.__name__}: {color}')


class Style(metaclass=MetaStyle):

    _utils = Utilities()
    _ESC: str = Library.ESC
    _END: str = Library.END
    _STYLES: dict = Library.STYLES
    _UNDER: str = Library.UNDERLINE_COLOR
    _COLORS: dict = Library.COLORS

    for _style, _code in _STYLES.items():
        vars()[_style] = f'{_ESC}{_code}{_END}'
        vars()[_style.upper()] = f'{_ESC}{_code}{_END}'

    @classmethod
    def underline_color(cls, color: str | int) -> str:
        """ Combination with text returns color underline text.
        print(f"{Style.underline_color('red')}White text with red color underline.")

        Args:
            color: Sets the name of the underline color,
                   numbers are also acceptable.

        Returns:
            str: Underline color code.
        """
        color: str = str(color).lower()
        cls._utils.is_color_exist(color)
        if not color.isdigit():
            color: str = cls._COLORS[color]
        return f'{cls._UNDER}{color}{cls._END}'

    @classmethod
    def UNDERLINE_COLOR(cls, color: str | int) -> str:
        """ Combination with text returns color underline text.
        print(f"{Style.underline_color('red')}White text with red color underline.")

        Args:
            color: Sets the name of the underline color,
                         numbers are also acceptable.

        Returns:
            str: Underline color code.
        """
        return cls.underline_color(color)


class style(Style):
    """ This will be deprecated in the future, do not use this for version >= 2.0.0,
        instead please use Style class (See issue #28). """
    pass
