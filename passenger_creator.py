import random
import config as c
import data_loader as dl


def rand(start, stop):
    """
        Simple function to return random int
        Basic alias to shorten lines
    """
    return random.randint(start, stop)

def create_record_anomaly(source_rec, rec_field_type):
    """
        Introduce record anomlaies whihc require reject
        or arrest actions
    """
    pass


def gen_passenger_threat_level():
    """
        Randomly spawn bad actors in passengers
        Set a threat level of high for dangerous ones (need arrest)
        Medium is for bad details (reject)
        None are all good passengers
    """
    chance = rand(1, 100)
    if chance < 10:
        return "high"
    if chance > 85:
        return "medium"
    return "none"


def gen_ticket_token():
    """
        Generate new ticket token in format IIS-XXXXXXXX
        Check on the rare chance it has already been generated
        during this playthrough and generate another
    """
    token_duplicate = True
    while token_duplicate:
        temp_token = "IIS-"
        for i in range(8):
            temp_token += c.VALID_KEYS[rand(0, (len(c.VALID_KEYS) - 1))]
        if len(c.PSNGR_LIST) > 0:
            for i in range(len(c.PSNGR_LIST) - 1):
                if temp_token == c.PSNGR_LIST[i].m_ticket_token:
                    token_duplicate = True
                    break
        token_duplicate = False
    return temp_token


def gen_cabin_id():
    """
        Generate new cabin ID
        Check on the rare chance it has already been generated
        during this playthrough and generate another
    """
    token_duplicate = True
    while token_duplicate:
        temp_cabin_id = "CAB-"
        for i in range(5):
            temp_cabin_id += c.VALID_KEYS[rand(0, (len(c.VALID_KEYS) - 1))]
        if len(c.PSNGR_LIST) > 0:
            for i in range(len(c.PSNGR_LIST) - 1):
                if temp_cabin_id == c.PSNGR_LIST[i].m_cabin_id:
                    token_duplicate = True
                    break
        token_duplicate = False
    return temp_cabin_id


def gen_dna_fingerprint():
    """
        Generate digital dna fingerprint
        Check on the rare chance it has already been generated
        during this playthrough and generate another
    """
    token_duplicate = True
    while token_duplicate:
        temp_dna = ""
        temp_chars = ["+", "|"]
        for i in range(200):
            temp_dna += temp_chars[rand(0, 1)]
        if len(c.PSNGR_LIST) > 0:
            for i in range(len(c.PSNGR_LIST) - 1):
                if temp_dna == c.PSNGR_LIST[i].m_dna_fingerprint:
                    token_duplicate = True
                    break
        token_duplicate = False
    return temp_dna


def gen_passenger_name(sex):
    """
        Pick out random passenger name
        Takes sex as input
        Remove name from the list
        if all names are used then call the data_loader and refil list
    """
    if len(c.MALE_NAMES) < 1 or len(c.FEMALE_NAMES) < 1:
        dl.gen_data_lists()

    if sex == "MALE":
        index = rand(0, len(c.MALE_NAMES) - 1)
        temp_name = c.MALE_NAMES[index]
        c.MALE_NAMES.pop(index)
    else:
        index = rand(0, len(c.FEMALE_NAMES) - 1)
        temp_name = c.FEMALE_NAMES[index]
        c.FEMALE_NAMES.pop(index)
    return temp_name


def gen_passenger_sex():
    """
        Pick out random sex
    """
    temp_sex = ["MALE", "FEMALE"]
    return temp_sex[rand(0, 1)]


class Passenger():
    """
        Build random passenger details
        Ticket token is master and never corrupt/hidden
        Manifest details are the truth
        Passenger details that differ from manifest are suspect
    """

    def __init__(self):
        self.threat_level = gen_passenger_threat_level()
        self.m_ticket_token = gen_ticket_token()
        self.i_ticket_token = self.m_ticket_token
        self.m_cabin_id = gen_cabin_id()
        self.i_cabin_id = self.m_cabin_id
        self.m_cabin_class = c.CABIN_CLASS[rand(0, len(c.CABIN_CLASS) - 1)]
        self.i_cabin_class = self.m_cabin_class
        self.m_sex = gen_passenger_sex()
        self.i_sex = self.m_sex
        self.m_name = gen_passenger_name(self.m_sex)
        self.i_name = self.m_name
        self.m_age = rand(18, 130)
        self.i_age = self.m_age


        self.m_dna_fingerprint = gen_dna_fingerprint()
        self.i_dna_fingerprint = self.m_dna_fingerprint
