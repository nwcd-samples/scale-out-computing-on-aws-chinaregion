#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .library import Library
from .utilities import Utilities
from .exceptions import InvalidControl


class Controls:

    def __init__(self):
        self._utils = Utilities()
        self._ESC: str = Library.ESC
        self._CONTROLS: dict = Library.CONTROLS

    def nav(self, name: str, row: int, column=None) -> str:
        """ Moves the cursor n (default 1) cells in the given direction.
            If the cursor is already at the edge of the screen, this has no effect.
            Reference: https://en.wikipedia.org/wiki/ANSI_escape_code#CSI

        Args:
            name: type of moves. (See library.py).
            row: number of rows.
            column: number of columns.

        Returns:
            ESC[ row A: Cursor Up
            ESC[ row B: Cursor Down
            ESC[ row C: Cursor Forward
            ESC[ row D: Cursor Back
            ESC[ row E: Cursor Next Line
            ESC[ row F: Cursor Previous Line
            ESC[ row G: Cursor Horizontal Absolute
            ESC[ row; col; H: Cursor Position
            ESC[ row J: Erase in Display
            ESC[ row K: Erase in Line
            ESC[ row S: Scroll Up
            ESC[ row T: Scroll Down

        Raises:
            InvalidControl: Raises an Exception.
        """
        self._is_str_object(name)
        self._utils.is_control_exist(name)

        if column:
            if name.lower() == 'position':
                return f'{self._ESC}{row};{column}{self._CONTROLS[name.lower()]}'
            else:
                raise InvalidControl(f"{InvalidControl.__name__}: {name}: Expected 'position'")

        return f'{self._ESC}{row}{self._CONTROLS[name.lower()]}'

    @staticmethod
    def _is_str_object(move: str) -> None:
        if not isinstance(move, str):
            raise AttributeError("'str' object required")
