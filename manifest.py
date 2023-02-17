import curses
from curses import wrapper
import time
import random

def draw_box(line, col, width, height, fill, style, stdscr):
    """
        Draw a window, takes starting position line & col.
        If fill is set True then insert spaces to fill window
        Width and height for size and style is curses color pairing.
        Also takes curses screen we need to use
    """
    l = int(line)
    c = int(col)
    w = int(width)
    h = int(height)
    s = style
    f = fill
    stdscr.addstr(l, c, "╔", s)
    for i in range(w - 1):
        stdscr.addstr(l, c  + 1 + i, "═", s)
    stdscr.addstr(l, c + w , "╗", s)
    for i in range(h - 1):
        stdscr.addstr(l + 1 + i, c, "║", s)
        if(fill):
            for x in range(w - 1):
                stdscr.addstr(l + 1 + i, c + 1 + x, " ", s)
        stdscr.addstr(l + 1 + i, c + w, "║", s)
    stdscr.addstr(l + h, c, "╚", s)
    for i in range(w - 1):
        stdscr.addstr(l + h, c + 1 + i, "═", s)
    stdscr.addstr(l + h , c + w , "╝", s)
    stdscr.refresh()
    

def main(stdscr):
    #Grab max row and col so we can avoid placing out of bounds
    MAX_LINE = curses.LINES - 1
    MAX_COL = curses.COLS - 1
    curses.start_color()
    curses.use_default_colors()
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_WHITE , -1)
    curses.init_pair(2, curses.COLOR_RED, -1)
    curses.init_pair(3, curses.COLOR_GREEN, -1)
    curses.init_pair(4, curses.COLOR_BLUE, -1)
    curses.init_pair(5, curses.COLOR_WHITE , curses.COLOR_BLUE)
    white = curses.color_pair(1) | curses.A_BOLD
    red = curses.color_pair(2) | curses.A_BOLD
    green = curses.color_pair(3) | curses.A_BOLD
    blue = curses.color_pair(4) | curses.A_BOLD
    w_on_b = curses.color_pair(5) | curses.A_BOLD
    # Clear screen
    stdscr.clear()
    stdscr.refresh()
    draw_box(0, 0, 79, 51, True, red, stdscr)
    for i in range(38):
        draw_box(8, 1 + i, 1 + i, 1 + i,False, red, stdscr)
        time.sleep(.01)
        stdscr.refresh()
    for i in range(38):
        draw_box(45 -i , 1 + i, 1 + i, 1 + i, False, green, stdscr)
        time.sleep(.01)
        stdscr.refresh()
    for i in range(38):
        draw_box(9, 38 - i, 1 + i, 1 + i, True, red, stdscr)
        draw_box(9, 77 - i, 1 + i, 1 + i, True, red, stdscr)
        time.sleep(.01)
        stdscr.refresh()
    pad = curses.newpad(6,78)
    draw_box(1, 1, 77, 7, True, white, stdscr)
    draw_box(48, 1, 10, 2, True, w_on_b, stdscr)
    stdscr.addstr(49, 3, "[S]CAN", red)
    draw_box(48, 12, 10, 2, True, w_on_b, stdscr)
    stdscr.addstr(49, 14, "[P]ERMIT", red)
    draw_box(48, 23, 10, 2, True, w_on_b, stdscr)
    f = open('./assets/gfx/logo.txt')
    data = f.read()
    for i in range(30):
        for ch in data:
            rc = random.randint(1,32 - i)
            if rc == 1:
                pad.addstr(ch, red)
            elif rc == 2:
                pad.addstr(ch, green)
            elif rc == 3:
                pad.addstr(ch, blue)
            else:
                pad.addstr(" ", white)
        pad.refresh(0, 0, 2, 7, 25,70)
        time.sleep(.1)
        pad.clear()
    stdscr.addstr(0, 30, "[Manifest V0.1]", red)
    stdscr.addstr(10, 3, "Name: MAX HEADROOM", red)
    stdscr.addstr(11, 3, "AGE: 49", red)
    stdscr.addstr(12, 3, "SEX: MALE", red)


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
                curses.init_pair(i , -1, i)
                stdscr.addstr(str(i), curses.color_pair(i))
            stdscr.addstr("\nThese are the available colors\n")
            for i in range(1, curses.COLORS):
                curses.init_pair(i , 1, i)
                stdscr.addstr(str(i), curses.color_pair(i) | curses.A_BOLD)
            stdscr.addstr("\nThese are the available colors in BOLD\n")
            for i in range(1, curses.COLORS):
                curses.init_pair(i , 1, i)
                stdscr.addstr(str(i), curses.color_pair(i) | curses.A_DIM)
            stdscr.addstr("\nThese are the available colors in DIM\n")
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


