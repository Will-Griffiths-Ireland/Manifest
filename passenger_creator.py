import random
import config as c


def rand(start, stop):
    """
        Simple function to return random int
        Basic alias to shorten lines
    """
    return random.randint(start, stop)


def gen_ticket_token():
    """
        Generate new ticket token in format IIS-XXXXXXXX
        Check on the rare chance it has already been generated
    """
    temp_token = "IIS-"
    token_duplicate = True
    dup_count = 0
    #while token_duplicate:
    for i in range(8):
        let = c.VALID_KEYS[rand(0, (len(c.VALID_KEYS) - 1))]
        temp_token += let
        # for i in range(len(c.PSNGR_LIST)):
        #     if temp_token == c.PSNGR_LIST[i].ticket_token:
        #         token_duplicate = True
        #         dup_count += 1
        #         break
        #     else:
        #         token_duplicate = False

    return temp_token

class Passenger():
    def __init__(self, bad_actor, difficulty):
        self.ticket_token = gen_ticket_token()