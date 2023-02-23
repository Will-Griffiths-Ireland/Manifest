import curses
from curses import wrapper
import time
import random
import threading

# Animation delay setting
ANI_DLA = 0.1
DIFFICULTY = "MINOR"
P_NAME = ""
# Decryption game active flag
DRG_ACT = False
# Cursor postion storage
G_CUR_YX = (0, 0)
# Passenger data
MALE_NAMES = []
FEMALE_NAMES = []
COUNTRY_NAMES = []
# Dialog responses
P_APPR_ACT = []
P_SCAN_RESP = []
SO_WELC = []
SO_SCAN_REQ = []


def gen_data_lists(stdscr):
    """
        Gen lists
    """
    global MALE_NAMES
    global FEMALE_NAMES
    global COUNTRY_NAMES
    global P_APPR_ACT
    global SO_WELC
    global SO_SCAN_REQ
    global P_SCAN_RESP

    P_SCAN_RESP = []
    f = open('./assets/data/passenger_scan_response.txt')
    data = f.read().splitlines()
    f.close()
    for line in data:
        P_SCAN_RESP.append(line.upper())

    SE_SCAN_REQ = []
    f = open('./assets/data/secoff_scan_request')
    data = f.read().splitlines()
    f.close()
    for line in data:
        SO_SCAN_REQ.append(line.upper())

    SO_WELC = []
    f = open('./assets/data/secoff_welcome.txt')
    data = f.read().splitlines()
    f.close()
    for line in data:
        SO_WELC.append(line.upper())

    P_APPR_ACT = []
    f = open('./assets/data/passenger_approach.txt')
    data = f.read().splitlines()
    f.close()
    for line in data:
        P_APPR_ACT.append(line.upper())

    MALE_NAMES = []
    f = open('./assets/data/male_names.txt')
    data = f.read().splitlines()
    f.close()
    for line in data:
        MALE_NAMES.append(line.upper())

    FEMALE_NAMES = []
    f = open('./assets/data/female_names.txt')
    data = f.read().splitlines()
    f.close()
    for line in data:
        FEMALE_NAMES.append(line.upper())
    
    COUNTRY_NAMES = []
    f = open('./assets/data/country_names.txt')
    data = f.read().splitlines()
    f.close()
    for line in data:
        COUNTRY_NAMES.append(line.upper())


def set_game(stdscr):
    # pick diff
    # give name
    pass


def draw_action_buttons(stdscr):
    """
        Draw 'buttons' with actions the player can take
    """
    draw_box(48, 7, 14, 2, True, GREEN, stdscr)
    stdscr.addstr(49, 12, "B", GREEN)
    stdscr.addstr("OARD", WHITE)
    stdscr.refresh()
    time.sleep(.25)
    draw_box(48, 23, 14, 2, True, YELLOW, stdscr)
    stdscr.addstr(49, 28, "R", YELLOW)
    stdscr.addstr("EJECT", WHITE)
    stdscr.refresh()
    time.sleep(.25)
    draw_box(48, 39, 14, 2, True, RED, stdscr)
    stdscr.addstr(49, 43, "A", RED)
    stdscr.addstr("RREST", WHITE)
    stdscr.refresh()
    time.sleep(.25)
    draw_box(48, 55, 14, 2, True, BLUE, stdscr)
    stdscr.addstr(49, 59, "D", BLUE)
    stdscr.addstr("ECRYPT", WHITE)

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
        if (f):
            for x in range(w - 1):
                stdscr.addstr(l + 1 + i, c + 1 + x, " ", s)
        stdscr.addstr(l + 1 + i, c + w, "║", s)
    stdscr.addstr(l + h, c, "╚", s)
    for i in range(w - 1):
        stdscr.addstr(l + h, c + 1 + i, "═", s)
    stdscr.addstr(l + h , c + w , "╝", s)


def get_input(echo_style, max_size, stdscr):
    """
        Gather input from the user and echo in selected style
        Escape is 27
        Backspace is 127
        Space is 32
    """
    global DRG_ACT
    global G_CUR_YX
    s = echo_style
    ms = max_size
    user_input = ""
    valid_keys = []

    f = open("./assets/data/alfanum.txt", "r")
    data = f.read()
    f.close()
    for ch in data:
        valid_keys.append(ch)

    while True and DRG_ACT is True:
        try:
            key = stdscr.getch()
            #key_as_char = str(chr(key))
            #stdscr.addstr(0,0, str(key), RED)
            if DRG_ACT is False:
                break
            if key == ord('\n') or key == ord('\r'):
                user_input = user_input.upper()
                return user_input
            if key == 127 or key == ord('\b'):
                if len(user_input) >= 1:
                    if DRG_ACT is True:
                        (y, x) = G_CUR_YX
                        G_CUR_YX = (y, x - 1)
                    else:
                        (y, x) = curses.getsyx()
                    stdscr.move(y, x - 1)
                    stdscr.addstr(" ", s)
                    stdscr.move(y, x - 1)
                    user_input = user_input[:-1]
            elif len(user_input) == max_size:
                warn_msg("INPUT LIMIT REACHED", W_ON_R , stdscr)
            elif chr(key).upper() in valid_keys:
                if DRG_ACT is True:
                    (y, x) = G_CUR_YX
                    G_CUR_YX = (y, x + 1)
                user_input += chr(key)
                screen_key = chr(key)
                screen_key = screen_key.upper()
                stdscr.addstr(screen_key, s)
            else:
                warn_msg("     INVALID KEY", W_ON_R , stdscr)
        except:
            pass
def warn_msg(msg, style, stdscr):
    """
        Display warning to user
    """
    box = curses.newpad(6,30)
    draw_box(0, 0, 28, 4, True, style, box)
    box.addstr(2, 5, msg, style)
    box.addstr(0, 10, "[ WARNING ]", style)
    stdscr.refresh()
    box.refresh(0, 0, 25, 25, 29, 53)
    time.sleep(2)
    curses.flushinp()
    box.erase()
    del box
    stdscr.touchwin()
    stdscr.refresh()


def countdown(stdscr):
    """
        Countdown timer
    """
    global DRG_ACT
    timelimit = 60
    blank_line = "   "
    for i in range(timelimit):
        blank_line += " "
    while DRG_ACT is True:
        bar_line = ""
        for i in range(timelimit):
            bar_line += "#"
        if timelimit == 0:
            # ran out of time!!
            blank_line = ""
            for i in range(70):
                blank_line += " "
            stdscr.addstr(2, 4, blank_line, GREEN )
            stdscr.addstr(3, 4, blank_line, GREEN )
            stdscr.addstr(2, 30, "RECORD PERMA LOCKED!", RED )
            stdscr.addstr(3, 29, "HIT ANY KEY TO RETURN", RED )
            stdscr.refresh()
            DRG_ACT = False
            break
        stdscr.addstr(2, 4, "SEGMENTED MEMORY LOCKOUT EXPIRING IN ...", BLUE )
        stdscr.addstr(3, 4, blank_line, GREEN )
        if timelimit > 40:
            stdscr.addstr(3, 4, str(timelimit) + " " + bar_line, GREEN )
        elif timelimit > 19 and timelimit <= 40:
            stdscr.addstr(3, 4, str(timelimit) + " " + bar_line, YELLOW )
        else:
            stdscr.addstr(3, 4, str(timelimit) + " " + bar_line, RED)
        stdscr.refresh()
        # Put the cursor back to where it was for input
        (y, x) = G_CUR_YX
        stdscr.move(y, x)
        time.sleep(1)
        timelimit -= 1
    

def decrypt_record_game(stdscr):
    """
        Player gets 5 chances to work out the encryption key.

    """
    global G_CUR_YX
    global DRG_ACT
    DRG_ACT = True
    drgwin = curses.newwin(52, 81)
    draw_box(0, 0, 79, 51, True, BLUE, drgwin)
    drgwin.addstr(0, 25, "[ MANIFEST RECORD DECRYPTION ]", BLUE )
    drgwin.refresh()
    # Use alfanum file to create random key based on difficulty setting
    f = open("./assets/data/alfanum.txt", "r")
    data = f.read()
    f.close()
    ekey = ""
    if DIFFICULTY == "MINOR":
        dud_keys = 60
        for i in range(5):
            ekey += data[random.randint(0, (len(data) - 1))]
    if DIFFICULTY == "MAJOR":
        dud_keys = 60
        for i in range(8):
            ekey += data[random.randint(0, (len(data) - 1))]
    if DIFFICULTY == "CHAOS":
        dud_keys = 60
        for i in range(12):
            ekey += data[random.randint(0, (len(data) - 1))]
    for i in range(35):
        drgwin.move(6 + i, 4)
        for i in range(72):
            drgwin.addstr(str(random.randint(0, 1)), WHITE)
            #drgwin.addch(data[random.randint(0, (len(data) - 1))])
    line_pos = random.randint(6, 40)
    row_pos = random.randint(4, (72 - len(ekey)))
    used_locs = []
    used_locs.append((line_pos, row_pos))
    drgwin.addstr(line_pos, row_pos, ekey, BLUE)
    # insert the invalid keys
    used_keys = []
    for keys in range(dud_keys):
        # Create a temp key the same size as the actual ekey
        # Check if key has already been generated
        duplicate_key = True
        while duplicate_key:
            t_k = ''
            for char in range(len(ekey)):
                t_k += data[random.randint(0, (len(data) - 1))]
            if t_k not in used_keys:
                duplicate_key = False
                used_keys.append(t_k)
        # find somewhere to insert it that doesn't clash
        look_for_loc = True
        while look_for_loc:
            # create a new random location
            line_pos = random.randint(6, 40)
            row_pos = random.randint(4, (72 - len(ekey)))
            # check if line is empty
            line_used = False
            for i in range(len(used_locs)):
                l, r = used_locs[i]
                if line_pos == l:
                    line_used = True
            if line_used is not True:
                drgwin.addstr(line_pos, row_pos, t_k, BLUE)
                used_locs.append((line_pos, row_pos))
                look_for_loc = False
                break
            for i in range(6,40):
                space_free = False
                for x in range(len(used_locs)):
                    l, r = used_locs[x]
                    if line_pos == l:
                        if row_pos <= ((r - len(ekey) - 1)) \
                        or row_pos >= ((r + len(ekey) + 1)):
                            space_free = True
                            continue
                        else:
                            space_free = False
                            break
                if space_free is True:
                    drgwin.addstr(line_pos, row_pos, t_k, BLUE)
                    used_locs.append((line_pos, row_pos))
                    look_for_loc = False
                    break
            break
    # Launch countodown timer in a thread
    threading.Thread(target=countdown,daemon=True, args=(drgwin,)).start()
    # Pause execution to allow countdown thread to start
    time.sleep(0.1)
    correct_key = False
    for i in range(5):
        G_CUR_YX = (46, 21)
        draw_box(44, 4, 34, 4, True, BLUE, drgwin)
        drgwin.addstr(44, 12, "[ KEY VERIFICATION ]", BLUE)
        drgwin.addstr(46, 10, "ENTER KEY: ", BLUE)
        drgwin.refresh()
        key_selection = get_input(BLUE, len(ekey), drgwin)
        if DRG_ACT is False:
            break
        draw_box(42, 35, 37, 8, False, BLUE, drgwin)
        drgwin.addstr(42, 46, "[ RESULT FEED ]", BLUE)
        drgwin.addstr(44 + i, 44, "SEQUENCE " + str(i + 1) + " : ", BLUE)
        for i in range(len(key_selection)):
            if key_selection[i] not in ekey:
                drgwin.addstr(key_selection[i], RED)
            elif key_selection[i] == ekey[i]:
                drgwin.addstr(key_selection[i], GREEN)
            else:
                drgwin.addstr(key_selection[i], YELLOW)
        if key_selection == ekey:
            correct_key = True
            break
    if correct_key:
        draw_box(44, 4, 34, 4, True, GREEN, drgwin)
        drgwin.addstr(44, 12, "[ KEY VERIFICATION ]", GREEN)
        drgwin.addstr(46, 7, "VALID KEY - RECORD RECOVERED", GREEN)
        drgwin.refresh()
    else:
        drgwin.move(0, 0)
        for i in range(52):
            drgwin.move(0 + i, 0)
            for i in range(80):
                drgwin.addstr("X", RED)
        draw_box(44, 4, 34, 4, True, RED, drgwin)
        drgwin.addstr(44, 12, "[ KEY VERIFICATION ]", RED)
        drgwin.addstr(46, 10, "RECORD PERMA LOCKED!", RED)
        drgwin.refresh()
    DRG_ACT = False
    time.sleep(2)
    drgwin.clear()
    del drgwin
    stdscr.touchwin()
    stdscr.refresh()



def main(stdscr):
    """
        Primary startup function.
        Setup curses and color vars
    """
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_WHITE, -1)
    curses.init_pair(2, curses.COLOR_RED, -1)
    curses.init_pair(3, curses.COLOR_GREEN, -1)
    curses.init_pair(4, curses.COLOR_BLUE, -1)
    curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_BLUE)
    curses.init_pair(6, curses.COLOR_WHITE, curses.COLOR_RED)
    curses.init_pair(7, curses.COLOR_YELLOW, -1)
    global WHITE
    WHITE = curses.color_pair(1) | curses.A_BOLD
    global RED
    RED = curses.color_pair(2) | curses.A_BOLD
    global GREEN
    GREEN = curses.color_pair(3) | curses.A_BOLD
    global BLUE
    BLUE = curses.color_pair(4) | curses.A_BOLD
    global W_ON_B
    W_ON_B = curses.color_pair(5) | curses.A_BOLD
    global W_ON_R
    W_ON_R = curses.color_pair(6) | curses.A_BOLD
    global YELLOW
    YELLOW = curses.color_pair(7) | curses.A_BOLD
    # Display main menu
    main_menu(stdscr)
    


def main_menu(stdscr):
    """
        Display logo and main menu
    """
    # Clear screen
    global ANI_DLA
    stdscr.clear()
    stdscr.refresh()
    # read in logo and animate display
    f = open('./assets/gfx/logo.txt')
    data = f.read()
    f.close()
    for i in range(24):
        stdscr.move(32 - i, 7)
        time.sleep(ANI_DLA)
        new_r_count = 0
        start_line = 1
        for ch in data:
            if new_r_count >= (len(data) / 6):
                stdscr.move(((32 - i) + start_line), 7)
                new_r_count = 0
                start_line += 1
            rc = random.randint(1,26 - i)
            if rc == 1:
                stdscr.addstr(ch, RED)
            elif rc == 2:
                stdscr.addstr(ch, GREEN)
            elif rc == 3:
                stdscr.addstr(ch, BLUE)
            else:
                stdscr.addstr(" ", WHITE)
            new_r_count = new_r_count + 1
        stdscr.refresh()
    draw_box(0, 0, 79, 51, False, GREEN, stdscr)
    stdscr.addstr(0, 29, "[ MANIFEST V0.4 ]", GREEN)
    for i in range(9):
        draw_box(24, 19, 38, 2 + (i - 2), True, GREEN, stdscr)
        time.sleep(ANI_DLA)
        stdscr.refresh()
    stdscr.addstr(24, 31, "[ MAIN MENU ]", GREEN)
    stdscr.addstr(26, 33, "N", YELLOW)
    stdscr.addstr("EW GAME", WHITE)
    stdscr.addstr(28, 33, "T", YELLOW)
    stdscr.addstr("UTORIAL", WHITE)
    stdscr.addstr(30, 33, "Q", YELLOW)
    stdscr.addstr("UIT", WHITE)
    stdscr.addstr(42, 16, "TYPE THE FIRST LETTER OF AN OPTION TO SELECT", WHITE)
    stdscr.addstr(51, 26, "[ © WILL GRIFFITHS 2023 ]", GREEN)
    stdscr.refresh()
    gen_data_lists(stdscr)
    # REDuce animation delay time for future rendering
    ANI_DLA = 0.005

    while True:
        key = stdscr.getkey()
        #stdscr.addstr(0, 0, key)
        if key == 'N' or key == 'n':
            game_loop(stdscr)
            break
        elif key == 'Q' or key == 'q':
            exit()

def game_loop(stdscr):
    """
        Handle main game loop
    """
    global P_APPR_ACT
    global SO_WELC
    global SO_SCAN_REQ
    global P_SCAN_RESP

    for i in range(38):
        draw_box(9, 1 + i, 1 + i, 1 + i, False, RED, stdscr)
        draw_box(46 - i, 1 + i, 1 + i, 1 + i, False, GREEN, stdscr)
        time.sleep(ANI_DLA)
        stdscr.refresh()
    for i in range(38):
        draw_box(46 - i, 1 + i, 1 + i, 1 + i, False, GREEN, stdscr)
        draw_box(9, 1 + i, 1 + i, 1 + i, False, RED, stdscr)
        time.sleep(ANI_DLA)
        stdscr.refresh()
    for i in range(38):
        draw_box(9, 38 - i, 1 + i, 1 + i, True, GREEN, stdscr)
        draw_box(9, 77 - i, 1 + i, 1 + i, True, GREEN, stdscr)
        time.sleep(ANI_DLA)
        stdscr.refresh()


    stdscr.addstr(2, 3, "PASSENGER - ", GREEN)
    stdscr.addstr(P_APPR_ACT[random.randint(0, len(P_APPR_ACT) - 1)], WHITE)
    stdscr.refresh()
    time.sleep(2)
    stdscr.addstr(4, 56, " - SEC.OFFICER (YOU)", GREEN)
    temp_resp = SO_WELC[random.randint(0, len(SO_WELC) - 1)]
    stdscr.addstr(4, 56 - len(temp_resp), temp_resp, WHITE)
    stdscr.refresh()
    time.sleep(2)
    stdscr.addstr(5, 56, " - SEC.OFFICER (YOU)", GREEN)
    temp_resp = SO_SCAN_REQ[random.randint(0, len(SO_SCAN_REQ) - 1)]
    stdscr.addstr(5, 56 - len(temp_resp), temp_resp, WHITE)
    stdscr.refresh()
    time.sleep(2)
    stdscr.addstr(7, 3, "PASSENGER - ", GREEN)
    stdscr.addstr(P_SCAN_RESP[random.randint(0, len(P_SCAN_RESP) - 1)], WHITE)
    stdscr.refresh()
    time.sleep(1)
    stdscr.addstr(9, 3, "[ CONNECTING TO IMPLANT. ]", YELLOW)
    stdscr.refresh()
    time.sleep(1)
    stdscr.addstr(9, 3, "[ SUBDERMAL IMPLANT DATA ]", GREEN)
    stdscr.refresh()
    time.sleep(.5)
    stdscr.addstr(11, 4, "[ VOYAGE DATA ]", GREEN)
    stdscr.addstr(13, 4, "TICKET TOKEN: ", GREEN)
    stdscr.addstr("FH7FGH5", WHITE)
    stdscr.addstr(14, 4, "CABIN ID: ", GREEN)
    stdscr.addstr("FH7FGH5", WHITE)
    stdscr.addstr(15, 4, "CABIN CLASS: ", GREEN)
    stdscr.addstr("LUXURY", WHITE)
    stdscr.refresh()
    time.sleep(.5)
    stdscr.addstr(17, 4, "[ PERSONAL DATA ]", GREEN)
    stdscr.refresh()
    time.sleep(.5)
    stdscr.addstr(19, 4, "NAME: ", GREEN)
    stdscr.addstr(MALE_NAMES[random.randint(0, len(MALE_NAMES))], WHITE)
    stdscr.addstr(20, 4, "AGE: ", GREEN)
    stdscr.addstr("48", WHITE)
    stdscr.addstr(21, 4, "SEX: ", GREEN)
    stdscr.addstr("MALE", WHITE)
    stdscr.addstr(22, 4, "COUNTRY: ", GREEN)
    stdscr.addstr(COUNTRY_NAMES[random.randint(0, len(COUNTRY_NAMES))], WHITE)
    stdscr.addstr(23, 4, "HEIGHT: ", GREEN)
    stdscr.addstr("162 CM", WHITE)
    stdscr.addstr(24, 4, "HAIR COLOR: ", GREEN)
    stdscr.addstr("LIPSTICK PINK", WHITE)
    stdscr.addstr(25, 4, "PROFESSION: ", GREEN)
    stdscr.addstr("NUTRIBIOLOGIST", WHITE)
    stdscr.addstr(26, 4, "MARITAL STATUS: ", GREEN)
    stdscr.addstr("MARRIED", WHITE)
    stdscr.addstr(27, 4, "CRIMINAL STATUS: ", GREEN)
    stdscr.addstr("CLEAN RECORD", WHITE)
    stdscr.addstr(28, 4, "ALERGIES: ", GREEN)
    stdscr.addstr("NONE", WHITE)
    stdscr.addstr(29, 4, "VOICE COM ID: ", GREEN)
    stdscr.addstr("827364827634", WHITE)
    stdscr.addstr(30, 4, "CREDIT RATING: ", GREEN)
    stdscr.addstr("A++", WHITE)
    stdscr.addstr(31, 4, "EDUCATION LEVEL: ", GREEN)
    stdscr.addstr("PHD", WHITE)
    stdscr.addstr(32, 4, "UERI: ", GREEN)
    stdscr.addstr("FTHG 56GH FGH6 FGHS", WHITE)
    stdscr.addstr(33, 4, "MENTAK ALIGNMENT: ", GREEN)
    stdscr.addstr("LISTRO", WHITE)
    stdscr.refresh()

    stdscr.addstr(9, 42, "[ WARNING !!!!!!!!!! ]", RED)
    stdscr.refresh()
    time.sleep(1)
    stdscr.addstr(9, 42, "[ RECORD ENCRYPTED ! ]", YELLOW)
    stdscr.refresh()
    time.sleep(1)
    stdscr.addstr(9, 42, "[ SHIP MANIFEST DATA ]", GREEN)
    stdscr.refresh()
    time.sleep(.5)
    stdscr.addstr(11, 43, "[ VOYAGE DATA ]", GREEN)
    stdscr.addstr(13, 43, "TICKET TOKEN: ", GREEN)
    stdscr.addstr("FH7FGH5", WHITE)
    stdscr.addstr(14, 43, "CABIN ID: ", GREEN)
    stdscr.addstr("FH7####", RED)
    stdscr.addstr(15, 43, "CABIN CLASS: ", GREEN)
    stdscr.addstr("LUXURY", WHITE)
    stdscr.refresh()
    time.sleep(.5)
    stdscr.addstr(17, 43, "[ PERSONAL DATA ]", GREEN)
    stdscr.refresh()
    time.sleep(.5)
    stdscr.addstr(19, 43, "NAME: ", GREEN)
    stdscr.addstr(MALE_NAMES[random.randint(0, len(MALE_NAMES))], WHITE)
    stdscr.addstr(20, 43, "AGE: ", GREEN)
    stdscr.addstr("48", WHITE)
    stdscr.addstr(21, 43, "SEX: ", GREEN)
    stdscr.addstr("MALE", WHITE)
    stdscr.addstr(22, 43, "COUNTRY: ", GREEN)
    stdscr.addstr(COUNTRY_NAMES[random.randint(0, len(COUNTRY_NAMES))], WHITE)
    stdscr.addstr(23, 43, "HEIGHT: ", GREEN)
    stdscr.addstr("162 CM", WHITE)
    stdscr.addstr(24, 43, "HAIR COLOR: ", GREEN)
    stdscr.addstr("LIPSTICK PINK", WHITE)
    stdscr.addstr(25, 43, "PROFESSION: ", GREEN)
    stdscr.addstr("NUTRIBIOLOGIST", WHITE)
    stdscr.addstr(26, 43, "MARITAL STATUS: ", GREEN)
    stdscr.addstr("MARRIED", WHITE)
    stdscr.addstr(27, 43, "CRIMINAL STATUS: ", GREEN)
    stdscr.addstr("CLEAN RECORD", WHITE)
    stdscr.addstr(28, 43, "ALERGIES: ", GREEN)
    stdscr.addstr("NONE", WHITE)
    stdscr.addstr(29, 43, "VOICE COM ID: ", GREEN)
    stdscr.addstr("#####4827634", RED)
    stdscr.addstr(30, 43, "CREDIT RATING: ", GREEN)
    stdscr.addstr("###", RED)
    stdscr.addstr(31, 43, "EDUCATION LEVEL: ", GREEN)
    stdscr.addstr("PHD", WHITE)
    stdscr.addstr(32, 43, "UERI: ", GREEN)
    stdscr.addstr("FTHG #### FGH6 FGHS", RED)
    stdscr.addstr(33, 43, "MENTAK ALIGNMENT: ", GREEN)
    stdscr.addstr("LISTRO", WHITE)
    stdscr.refresh()

    draw_action_buttons(stdscr)
    while True:
        key = stdscr.getkey()
        if key == 'd' or key == 'D':
            decrypt_record_game(stdscr)
        elif key == 'm' or key == 'M':
            main_menu(stdscr)

wrapper(main)
