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
    #stdscr.refresh()
    
def get_input(echo_style, max_size, stdscr):
    """
        Gather input from the user and echo in selected style
    """
    s = echo_style
    ms = max_size
    input = ""
    while True:
        key = stdscr.getch()
        #stdscr.addstr("[" + str(key) + "]", s)
        if key == ord('\n') or key == ord('\r'):
            return input
        elif key == 263:
            if len(input) >= 1:
                (y, x) = curses.getsyx()
                stdscr.move(y, x -1)
                stdscr.addstr(" ", s)
                stdscr.move(y, x -1)
                input = input[:-1]
        elif len(input) == max_size:
            warn_msg("Name Too Long", w_on_r , stdscr)
        else:
            input += chr(key)
            stdscr.addstr(chr(key), s)

def warn_msg(msg, style, stdscr):
    """
        Display warning to user
    """
    box = curses.newpad(6,30)
    draw_box(0, 0, 28, 4, True, style, box)
    box.addstr(2, 5, msg, style)
    box.addstr(0, 10, "[WARNING]", style)
    stdscr.refresh()
    box.refresh(0, 0, 25, 25, 29, 53)
    time.sleep(2)
    box.erase()
    del box
    #box.refresh(0, 0, 23, 15, 29, 43)
    #stdscr.clear()
    stdscr.touchwin()
    stdscr.refresh()

def main(stdscr):
    #Grab max row and col so we can avoid placing out of bounds
    MAX_LINE = curses.LINES - 1
    MAX_COL = curses.COLS - 1
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_WHITE , -1)
    curses.init_pair(2, curses.COLOR_RED, -1)
    curses.init_pair(3, curses.COLOR_GREEN, -1)
    curses.init_pair(4, curses.COLOR_BLUE, -1)
    curses.init_pair(5, curses.COLOR_WHITE , curses.COLOR_BLUE)
    curses.init_pair(6, curses.COLOR_WHITE , curses.COLOR_RED)
    global white
    white = curses.color_pair(1) | curses.A_BOLD
    global red
    red = curses.color_pair(2) | curses.A_BOLD
    global green
    green = curses.color_pair(3) | curses.A_BOLD
    global blue
    blue = curses.color_pair(4) | curses.A_BOLD
    global w_on_b
    w_on_b = curses.color_pair(5) | curses.A_BOLD
    global w_on_r
    w_on_r = curses.color_pair(6) | curses.A_BOLD
    # Clear screen
    stdscr.clear()
    stdscr.refresh()
    draw_box(0, 0, 79, 51, True, green, stdscr)
    for i in range(38):
        draw_box(8, 1 + i, 1 + i, 1 + i, False, red, stdscr)
        time.sleep(.01)
        stdscr.refresh()
    for i in range(38):
        draw_box(45 - i , 1 + i, 1 + i, 1 + i, False, green, stdscr)
        time.sleep(.01)
        stdscr.refresh()
    for i in range(38):
        draw_box(8, 38 - i, 1 + i, 1 + i, True, green, stdscr)
        draw_box(8, 77 - i, 1 + i, 1 + i, True, green, stdscr)
        time.sleep(.01)
        stdscr.refresh()
    pad = curses.newpad(6,78)
    #draw_box(1, 1, 77, 7, False, white, stdscr)
    draw_box(48, 1, 10, 2, True, green, stdscr)
    stdscr.addstr(49, 3, "[S]CAN", green)
    draw_box(48, 12, 10, 2, True, green, stdscr)
    stdscr.addstr(49, 14, "[P]ERMIT", green)
    draw_box(48, 23, 10, 2, True, green, stdscr)
    f = open('./assets/gfx/logo.txt')
    data = f.read()
    f.close()
    for i in range(12):
        pad.clear()
        time.sleep(.25)
        for ch in data:
            rc = random.randint(1,14 - i)
            if rc == 1:
                pad.addstr(ch, red)
            elif rc == 2:
                pad.addstr(ch, green)
            elif rc == 3:
                pad.addstr(ch, blue)
            else:
                pad.addstr(" ", white)
        pad.refresh(0, 0, 2, 7, 25, 70)
    stdscr.addstr(0, 30, "[MANIFEST V0.1]", green)
    stdscr.addstr(8, 5, "[PASSENGER DATA CHIP]", green)
    stdscr.addstr(10, 3, "Name: MAX HEADROOM", green)
    stdscr.addstr(11, 3, "AGE: 49", green)
    stdscr.addstr(12, 3, "SEX: MALE", green)
    stdscr.addstr(12, 3, "Country: United Kingdom", green)
    stdscr.addstr(13, 3, "APPEARANCE:🤨(PUZZLED)", green) 
    stdscr.addstr(14, 3, "APPEARANCE: 🤢 (SICK)", green)
    stdscr.addstr(15, 3, "APPEARANCE: 🥳(READY TO PARTY)", green)
    stdscr.addstr(16, 3, "APPEARANCE: 🥴  (DRUNK)", green)
    #draw_box(20, 10, 20, 5, False, green, stdscr)
    #stdscr.addstr(22, 12, "USERNAME : ", green)
    #user = get_input(green, 5, stdscr)
    #stdscr.addstr(23, 12, user, green)

    while True:
        key = stdscr.getkey()
        if key == 'a':
            warn_msg("INVALID INPUT!", w_on_r, stdscr)
            pad.touchwin()
            pad.refresh(0, 0, 2, 7, 25, 70)
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
            exit()

wrapper(main)


