import curses
import sys
import time
import datetime
import array
import json
import piplates.RELAYplate as RELAY
import smtplib
from pathlib2 import Path

def prod(inIdx, inArr):
    retVal = 1
    for idx in range(len(inArr)): 
        if idx != inIdx:
            retVal *= inArr[idx]
    return retVal

def main(src):

    scr = curses.initscr()
    curses.cbreak()
    curses.noecho()
    scr.keypad(1)
    scr.nodelay(1)

    src.addstr(3,1,"woot")

    inArr = [3, 1, 8, 2]
    outArr = []
    for idx in range(len(inArr)):
        outArr.append(prod(idx, inArr))
    
    src.addstr(5, 2, str(outArr))

    scr.refresh()
    time.sleep(10)

    curses.endwin()

if __name__ == '__main__':
    try:
        curses.wrapper(main)
    finally:
        time.sleep(1)
