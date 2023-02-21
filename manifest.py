import curses
from curses import wrapper
import time
import random

global ANI_DLA
ANI_DLA = 0.05
global DIFFICULTY
DIFFICULTY = "CHAOS"

def draw_box(line, col, width, height, fill, style, stdscr):
    """
        Draw a window, takes starting position line & col.
        If fill is set True then insert spaces to fill window
        Width and height for size and style is curses color pairing.
        Also takes curses screen/pad we need to use
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
        stdscr.refresh()
        key = stdscr.getch()
        #stdscr.addstr(2, 2, "[" + str(key) + "]", s)
        if key == ord('\n') or key == ord('\r'):
            input = input.upper()
            return input
        elif key == 127:
            if len(input) >= 1:
                (y, x) = curses.getsyx()
                stdscr.move(y, x -1)
                stdscr.addstr(" ", s)
                stdscr.move(y, x -1)
                input = input[:-1]
        elif len(input) == max_size:
            warn_msg("INPUT LIMIT REACHED", w_on_r , stdscr)
        else:
            input += chr(key)
            screen_key = chr(key)
            screen_key = screen_key.upper()
            stdscr.addstr(screen_key, s)

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


def decrypt_record_game(stdscr):
    """
        Player gets 5 chances to work out the encryption key
    """
    drgwin = curses.newwin(52,81)
    draw_box(0, 0, 79, 51, True, blue, drgwin)
    drgwin.addstr(0, 25, "[MANIFEST RECORD DECRYPTION]", blue )
    drgwin.refresh()
    #Use alfanum file to create random key based on difficulty setting
    f = open('./assets/data/alfanum.txt')
    data = f.read()
    f.close()
    ekey = ""
    if DIFFICULTY == "MINOR":
        dud_keys = 15
        for i in range(5):
            ekey += data[random.randint(0, (len(data) - 1))]
    if DIFFICULTY == "MAJOR":
        dud_keys = 25
        for i in range(8):
            ekey += data[random.randint(0, (len(data) - 1))]
    if DIFFICULTY == "CHAOS":
        dud_keys = 35
        for i in range(12):
            ekey += data[random.randint(0, (len(data) - 1))]            
    gp = curses.newpad(51, 76)
    junk_data = ["0", "1"]
    for i in range(40):
        drgwin.move(4 +i, 2)
        for i in range(76):
            drgwin.addstr(str(random.randint(0, 1)), white)
    line_pos = random.randint(4, 43)
    row_pos = random.randint(2, (76 - len(ekey)))
    used_locs = []
    used_locs.append((line_pos, row_pos))
    drgwin.addstr(line_pos, row_pos, ekey, blue)
    #insert the other invalid keys
    used_keys = []
    for keys in range(dud_keys):
        #Create a temp key the same size as the actual ekey
        #Check if key has already been generated
        duplicate_key = True
        while duplicate_key:
            t_k = ''
            for char in range(len(ekey)):
                t_k += data[random.randint(0, (len(data) - 1))]
            if t_k not in used_keys:
                duplicate_key = False
                used_keys.append(t_k)
        #find somewhere to insert it that doesn't clash
        look_for_loc = True
        while look_for_loc:
            #create a new random location
            line_pos = random.randint(4, 43)
            row_pos = random.randint(2, (76 - len(ekey)))
            #check if line is empty
            line_used = False
            for i in range(len(used_locs)):
                l, r = used_locs[i]
                if line_pos == l:
                    line_used = True
            if line_used != True:
                look_for_loc = False
                break
        drgwin.addstr(line_pos, row_pos, t_k, blue)
        used_locs.append((line_pos, row_pos))
    correct_key = False
    for i in range(5):
        draw_box(45, 2, 40, 4, True, blue, drgwin)
        drgwin.addstr(45, 11, "[KEY VERIFICATION]", blue)
        drgwin.addstr(47, 11, "ENTER KEY: ", blue)
        drgwin.refresh()
        key_selection = get_input(blue, len(ekey), drgwin)
        #drgwin.refresh()
        drgwin.addstr(45  + i, 45, "ATTEMPT " + str(i + 1) + " : ", blue)
        for i in range(len(key_selection)):
            if key_selection[i] not in ekey:
                drgwin.addstr(key_selection[i], red)
            elif key_selection[i] == ekey[i]:
                drgwin.addstr(key_selection[i], green)
            else:
                drgwin.addstr(key_selection[i], YELLOW)
        if key_selection == ekey:
                correct_key = True
                break
    if correct_key:
        draw_box(45, 2, 40, 4, True, green, drgwin)
        drgwin.addstr(45, 11, "[KEY VERIFICATION]", green)
        drgwin.addstr(47, 12, "VALID KEY FOUND!", green)
        drgwin.refresh()
    else:
        draw_box(45, 2, 40, 4, True, red, drgwin)
        drgwin.addstr(45, 11, "[KEY VERIFICATION]", red)
        drgwin.addstr(47, 10, "NO VALID KEY FOUND!", green)
        drgwin.refresh()
    
    time.sleep(2)
    drgwin.clear()
    del drgwin
    stdscr.touchwin()
    stdscr.refresh()



def main(stdscr):
    """
        Primary startup function, which displays logo and menu
    """
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_WHITE , -1)
    curses.init_pair(2, curses.COLOR_RED, -1)
    curses.init_pair(3, curses.COLOR_GREEN, -1)
    curses.init_pair(4, curses.COLOR_BLUE, -1)
    curses.init_pair(5, curses.COLOR_WHITE , curses.COLOR_BLUE)
    curses.init_pair(6, curses.COLOR_WHITE , curses.COLOR_RED)
    curses.init_pair(7, curses.COLOR_YELLOW, -1)
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
    global YELLOW
    YELLOW = curses.color_pair(7) | curses.A_BOLD
    # Clear screen
    stdscr.clear()
    stdscr.refresh()
    #read in logo and animate display
    f = open('./assets/gfx/logo.txt')
    data = f.read()
    f.close()
    for i in range(24):
        stdscr.move(25 -i, 7)
        time.sleep(ANI_DLA)
        new_r_count = 0
        start_line = 1
        for ch in data:
            if new_r_count >= (len(data) / 6):
                stdscr.move(((25 - i) + start_line), 7)
                new_r_count = 0
                start_line += 1
            rc = random.randint(1,26 - i)
            if rc == 1:
                stdscr.addstr(ch, red)
            elif rc == 2:
                stdscr.addstr(ch, green)
            elif rc == 3:
                stdscr.addstr(ch, blue)
            else:
                stdscr.addstr(" ", white)
            new_r_count = new_r_count + 1
        stdscr.refresh()
    draw_box(0, 0, 79, 51, False, green, stdscr)
    stdscr.addstr(0, 30, "[ MANIFEST V0.2 ]", green)
    for i in range(20):
        draw_box(16, 18, 1 + (i*2), 1 + i, False, red, stdscr)
        draw_box(17, 19, -1 + (i*2), -1 + i, False, green, stdscr)
        draw_box(18, 20, -3 + (i*2), -3 + i, False, blue, stdscr)
        time.sleep(ANI_DLA)
        #draw_box(line, col, width, height, fill, style, stdscr)
        stdscr.refresh()
    stdscr.addstr(17, 31, "[ MAIN MENU ]", green)
    stdscr.addstr(31, 25, "[ ", white)
    stdscr.addstr("N", YELLOW)
    stdscr.addstr("EW GAME ]", white)
    stdscr.addstr(33, 30, "[ ", white)
    stdscr.addstr("Q", YELLOW)
    stdscr.addstr("UIT GAME ]", white)
    stdscr.addstr(44, 16, "TYPE THE FIRST LETTER OF AN OPTION TO SELECT", white)
    stdscr.refresh()
    while True:
        key = stdscr.getkey()
        #stdscr.addstr(0, 0, key)
        if key == 'N' or key == 'n':
            #launch main game function
            break
        elif key == 'Q' or key == 'q':
            exit()

    for i in range(38):
        draw_box(8, 1 + i, 1 + i, 1 + i, False, red, stdscr)
        time.sleep(ANI_DLA)
        stdscr.refresh()
    for i in range(38):
        draw_box(45 - i , 1 + i, 1 + i, 1 + i, False, green, stdscr)
        time.sleep(ANI_DLA)
        stdscr.refresh()
    for i in range(38):
        draw_box(8, 38 - i, 1 + i, 1 + i, True, green, stdscr)
        draw_box(8, 77 - i, 1 + i, 1 + i, True, green, stdscr)
        time.sleep(ANI_DLA)
        stdscr.refresh()

    #draw_box(1, 1, 77, 7, False, white, stdscr)
    draw_box(48, 1, 10, 2, True, green, stdscr)
    stdscr.addstr(49, 3, "[S]CAN", green)
    draw_box(48, 12, 10, 2, True, green, stdscr)
    stdscr.addstr(49, 14, "[P]ERMIT", green)
    draw_box(48, 23, 10, 2, True, green, stdscr)
    
    stdscr.addstr(8, 3, "[SUBDERMAL IMPLANT DATA]", green)
    stdscr.addstr(8, 42, "[SHIP MANIFEST DATA]", green)
    stdscr.addstr(10, 3, "NAME: MAX HEADROOM", green)
    stdscr.addstr(11, 3, "AGE: 49", green)
    stdscr.addstr(12, 3, "SEX: MALE", green)
    stdscr.addstr(12, 3, "COUNTRY: United Kingdom", green)
    stdscr.addstr(13, 3, "MOOD: 🤨 (PUZZLED)", green) 
    stdscr.addstr(14, 3, "MOOD: 🤢 (SICK)", green)
    stdscr.addstr(15, 3, "MOOD: 🥳 (READY TO PARTY)", green)
    stdscr.addstr(16, 3, "MOOD: 🥴 (INEBRIATED)", green)
    stdscr.addstr(17, 3, "MOOD: 🥺 (WORRIED)", green)
    stdscr.addstr(18, 3, "MOOD: 😶 (UNAVAILABLE)", green)
    #stdscr.addstr(19, 3, "Type here: ", green)
    #userstuff = get_input(green, 10, stdscr)
    #draw_box(20, 10, 20, 5, False, green, stdscr)
    #stdscr.addstr(22, 12, "USERNAME : ", green)
    #user = get_input(green, 5, stdscr)
    #stdscr.addstr(23, 12, user, green)

    while True:
        key = stdscr.getkey()
        #stdscr.addstr(0, 0, key)
        if key == 'a':
            warn_msg("INVALID INPUT!", w_on_r, stdscr)
            pad.touchwin()
            pad.refresh(0, 0, 2, 7, 25, 70)
            stdscr.refresh()
        elif key == 'c' or key == 'C':
            decrypt_record_game(stdscr)
        elif key == 'q' or key == 'Q':
            exit()

wrapper(main)