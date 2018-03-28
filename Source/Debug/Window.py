# -*- encoding: utf-8 -*-
#
# Authors: Mads Ynddal
# License: See LICENSE file
# GitHub: https://github.com/Baekalfen/PyBoy
#
import Debug.GenericScreen as GenericScreen
import curses

class Window(GenericScreen.GenericScreen):
    def __init__(self, line_column, sz):
        self._screen = curses.newwin(sz[0],sz[1],line_column[0],line_column[1])



