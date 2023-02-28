import config as c
import curses
from curses import wrapper
import time
import random
import threading
import data_loader as dl
import passenger_creator as pc


WHITE = ""
RED = ""
GREEN = ""
BLUE = ""
W_ON_B = ""
W_ON_R = ""
YELLOW = ""


def set_game(scr):
    # pick diff
    # give name
    pass


def confirm_action(msg, style, scr):
    """
        Get player to confirm the action / key
    """
    conf_win = curses.newpad(6, 30)
    draw_box(0, 0, 28, 4, True, style, conf_win)
    conf_win.addstr(2, 10, "Y", WHITE)
    conf_win.addstr("ES OR", style)
    conf_win.addstr(2, 17, "N", WHITE)
    conf_win.addstr("O", style)
    conf_win.addstr(0, 8, "[ " + str(msg) + " ]", style)
    scr.refresh()
    conf_win.refresh(0, 0, 25, 25, 29, 53)
    while True:
        key = scr.getkey()
        if key in ('Y', 'y'):
            confirm = True
            break
        elif key in ('N', 'n'):
            confirm = False
            break
    curses.flushinp()
    conf_win.erase()
    del conf_win
    scr.touchwin()
    scr.refresh()
    return confirm


def rand(start, stop):
    """
        Simple function to return random int
        Basic alias to shorten lines
    """
    return random.randint(start, stop)

def draw_action_buttons(scr):
    """
        Draw 'buttons' with actions the player can take
        Draw with only 3 if decrpyt that been used
    """
    draw_box(48, 7, 14, 2, True, GREEN, scr)
    scr.addstr(49, 12, "B", GREEN)
    scr.addstr("OARD", WHITE)
    scr.refresh()
    time.sleep(.25)
    draw_box(48, 23, 14, 2, True, YELLOW, scr)
    scr.addstr(49, 28, "R", YELLOW)
    scr.addstr("EJECT", WHITE)
    scr.refresh()
    time.sleep(.25)
    draw_box(48, 39, 14, 2, True, RED, scr)
    scr.addstr(49, 43, "A", RED)
    scr.addstr("RREST", WHITE)
    scr.refresh()
    time.sleep(.25)
    draw_box(48, 55, 14, 2, True, BLUE, scr)
    scr.addstr(49, 59, "D", BLUE)
    scr.addstr("ECRYPT", WHITE)

def draw_box(line, col, width, height, fill, style, scr):
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
    scr.addstr(l, c, "╔", s)
    for i in range(w - 1):
        scr.addstr(l, c  + 1 + i, "═", s)
    scr.addstr(l, c + w , "╗", s)
    for i in range(h - 1):
        scr.addstr(l + 1 + i, c, "║", s)
        if (f):
            for x in range(w - 1):
                scr.addstr(l + 1 + i, c + 1 + x, " ", s)
        scr.addstr(l + 1 + i, c + w, "║", s)
    scr.addstr(l + h, c, "╚", s)
    for i in range(w - 1):
        scr.addstr(l + h, c + 1 + i, "═", s)
    scr.addstr(l + h , c + w , "╝", s)


def get_input(echo_style, max_size, scr):
    """
        Gather input from the user and echo in selected style
        Escape is 27
        Backspace is 127
        Space is 32
    """
    s = echo_style
    ms = max_size
    user_input = ""
    while c.DRG_ACT:
        try:
            key = scr.getch()
            #key_as_char = str(chr(key))
            #scr.addstr(0,0, str(key), RED)
            if c.DRG_ACT is False:
                break
            if key == ord('\n') or key == ord('\r'):
                user_input = user_input.upper()
                return user_input
            if key == 127 or key == ord('\b'):
                if len(user_input) >= 1:
                    if c.DRG_ACT:
                        (y, x) = c.G_CUR_YX
                        c.G_CUR_YX = (y, x - 1)
                    else:
                        (y, x) = curses.getsyx()
                    scr.move(y, x - 1)
                    scr.addstr(" ", s)
                    scr.move(y, x - 1)
                    user_input = user_input[:-1]
            elif len(user_input) == max_size:
                warn_msg("INPUT LIMIT REACHED", W_ON_R , scr)
            elif chr(key).upper() in c.VALID_KEYS:
                if c.DRG_ACT:
                    (y, x) = c.G_CUR_YX
                    c.G_CUR_YX = (y, x + 1)
                user_input += chr(key)
                screen_key = chr(key)
                screen_key = screen_key.upper()
                scr.addstr(screen_key, s)
            else:
                warn_msg("    INVALID KEY", W_ON_R , scr)
        except:
            pass
def warn_msg(msg, style, scr):
    """
        Display warning to user
    """
    box = curses.newpad(6,30)
    draw_box(0, 0, 28, 4, True, style, box)
    box.addstr(2, 5, msg, style)
    box.addstr(0, 9, "[ WARNING ]", style)
    scr.refresh()
    box.refresh(0, 0, 25, 25, 29, 53)
    time.sleep(1.5)
    curses.flushinp()
    box.erase()
    del box
    scr.touchwin()
    scr.refresh()


def countdown(scr):
    """
        Countdown timer
    """
    timelimit = 60
    blank_line = ""
    indent = 0
    for i in range(timelimit):
        blank_line += " "
    while c.DRG_ACT:
        bar_line = ""
        for i in range(timelimit):
            bar_line += "█"
        if timelimit == 0:
            # ran out of time!!
            blank_line = ""
            for i in range(70):
                blank_line += " "
            scr.addstr(3, 4, blank_line, GREEN )
            scr.addstr(4, 4, blank_line, GREEN )
            scr.addstr(3, 30, "RECORD PERMA LOCKED!", RED )
            scr.addstr(4, 29, "HIT ANY KEY TO RETURN", RED )
            scr.refresh()
            c.DRG_ACT = False
            break
        scr.addstr(2, 4, "MEMORY ANALISED. INPUT CORRECT KEY TO UNLOCK", BLUE )
        scr.addstr(4, 10, blank_line, GREEN )
        if timelimit > 40:
            scr.addstr(4, 10 + ( 60 - timelimit) - indent, bar_line, GREEN )
            scr.addstr(4, 37, "[ " + str(timelimit) + " ]", GREEN )
        elif timelimit > 19 and timelimit <= 40:
            scr.addstr(4, 10 + ( 60 - timelimit) - indent, bar_line, YELLOW )
            scr.addstr(4, 37, "[ " + str(timelimit) + " ]", YELLOW )
        else:
            scr.addstr(4, 10 + ( 60 - timelimit) - indent, bar_line, RED)
            scr.addstr(4, 37, "[ " + str(timelimit) + " ]", RED )
        scr.refresh()
        if timelimit % 2 == 0:
            indent += 1
        # Put the cursor back to where it was for input
        (y, x) = c.G_CUR_YX
        scr.move(y, x)
        time.sleep(1)
        timelimit -= 1
    

def decrypt_record_game(scr):
    """
        Player gets 5 chances to work out the encryption key.

    """
    c.DRG_ACT = True
    drgwin = curses.newwin(52, 81)
    for i in range(51):
        draw_box(51 - i , 0, 79, i, True, BLUE, drgwin)
        drgwin.addstr(51 - i, 25, "[ MANIFEST RECORD DECRYPTION ]", BLUE )
        drgwin.refresh()
        time.sleep(.005)
        #draw_box(line, col, width, height, fill, style, scr)
    draw_box(0, 0, 79, 51, True, BLUE, drgwin)
    drgwin.addstr(0, 25, "[ MANIFEST RECORD DECRYPTION ]", BLUE )
    drgwin.refresh()
    ekey = ""
    if c.DIFFICULTY == "MINOR":
        dud_keys = 60
        for i in range(12):
            ekey += c.VALID_KEYS[rand(0, (len(c.VALID_KEYS) - 1))]
    if c.DIFFICULTY == "MAJOR":
        dud_keys = 100
        for i in range(8):
            ekey += c.VALID_KEYS[rand(0, (len(c.VALID_KEYS) - 1))]
    if c.DIFFICULTY == "CHAOS":
        dud_keys = 120
        for i in range(5):
            ekey += c.VALID_KEYS[rand(0, (len(c.VALID_KEYS) - 1))]
    for i in range(35):
        drgwin.move(6 + i, 4)
        for i in range(72):
            tk = c.VALID_KEYS[rand(0, (len(c.VALID_KEYS) - 1))]
            drgwin.addstr(tk, WHITE)
            #drgwin.addch(data[rand(0, (len(data) - 1))])
    line_pos = rand(6, 40)
    row_pos = rand(4, (72 - len(ekey)))
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
                t_k += c.VALID_KEYS[rand(0, (len(c.VALID_KEYS) - 1))]
            if t_k not in used_keys:
                duplicate_key = False
                used_keys.append(t_k)
        # find somewhere to insert it that doesn't clash
        look_for_loc = True
        while look_for_loc:
            # create a new random location
            line_pos = rand(6, 40)
            row_pos = rand(4, (72 - len(ekey)))
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
        c.G_CUR_YX = (46, 21)
        draw_box(44, 4, 34, 4, True, BLUE, drgwin)
        drgwin.addstr(44, 12, "[ KEY VERIFICATION ]", BLUE)
        drgwin.addstr(46, 10, "ENTER KEY: ", BLUE)
        drgwin.refresh()
        key_selection = get_input(BLUE, len(ekey), drgwin)
        if c.DRG_ACT is False:
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
    c.DRG_ACT = False
    time.sleep(2)
    curses.flushinp()
    drgwin.clear()
    del drgwin
    scr.touchwin()
    scr.refresh()


def main(scr):
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
    dl.gen_data_lists()
    # Display main menu
    main_menu(scr)


def main_menu(scr):
    """
        Display logo and main menu options
    """
    scr.clear()
    scr.refresh()
    # read in logo and animate display
    f = open('./assets/gfx/logo.txt')
    data = f.read()
    f.close()
    for i in range(24):
        scr.move(32 - i, 7)
        time.sleep(c.ANI_DLA)
        new_r_count = 0
        start_line = 1
        for ch in data:
            if new_r_count >= (len(data) / 6):
                scr.move(((32 - i) + start_line), 7)
                new_r_count = 0
                start_line += 1
            rc = rand(1,26 - i)
            if rc == 1:
                scr.addstr(ch, RED)
            elif rc == 2:
                scr.addstr(ch, GREEN)
            elif rc == 3:
                scr.addstr(ch, BLUE)
            else:
                scr.addstr(" ", WHITE)
            new_r_count = new_r_count + 1
        scr.refresh()
    draw_box(0, 0, 79, 51, False, GREEN, scr)
    scr.addstr(0, 30, "[ MANIFEST V0.4 ]", GREEN)
    for i in range(9):
        draw_box(24, 19, 38, 2 + (i - 2), True, GREEN, scr)
        time.sleep(c.ANI_DLA)
        scr.refresh()
    scr.addstr(24, 31, "[ MAIN MENU ]", GREEN)
    scr.addstr(26, 33, "N", YELLOW)
    scr.addstr("EW GAME", WHITE)
    scr.addstr(28, 33, "T", YELLOW)
    scr.addstr("UTORIAL", WHITE)
    scr.addstr(30, 33, "Q", YELLOW)
    scr.addstr("UIT", WHITE)
    scr.addstr(42, 16, "TYPE THE FIRST LETTER OF AN OPTION TO SELECT", WHITE)
    scr.addstr(51, 26, "[ © WILL GRIFFITHS 2023 ]", GREEN)
    scr.refresh()

    # Reduce animation delay time for future rendering
    c.ANI_DLA = 0.005

    #curses.flushinp()
    while True:
        key = scr.getkey()
        #scr.addstr(0, 0, key)
        if key == 'N' or key == 'n':
            game_loop(scr)
            break
        elif key == 'Q' or key == 'q':
            exit()


def encrypt(field):
    """
        Takes a record and randomly hides it based on difficulty.
        Only emulating the field as being encrypted for gameplay
        Might skip encryption altogether 
    """

    if c.DIFFICULTY == "CHAOS":
        diff_modifier = 0.90
        skip_chance = 4
    if c.DIFFICULTY == "MAJOR":
        diff_modifier = 0.7
        skip_chance = 3
    if c.DIFFICULTY == "MINOR":
        diff_modifier = 0.5
        skip_chance = 2

    if rand(1, skip_chance) == 1:
        return field

    size = len(field)
    temp_list = []
    injecting = True
    injectlimit = round(size * diff_modifier)
    total_injects = 0

    for count, value in enumerate(field):
        temp_list.append(value)

    while injecting:
        temp_loc = rand(0, size - 1)
        if temp_list[temp_loc] != "#":
            temp_list[temp_loc] = "#"
            total_injects += 1
        if total_injects >= injectlimit:
            injecting = False
    
    field = ""
    for count, value in enumerate(temp_list):
        field += value

    return field


    # inject random hashes
    # stop once threshold reached


def game_loop(scr):
    """
        Handle main game loop
        Interact with passenger
        display data
        take action
    """
    # clear out the passenger list
    c.PSNGR_LIST = []

    # Generate a new passenger
    c.PSNGR_LIST.append(pc.Passenger())


    scr.clear()
    draw_box(0, 0, 79, 51, False, GREEN, scr)
    scr.addstr(0, 3, "[ INFINITUM SECURITY TERMINAL ]", GREEN)
    for i in range(38):
        draw_box(9, 1, 38, 1 + i, True, GREEN, scr)
        draw_box(9, 40, 38, 1 + i, True, GREEN, scr)
        time.sleep(c.ANI_DLA)
        scr.refresh()
    loop = 7
    h_loop = 5
    for i in range(8):
        for i in range(8):
            scr.move(1 + i, 1)
            for i in range(78):
                scr.addstr(" " , GREEN)
        scr.refresh()
        for i in range(loop):
            scr.move(1 + i, 1)
            for i in range(78):
                scr.addstr("░" , GREEN)
        if h_loop > 0:
            scr.addstr(h_loop, 20, "*SECURITY HATCH SHUTTERING RAISES*")
        if h_loop < 2:
            scr.addstr(5, 19, "*PASSENGER APPROACH SIGN ILUMINATES*", YELLOW)
        scr.refresh()
        #time.sleep(.75)
        loop -= 1
        h_loop -= 1

    scr.addstr(5, 19, "                                      ")
    scr.refresh()
    scr.addstr(2, 3, "PASSENGER - ", GREEN)
    scr.addstr(c.P_APPR_ACT[rand(0, len(c.P_APPR_ACT) - 1)], WHITE)
    scr.refresh()
    #time.sleep(2)
    scr.addstr(4, 56, " - SEC.OFFICER (YOU)", GREEN)
    temp_resp = c.SO_WELC[rand(0, len(c.SO_WELC) - 1)]
    scr.addstr(4, 56 - len(temp_resp), temp_resp, WHITE)
    scr.refresh()
    #time.sleep(2)
    scr.addstr(5, 56, " - SEC.OFFICER (YOU)", GREEN)
    temp_resp = c.SO_SCAN_REQ[rand(0, len(c.SO_SCAN_REQ) - 1)]
    scr.addstr(5, 56 - len(temp_resp), temp_resp, WHITE)
    scr.refresh()
    #time.sleep(2)
    scr.addstr(7, 3, "PASSENGER - ", GREEN)
    scr.addstr(c.P_SCAN_RESP[rand(0, len(c.P_SCAN_RESP) - 1)], WHITE)
    scr.refresh()
    #time.sleep(1)
    scr.addstr(9, 3, "[ CONNECTING TO IMPLANT  ]", YELLOW)
    scr.refresh()
    #time.sleep(1)
    scr.addstr(9, 3, "[ READING IMPLANT DATA.. ]", WHITE)
    scr.refresh()
    #time.sleep(.5)
    scr.addstr(11, 4, "[ VOYAGE DATA ]", GREEN)
    scr.addstr(13, 4, "TICKET TOKEN: ", GREEN)
    scr.addstr(c.PSNGR_LIST[c.CUR_PSNGR_NO].i_ticket_token, WHITE)
    scr.addstr(14, 4, "CABIN ID: ", GREEN)
    scr.addstr(c.PSNGR_LIST[c.CUR_PSNGR_NO].i_cabin_id, WHITE)
    scr.addstr(15, 4, "CABIN CLASS: ", GREEN)
    scr.addstr(c.PSNGR_LIST[c.CUR_PSNGR_NO].i_cabin_class, WHITE)
    scr.refresh()
    #time.sleep(.5)
    scr.addstr(17, 4, "[ PERSONAL DATA ]", GREEN)
    scr.refresh()
    #time.sleep(.5)
    scr.addstr(19, 4, "NAME: ", GREEN)
    scr.addstr(c.PSNGR_LIST[c.CUR_PSNGR_NO].i_name, WHITE)
    scr.addstr(20, 4, "AGE: ", GREEN)
    scr.addstr(str(c.PSNGR_LIST[c.CUR_PSNGR_NO].m_age), WHITE)
    scr.addstr(21, 4, "SEX: ", GREEN)
    scr.addstr(c.PSNGR_LIST[c.CUR_PSNGR_NO].i_sex, WHITE)
    scr.addstr(22, 4, "CITIZENSHIP: ", GREEN)
    scr.addstr(c.PSNGR_LIST[c.CUR_PSNGR_NO].i_citizenship, WHITE)
    scr.addstr(23, 4, "HEIGHT: ", GREEN)
    scr.addstr(str(c.PSNGR_LIST[c.CUR_PSNGR_NO].i_height) + " CM", WHITE)
    scr.addstr(24, 4, "HAIR COLOR: ", GREEN)
    scr.addstr(c.PSNGR_LIST[c.CUR_PSNGR_NO].i_hair_color, WHITE)
    scr.addstr(25, 4, "PROFESSION: ", GREEN)
    scr.addstr(c.PSNGR_LIST[c.CUR_PSNGR_NO].i_profession, WHITE)
    scr.addstr(26, 4, "MARITAL STATUS: ", GREEN)
    scr.addstr(c.PSNGR_LIST[c.CUR_PSNGR_NO].i_marital_stat, WHITE)
    scr.addstr(27, 4, "BLOOD TYPE: ", GREEN)
    scr.addstr(c.PSNGR_LIST[c.CUR_PSNGR_NO].i_blood_type, WHITE)
    scr.addstr(28, 4, "ALLERGIES: ", GREEN)
    scr.addstr(c.PSNGR_LIST[c.CUR_PSNGR_NO].i_allergies, WHITE)
    scr.addstr(29, 4, "VOICE COM ID: ", GREEN)
    scr.addstr(str(c.PSNGR_LIST[c.CUR_PSNGR_NO].i_voice_com_id), WHITE)
    scr.addstr(30, 4, "CREDIT RATING: ", GREEN)
    scr.addstr(c.PSNGR_LIST[c.CUR_PSNGR_NO].i_credit_rating, WHITE)
    scr.addstr(31, 4, "EDUCATION LEVEL: ", GREEN)
    scr.addstr(c.PSNGR_LIST[c.CUR_PSNGR_NO].i_edu_lv, WHITE)
    scr.addstr(32, 4, "UERI: ", GREEN)
    scr.addstr(c.PSNGR_LIST[c.CUR_PSNGR_NO].i_ueri, WHITE)
    scr.addstr(33, 4, "MENTAK ALIGNMENT: ", GREEN)
    scr.addstr(c.PSNGR_LIST[c.CUR_PSNGR_NO].i_mentak_alignment, WHITE)
    scr.addstr(34, 4, "DIGITAL DNA FINGERPRINT: ", GREEN)
    scr.move(36, 8)
    dna_loc = 0
    dna_data = c.PSNGR_LIST[c.CUR_PSNGR_NO].i_dna_fingerprint
    for i in range(10):
        scr.move(36 + i, 8)
        for i in range(20):
            scr.addstr(dna_data[dna_loc], WHITE)
            dna_loc += 1
    scr.addstr(9, 3, "[ PASSENGER IMPLANT DATA ]", GREEN)
    scr.refresh()

    # Dsiplay manifest data record

    scr.addstr(9, 42, "[ TICKET TOKEN MATCH ]", WHITE)
    scr.refresh()
    #time.sleep(1)
    scr.addstr(9, 42, "[ WARNING !!!!!!!!!! ]", RED)
    scr.refresh()
    #time.sleep(1)
    scr.addstr(9, 42, "[ PARTIAL RECORD...  ]", YELLOW)
    scr.refresh()
    #time.sleep(1)
    scr.addstr(9, 42, "[ SHIP MANIFEST DATA ]", GREEN)
    scr.refresh()
    #time.sleep(.5)
    scr.addstr(11, 43, "[ VOYAGE DATA ]", GREEN)
    scr.addstr(13, 43, "TICKET TOKEN: ", GREEN)
    scr.addstr(c.PSNGR_LIST[c.CUR_PSNGR_NO].m_ticket_token, WHITE)

    scr.addstr(14, 43, "CABIN ID: ", GREEN)
    if c.ENCRYPT_ON:
        cabin_id = encrypt(c.PSNGR_LIST[c.CUR_PSNGR_NO].m_cabin_id)
    else:
        cabin_id = c.PSNGR_LIST[c.CUR_PSNGR_NO].m_cabin_id
    display_color = WHITE
    if "#" in str(cabin_id):
        display_color = RED
    scr.addstr(cabin_id, display_color)

    scr.addstr(15, 43, "CABIN CLASS: ", GREEN)
    if c.ENCRYPT_ON:
        cabin_class = encrypt(c.PSNGR_LIST[c.CUR_PSNGR_NO].m_cabin_class)
    else:
        cabin_class = c.PSNGR_LIST[c.CUR_PSNGR_NO].m_cabin_class
    display_color = WHITE
    if "#" in str(cabin_class):
        display_color = RED
    scr.addstr(cabin_class, WHITE)
    scr.refresh()
    #time.sleep(.5)

    scr.addstr(17, 43, "[ PERSONAL DATA ]", GREEN)
    scr.refresh()
    #time.sleep(.5)

    scr.addstr(19, 43, "NAME: ", GREEN)
    if c.ENCRYPT_ON:
        name = encrypt(c.PSNGR_LIST[c.CUR_PSNGR_NO].m_name)
    else:
        name = c.PSNGR_LIST[c.CUR_PSNGR_NO].m_name
    display_color = WHITE
    if "#" in str(name):
        display_color = RED
    scr.addstr(name, display_color)

    scr.addstr(20, 43, "AGE: ", GREEN)
    if c.ENCRYPT_ON:
        age = encrypt(str(c.PSNGR_LIST[c.CUR_PSNGR_NO].m_age))
    else:
        age = str(c.PSNGR_LIST[c.CUR_PSNGR_NO].m_age)
    display_color = WHITE
    if "#" in str(age):
        display_color = RED
    scr.addstr(age, display_color)

    scr.addstr(21, 43, "SEX: ", GREEN)
    if c.ENCRYPT_ON:
        sex = encrypt(c.PSNGR_LIST[c.CUR_PSNGR_NO].m_sex)
    else:
        sex = c.PSNGR_LIST[c.CUR_PSNGR_NO].m_sex
    display_color = WHITE
    if "#" in str(sex):
        display_color = RED
    scr.addstr(sex, display_color)

    scr.addstr(22, 43, "CITIZENSHIP: ", GREEN)
    if c.ENCRYPT_ON:
        citizen = encrypt(c.PSNGR_LIST[c.CUR_PSNGR_NO].m_citizenship)
    else:
        citizen = c.PSNGR_LIST[c.CUR_PSNGR_NO].m_citizenship
    display_color = WHITE
    if "#" in str(citizen):
        display_color = RED
    scr.addstr(citizen, display_color)

    scr.addstr(23, 43, "HEIGHT: ", GREEN)
    if c.ENCRYPT_ON:
        height = encrypt(str(c.PSNGR_LIST[c.CUR_PSNGR_NO].m_height))
    else:
        height = str(c.PSNGR_LIST[c.CUR_PSNGR_NO].m_height)
    display_color = WHITE
    if "#" in str(height):
        display_color = RED
    scr.addstr(height + " CM", display_color)

    scr.addstr(24, 43, "HAIR COLOR: ", GREEN)
    if c.ENCRYPT_ON:
        hair = encrypt(c.PSNGR_LIST[c.CUR_PSNGR_NO].m_hair_color)
    else:
        hair = c.PSNGR_LIST[c.CUR_PSNGR_NO].m_hair_color
    display_color = WHITE
    if "#" in str(hair):
        display_color = RED
    scr.addstr(hair, display_color)

    scr.addstr(25, 43, "PROFESSION: ", GREEN)
    if c.ENCRYPT_ON:
        prof = encrypt(c.PSNGR_LIST[c.CUR_PSNGR_NO].m_profession)
    else:
        prof = c.PSNGR_LIST[c.CUR_PSNGR_NO].m_profession
    display_color = WHITE
    if "#" in str(prof):
        display_color = RED
    scr.addstr(prof, display_color)

    scr.addstr(26, 43, "MARITAL STATUS: ", GREEN)
    if c.ENCRYPT_ON:
        mari = encrypt(c.PSNGR_LIST[c.CUR_PSNGR_NO].m_marital_stat)
    else:
        mari = c.PSNGR_LIST[c.CUR_PSNGR_NO].m_marital_stat
    display_color = WHITE
    if "#" in str(mari):
        display_color = RED
    scr.addstr(mari, display_color)

    scr.addstr(27, 43, "BLOOD TYPE: ", GREEN)
    if c.ENCRYPT_ON:
        blood = encrypt(c.PSNGR_LIST[c.CUR_PSNGR_NO].m_blood_type)
    else:
        blood = c.PSNGR_LIST[c.CUR_PSNGR_NO].m_blood_type
    display_color = WHITE
    if "#" in str(blood):
        display_color = RED
    scr.addstr(blood, display_color)

    scr.addstr(28, 43, "ALLERGIES: ", GREEN)
    if c.ENCRYPT_ON:
        allergies = encrypt(c.PSNGR_LIST[c.CUR_PSNGR_NO].m_allergies)
    else:
        allergies = c.PSNGR_LIST[c.CUR_PSNGR_NO].m_allergies
    display_color = WHITE
    if "#" in str(allergies):
        display_color = RED
    scr.addstr(allergies, display_color)

    scr.addstr(29, 43, "VOICE COM ID: ", GREEN)
    if c.ENCRYPT_ON:
        com = encrypt(str(c.PSNGR_LIST[c.CUR_PSNGR_NO].m_voice_com_id))
    else:
        com = str(c.PSNGR_LIST[c.CUR_PSNGR_NO].m_voice_com_id)
    display_color = WHITE
    if "#" in str(com):
        display_color = RED
    scr.addstr(com, display_color)

    scr.addstr(30, 43, "CREDIT RATING: ", GREEN)
    if c.ENCRYPT_ON:
        cred = encrypt(c.PSNGR_LIST[c.CUR_PSNGR_NO].m_credit_rating)
    else:
        cred = c.PSNGR_LIST[c.CUR_PSNGR_NO].m_credit_rating
    display_color = WHITE
    if "#" in str(cred):
        display_color = RED
    scr.addstr(cred, display_color)

    scr.addstr(31, 43, "EDUCATION LEVEL: ", GREEN)
    if c.ENCRYPT_ON:
        edu = encrypt(c.PSNGR_LIST[c.CUR_PSNGR_NO].m_edu_lv)
    else:
        edu = c.PSNGR_LIST[c.CUR_PSNGR_NO].m_edu_lv
    display_color = WHITE
    if "#" in str(edu):
        display_color = RED
    scr.addstr(edu, display_color)

    scr.addstr(32, 43, "UERI: ", GREEN)
    if c.ENCRYPT_ON:
        ueri = encrypt(c.PSNGR_LIST[c.CUR_PSNGR_NO].m_ueri)
    else:
        ueri = c.PSNGR_LIST[c.CUR_PSNGR_NO].m_ueri
    display_color = WHITE
    if "#" in str(ueri):
        display_color = RED
    scr.addstr(ueri, display_color)

    scr.addstr(33, 43, "MENTAK ALIGNMENT: ", GREEN)
    if c.ENCRYPT_ON:
        mentak = encrypt(c.PSNGR_LIST[c.CUR_PSNGR_NO].m_mentak_alignment)
    else:
        mentak = c.PSNGR_LIST[c.CUR_PSNGR_NO].m_mentak_alignment
    display_color = WHITE
    if "#" in str(mentak):
        display_color = RED
    scr.addstr(mentak, display_color)

    scr.addstr(34, 43, "DIGITAL DNA FINGERPRINT: ", GREEN)
    if c.ENCRYPT_ON:
        dna = encrypt(c.PSNGR_LIST[c.CUR_PSNGR_NO].m_dna_fingerprint)
    else:
        dna = c.PSNGR_LIST[c.CUR_PSNGR_NO].m_dna_fingerprint
    display_color = WHITE
    if "#" in str(dna):
        display_color = RED
    scr.move(36, 48)
    dna_loc = 0
    dna_data = dna
    for i in range(10):
        scr.move(36 + i, 48)
        for i in range(20):
            scr.addstr(dna_data[dna_loc], display_color)
            dna_loc += 1
    scr.refresh()

    draw_action_buttons(scr)
    # Display Quit option
    scr.addstr(0, 70, "[ ", GREEN)
    scr.addstr("Q", WHITE)
    scr.addstr("UIT ]", GREEN)
    curses.flushinp()
    while True:
        key = scr.getkey()
        if key == 'd' or key == 'D':
            decrypt_record_game(scr)
        elif key == 'q' or key == 'Q':
            end_game = confirm_action("END GAME", GREEN, scr)
            if end_game == True:
                main_menu(scr)

# Handle curses intialisation of main function
wrapper(main)
