import curses
from curses import wrapper
import time
import random


def main(stdscr):
    #Grab max row and col so we can avoid placing out of bounds
    MAX_LINE = curses.LINES - 1
    MAX_COL = curses.COLS - 1
    stdscr.leaveok(True)
    curses.use_default_colors()
    curses.init_pair(1, 2, 2)
    r_on_w = curses.color_pair(1)
    # Clear screen
    stdscr.clear()
    stdscr.refresh()
    #build box
    stdscr.addstr(0, 0, "╔", r_on_w)
    for i in range(78):
        stdscr.addstr(0, 1 + i, "═", r_on_w)
    stdscr.addstr(0, 79, "╗", r_on_w)
    for i in range(22):
        stdscr.addstr(1+i, 0, "║", r_on_w)
        stdscr.addstr(1+i, 79, "║", r_on_w)
    stdscr.addstr(23, 0, "╚", r_on_w)
    for i in range(78):
        stdscr.addstr(23, 1 + i, "═", r_on_w)
    stdscr.addstr(23, 79, "╝", r_on_w)
    stdscr.refresh()
    pad = curses.newpad(6,78)
    f = open('./assets/gfx/logo.txt')
    data = f.read()
    pad.addstr(data, r_on_w)
    stdscr.addstr(0, 30, "[Manifest V0.1]", r_on_w)
    pad.refresh(0,0,1,7,24,70)
    p_row = 10


    while True:
        key = stdscr.getkey()
        if key == 'a':
            stdscr.addstr(23, 10, "YOU PRESSED 'A' WELL DONE MAN",
             curses.A_RIGHT)
            stdscr.refresh()
        elif key == 'b':
            stdscr.addstr(24, 10, "YOU PRESSED 'B' WELL DONE MAN",
             curses.A_RIGHT)
            stdscr.refresh()
        #test all colors curses can produce
        elif key == 'c':
            pad.erase()
            stdscr.clear()
            for i in range(1, curses.COLORS):
                curses.init_pair(i , i, i)
                stdscr.addstr(str(i), curses.color_pair(i))
            #stdscr.refresh()
        elif key == 'q':
            stdscr.addstr(25, 10, "YOU PRESSED 'B' WELL DONE MAN",
             curses.A_RIGHT)
            exit()
        elif key == 'KEY_UP':
            if p_row == 1:
                pass
            else:
                stdscr.clear()
                stdscr.refresh()
                p_row = p_row - 1
                stdscr.addstr(1, 5, f"p_row : {p_row}", curses.A_ITALIC)
                pad.refresh(0,0 ,p_row, 10 ,p_row + 10,20)
            
        elif key == 'KEY_DOWN':
            if p_row == MAX_LINE - 10:
                pass
            else:
                stdscr.clear()
                stdscr.refresh()
                p_row = p_row + 1
                stdscr.addstr(1, 5, f"p_row : {p_row}", curses.A_ITALIC)
                pad.refresh(0,0 ,p_row, 10 ,p_row + 10,20)
        elif key == 'KEY_LEFT':
            if p_row == MAX_LINE - 10:
                pass
            else:
                stdscr.clear()
                stdscr.refresh()
                p_row = p_row + 1
                stdscr.addstr(1, 5, f"p_row : {p_row}", curses.A_ITALIC)
                pad.refresh(p_row,0 ,10, 10 ,10,20)
wrapper(main)