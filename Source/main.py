#! /usr/local/bin/python2
# -*- encoding: utf-8 -*-
#
# Authors: Asger Anders Lund Hansen, Mads Ynddal and Troels Ynddal
# License: See LICENSE file
# GitHub: https://github.com/Baekalfen/PyBoy
#

import traceback
import time
import os.path
import os
import sys
import numpy as np
import platform
from PyBoy.Logger import logger
import argparse

if platform.system() != "Windows":
    from Debug import Debug
from PyBoy import PyBoy


def getWindow(s):
    if not s:
        from PyBoy.GameWindow import SdlGameWindow as Window
    elif s == "sdl2":
        from PyBoy.GameWindow import SdlGameWindow as Window
    elif s == "dummy":
        from PyBoy.GameWindow import DummyGameWindow as Window
    else:
        print("Invalid arguments!")
        exit(1)

    return Window


def getROM(ROMdir):
    # Give a list of ROMs to start
    found_files = filter(lambda f: f.lower().endswith(
        ".gb") or f.lower().endswith(".gbc"), os.listdir(ROMdir))
    for i, f in enumerate(found_files):
        print ("%s\t%s" % (i + 1, f))
    filename = input("Write the name or number of the ROM file:\n")

    try:
        filename = ROMdir + found_files[int(filename) - 1]
    except:
        filename = ROMdir + filename

    return filename


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Gameboy emulator.')
    parser.add_argument('--game_name', type=str, help='Game filename (without ROMs)', default='Tetris.gb')
    parser.add_argument('--window', type=str, help='Game window type', default='sdl2')
    args = parser.parse_args()
    
    bootROM = None
    ROMdir = "ROMs/"
    scale = 1

    # Verify directories
    if not os.path.exists(ROMdir):
        print ("ROM folder not found. Please copy the Game-ROM to '%s'" % ROMdir)
        exit()

    filename = os.path.join(ROMdir, args.game_name)
    print(filename)

    try:
        # Start PyBoy and run loop
        pyboy = PyBoy((getWindow(args.window))(scale=scale), filename, bootROM)
        while not pyboy.tick():
            pass
        pyboy.stop()

    except KeyboardInterrupt:
        print ("Interrupted by keyboard")
    except Exception as ex:
        traceback.print_exc()
        # time.sleep(10)
    # finally:
    #     if debugger:
    #         logger.info("Debugger ready for shutdown")
    #         time.sleep(10)
    #         debugger.quit()
