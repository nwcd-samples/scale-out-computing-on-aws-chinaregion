#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import annotations
import os

from .exceptions import InvalidStyle, InvalidColor, InvalidHexColor, InvalidControl
from .library import Library


class Utilities:

    def __init__(self):
        self._COLORS: dict = Library.COLORS
        self._HEX_COLORS: dict = Library.HEX_COLORS
        self._STYLES: dict = Library.STYLES
        self._CONTROLS: dict = Library.CONTROLS
        self._COLORTERM: dict = Library.COLORTERM
        self.RGB_MAXIMUM_COLOR: int = 255
        self.colorterm: str = 'truecolor'
        self.set_colorterm()

    def is_color_exist(self, name: str) -> bool:
        """ Checks for valid color by name or by hex style name or number,
            and raise a InvalidColor or InvalidHexColor exception if it doesn't exist.

        Args:
            name: Sets the name of the style or the number.

        Returns:
              bool: True if exist.
        """
        if name.startswith('#'):
            if name not in self._HEX_COLORS.values():
                raise InvalidColor(f'{InvalidHexColor.__name__}: {name}')

        elif name not in self._COLORS.keys() and name not in self._COLORS.values():
            raise InvalidColor(f'{InvalidColor.__name__}: {name}')

        return True

    def is_style_exist(self, name: str) -> bool:
        """ Checks for valid style and raise a InvalidStyle exception
            if it doesn't exist.

        Args:
            name: Sets the name of the style or the number.

        Returns:
              bool: True if exist.
        """
        if name not in self._STYLES.keys() and name not in self._STYLES.values():
            raise InvalidStyle(f'{InvalidStyle.__name__}: {name}')

        return True

    def is_control_exist(self, name: str) -> bool:
        """ Checks for valid control and raise a InvalidControl exception
            if it doesn't exist.

        Args:
            name: Sets the name of the control.

        Returns:
              bool: True if exist.
        """
        if name.lower() not in self._CONTROLS.keys():
            raise InvalidControl(f'{InvalidControl.__name__}: {name}')

        return True

    def convert_percentages(self, percent: str | int) -> int | str:
        """ Convert percentages to color number with range 0-255:

        Args:
            percent: Sets the percent number.

        Returns:
            int | str: Returns the number of the range 0-255.
        """
        try:  # Sets maximum range for RGB colors.
            self.RGB_MAXIMUM_COLOR = self._COLORTERM[self.colorterm]
        except KeyError:
            pass

        percentages = {}
        for number in range(self.RGB_MAXIMUM_COLOR + 1):
            percentage = int((number / self.RGB_MAXIMUM_COLOR) * 100)
            percentages[f'{percentage}%'] = number
        try:
            color = percentages[percent]
        except KeyError:
            color = percent[:-1]

        return color

    def set_colorterm(self, colorterm: str = ''):
        """ Set the $COLORTERM environment variable if it's necessary.
        $COLORTERM used to indicate whether a terminal emulator
        could use colors, or whether it supports 8-bit color or more.

        Args:
            colorterm: Sets the $COLORTERM environment variable.
        """
        if not colorterm:
            self.colorterm: str = os.getenv('COLORTERM')
        else:
            self.colorterm: str = colorterm
            os.environ['COLORTERM'] = colorterm

    def is_percentage(self, numbers: tuple) -> list:
        """ Checks a tuple of RGB numbers and convert them to integers.

        Args:
            numbers: Sets percentages of numbers.

        Returns:
            list: List with RGB numbers.
        """
        rgb_list = []
        for num in numbers:
            if str(num).endswith('%'):
                rgb_list.append(self.convert_percentages(str(num)))
            else:
                rgb_list.append(num)
        return rgb_list
