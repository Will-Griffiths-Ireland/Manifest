import random
import config as c
import data_loader as dl


def rand(start, stop):
    """
        Simple function to return random int
        Basic alias to shorten lines
    """
    return random.randint(start, stop)



def gen_passenger_threat_level():
    """
        Randomly spawn bad actors in passengers
        Set a threat level of high for dangerous ones (need arrest)
        Medium is for bad details (reject)
        None are all good passengers
    """
    chance = rand(1, 100)
    if chance < 1000:
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


def gen_voice_com_id():
    """
        Generate a voice com Id
        Regen to avoid duplication
    """
    duplicate = True
    while duplicate:
        temp_com_id = rand(111111111111, 999999999999)
        if len(c.PSNGR_LIST) > 0:
            for i in range(len(c.PSNGR_LIST) - 1):
                if temp_com_id == c.PSNGR_LIST[i].m_voice_com_id:
                    duplicate = True
                    break
        duplicate = False
    return temp_com_id


def gen_passenger_ueri():
    """
        Generate a UERI (United Earth Resident Identifier)
        Regen to avoid duplication
    """
    duplicate = True
    while duplicate:
        temp_ueri = ""
        for i in range(4):
            for i in range(4):
                temp_ueri += c.VALID_KEYS[rand(0, len(c.VALID_KEYS) - 1)]
            if len(temp_ueri) < 15:
                temp_ueri += "-"
        if len(c.PSNGR_LIST) > 0:
            for i in range(len(c.PSNGR_LIST) - 1):
                if temp_ueri == c.PSNGR_LIST[i].m_ueri:
                    duplicate = True
                    break
        duplicate = False
    return temp_ueri


class Passenger():
    """
        Create a new passsenger
    """

    def __init__(self):
        """
            Init field data and generate field values where needed
        """
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
        self.m_citizenship = c.COUNTRY_NAMES[rand(0, len(c.COUNTRY_NAMES) - 1)]
        self.i_citizenship = self.m_citizenship
        self.m_height = rand(85, 240)
        self.i_height = self.m_height
        self.m_hair_color = c.HAIR_COLOUR[rand(0, len(c.HAIR_COLOUR) - 1)]
        self.i_hair_color = self.m_hair_color
        self.m_profession = c.PROFESSION[rand(0, len(c.PROFESSION) - 1)]
        self.i_profession = self.m_profession
        self.m_marital_stat = \
            c.MARITAL_STATUS[rand(0, len(c.MARITAL_STATUS) - 1)]
        self.i_marital_stat = self.m_marital_stat
        self.m_blood_type = c.BLOOD_TYPES[rand(0, len(c.BLOOD_TYPES) - 1)]
        self.i_blood_type = self.m_blood_type
        self.m_allergies = c.ALLERGIES[rand(0, len(c.ALLERGIES) - 1)]
        self.i_allergies = self.m_allergies
        self.m_voice_com_id = gen_voice_com_id()
        self.i_voice_com_id = self.m_voice_com_id
        self.m_credit_rating = \
            c.CREDIT_RATING[rand(0, len(c.CREDIT_RATING) - 1)]
        self.i_credit_rating = self.m_credit_rating
        self.m_edu_lv = c.EDU_LVS[rand(0, len(c.EDU_LVS) - 1)]
        self.i_edu_lv = self.m_edu_lv
        self.m_ueri = gen_passenger_ueri()
        self.i_ueri = self.m_ueri
        self.m_mentak_alignment = \
            c.MENTAK_ALIGNMENTS[rand(0, len(c.MENTAK_ALIGNMENTS) - 1)]
        self.i_mentak_alignment = self.m_mentak_alignment
        self.m_dna_fingerprint = gen_dna_fingerprint()
        self.i_dna_fingerprint = self.m_dna_fingerprint
        self.modify_implant_data()

    def modify_implant_data(self):
        """
            Manipulate fields to create bad passengers
        """
        if self.threat_level == "high":
            # Pick 1 or 2 fields to modify. Small 1 byte change
            self.i_dna_fingerprint = gen_dna_fingerprint()
        if self.threat_level == "Medium":
            # Pick 1 or 2 fields to modify. total obvious swap
            pass
