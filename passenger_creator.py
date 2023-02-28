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
    if chance > 80:
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
    digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    while duplicate:
        temp_com_id = ""
        for i in range(12):
            temp_com_id += str(digits[rand(0, len(digits) - 1)])
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


def anom_injection(field):
    """
        change 1 char
    """
    temp_list = []
    modify_count = 1
    size = len(field)
    if size > 50:
        modify_count = 25

    modifying = True

    for count, value in enumerate(field):
        temp_list.append(value)

    while modifying:
        temp_loc = rand(0, size - 1)
        if temp_list[temp_loc] not in [" ", "-"]:
            if size < 50:
                temp_c = c.VALID_KEYS[rand(0, len(c.VALID_KEYS) - 1)]
                if temp_list[temp_loc] != temp_c:
                    temp_list[temp_loc] = temp_c
                    modify_count -= 1
            if size > 50:
                dna_bit = ["+", "|"]
                temp_c = dna_bit[rand(0, 1)]
                if temp_list[temp_loc] != temp_c:
                    temp_list[temp_loc] = temp_c
                    modify_count -= 1
        if modify_count == 0:
            modifying = False

    field = ""
    for count, value in enumerate(temp_list):
        field += value

    return field

class Passenger():
    """
        Create a new passsenger
    """

    def __init__(self):
        """
            Init field data and generate field values where needed
            M_ are manifest records
            I_ are implant records
        """
        self.threat_level = gen_passenger_threat_level()
        self.boarding_status = ""
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
            medium threats should be easy to spot and reject.
            high threats will only have tiny data discrepencies
        """
        if self.threat_level == "high":
            rs = rand(1, 18)
            if rs == 1:
                self.i_cabin_id = anom_injection(self.i_cabin_id)
            if rs == 2:
                self.i_cabin_class = anom_injection(self.i_cabin_class)
            if rs == 3:
                self.i_name = anom_injection(self.i_name)
            if rs == 4:
                while self.i_age == self.m_age:
                    self.i_age += rand(-4, 4)
            if rs == 5:
                self.i_sex = anom_injection(self.i_sex)
            if rs == 6:
                self.i_citizenship = anom_injection(self.i_citizenship)
            if rs == 7:
                while self.i_height == self.m_height:
                    self.i_height += rand(-10, 10)
            if rs == 8:
                self.i_hair_color = anom_injection(self.i_hair_color)
            if rs == 9:
                self.i_profession = anom_injection(self.i_profession)
            if rs == 10:
                self.i_marital_stat = anom_injection(self.i_marital_stat)
            if rs == 11:
                self.i_blood_type = anom_injection(self.i_blood_type)
            if rs == 12:
                self.i_allergies = anom_injection(self.i_allergies)
            if rs == 13:
                self.i_voice_com_id = anom_injection(self.i_voice_com_id)
            if rs == 14:
                self.i_credit_rating = anom_injection(self.i_credit_rating)
            if rs == 15:
                self.i_edu_lv = anom_injection(self.i_edu_lv)
            if rs == 16:
                self.i_ueri = anom_injection(self.i_ueri)
            if rs == 17:
                self.i_mentak_alignment = \
                    anom_injection(self.i_mentak_alignment)
            if rs == 18:
                self.i_dna_fingerprint = anom_injection(self.i_dna_fingerprint)

        if self.threat_level == "medium":
            rs = rand(1, 18)
            if rs == 1:
                self.i_cabin_id = gen_cabin_id()
            if rs == 2:
                while self.i_cabin_class == self.m_cabin_class:
                    self.i_cabin_class = \
                        c.CABIN_CLASS[rand(0, len(c.CABIN_CLASS) - 1)]
            if rs == 3:
                self.i_name = gen_passenger_name(self.m_sex)
            if rs == 4:
                while self.i_age == self.m_age:
                    self.i_age = rand(18, 130)
            if rs == 5:
                while self.i_sex == self.m_sex:
                    self.i_sex = gen_passenger_sex()
            if rs == 6:
                while self.i_citizenship == self.m_citizenship:
                    self.i_citizenship = \
                        c.COUNTRY_NAMES[rand(0, len(c.COUNTRY_NAMES) - 1)]
            if rs == 7:
                while self.i_height == self.m_height:
                    self.i_height = rand(85, 240)
            if rs == 8:
                while self.i_hair_color == self.m_hair_color:
                    self.i_hair_color = \
                        c.HAIR_COLOUR[rand(0, len(c.HAIR_COLOUR) - 1)]
            if rs == 9:
                while self.i_profession == self.m_profession:
                    self.i_profession = \
                        c.PROFESSION[rand(0, len(c.PROFESSION) - 1)]
            if rs == 10:
                while self.i_marital_stat == self.m_marital_stat:
                    self.i_marital_stat = \
                        c.MARITAL_STATUS[rand(0, len(c.MARITAL_STATUS) - 1)]
            if rs == 11:
                while self.i_blood_type == self.m_blood_type:
                    self.i_blood_type = \
                        c.BLOOD_TYPES[rand(0, len(c.BLOOD_TYPES) - 1)]
            if rs == 12:
                while self.i_allergies == self.m_allergies:
                    self.i_allergies = \
                        c.ALLERGIES[rand(0, len(c.ALLERGIES) - 1)]
            if rs == 13:
                self.i_voice_com_id = gen_voice_com_id()
            if rs == 14:
                while self.i_credit_rating == self.m_credit_rating:
                    self.i_credit_rating = \
                        c.CREDIT_RATING[rand(0, len(c.CREDIT_RATING) - 1)]
            if rs == 15:
                while self.i_edu_lv == self.m_edu_lv:
                    self.i_edu_lv = c.EDU_LVS[rand(0, len(c.EDU_LVS) - 1)]
            if rs == 16:
                self.i_ueri = gen_passenger_ueri()
            if rs == 17:
                while self.i_mentak_alignment == self.m_mentak_alignment:
                    temp = \
                        c.MENTAK_ALIGNMENTS[
                            rand(0, len(c.MENTAK_ALIGNMENTS) - 1)]
                    self.i_mentak_alignment = temp
            if rs == 18:
                self.i_dna_fingerprint = gen_dna_fingerprint()

