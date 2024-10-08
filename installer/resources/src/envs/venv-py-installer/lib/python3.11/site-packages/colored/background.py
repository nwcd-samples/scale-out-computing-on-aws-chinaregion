#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import annotations

from .library import Library
from .utilities import Utilities
from .exceptions import InvalidColor


class MetaBack(type):
    """ Overrides AttributeError when __getattr__ called. """
    def __getattr__(cls, color: str):
        raise InvalidColor(f'{InvalidColor.__name__}: {color}')


class Back(metaclass=MetaBack):

    _utils = Utilities()
    _END: str = Library.END
    _COLORS: dict = Library.COLORS
    _BACKGROUND_256: str = Library.BACKGROUND_256
    _BACKGROUND_RGB: str = Library.BACKGROUND_RGB

    for _color, _code in _COLORS.items():
        vars()[_color] = f'{_BACKGROUND_256}{_code}{_END}'
        vars()[_color.upper()] = f'{_BACKGROUND_256}{_code}{_END}'

    @classmethod
    def rgb(cls, r: int | str, g: int | str, b: int | str) -> str:
        """ Combination with text returns color background with text.

        Args:
            r: Sets the Red color.
            g: Sets the Green color.
            b: Sets the Blue color.

        Returns:
            str: Background RGB code.
        """
        r, g, b = cls._utils.is_percentage((r, g, b))
        return f'{cls._BACKGROUND_RGB}{r};{g};{b}{cls._END}'

    @classmethod
    def RGB(cls, r: int | str, g: int | str, b: int | str) -> str:
        """ Combination with text returns color background with text.

        Args:
            r: Sets the Red color.
            g: Sets the Green color.
            b: Sets the Blue color.

        Returns:
            str: Background RGB code.
        """
        return cls.rgb(r, g, b)


class back(Back):
    """ This will be deprecated in the future, do not use this for version >= 2.0.0,
        instead please use Back class (See issue #28). """
    pass
