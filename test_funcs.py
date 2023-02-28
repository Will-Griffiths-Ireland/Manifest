# gen 20k pass objects
for i in range(20000):
        c.PSNGR_LIST.append(pc.Passenger())
    total_p = 0
    total_p_norm = 0
    total_p_med = 0
    total_p_high = 0

    for count, value in enumerate(c.PSNGR_LIST):
        total_p +=1
        if c.PSNGR_LIST[count].threat_level == "high":
            total_p_high +=1
        elif c.PSNGR_LIST[count].threat_level == "medium":
            total_p_med +=1
        else:
            total_p_norm +=1

    scr.addstr(2,2 , "TOTAL PASSENGERS - " + str(total_p))
    scr.addstr(3,2 , "TOTAL NORMAL PASSENGERS - " + str(total_p_norm))
    scr.addstr(4,2 , "TOTAL MED RISK PASSENGERS - " + str(total_p_med))
    scr.addstr(5,2 , "TOTAL HI RISK PASSENGERS - " + str(total_p_high))
    scr.refresh()
    scr.getch()