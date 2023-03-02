""" Import random and global vards in config"""
import random
import config as c


def gen_data_lists():
    """
        Build lists from stored data files
        Input validation key list
        Passenger attributes
        Dialog responses
    """

    c.SO_FINISHED = []
    f = open('./assets/data/secoff_finished.txt')
    data = f.read().splitlines()
    f.close()
    for line in data:
        c.SO_FINISHED.append(line)
    random.shuffle(c.SO_FINISHED)

    c.SO_NEXT = []
    f = open('./assets/data/secoff_next.txt')
    data = f.read().splitlines()
    f.close()
    for line in data:
        c.SO_NEXT.append(line)
    random.shuffle(c.SO_NEXT)

    c.BP_ARREST_RESP = []
    f = open('./assets/data/bad_passenger_arrest_response.txt')
    data = f.read().splitlines()
    f.close()
    for line in data:
        c.BP_ARREST_RESP.append(line)
    random.shuffle(c.BP_ARREST_RESP)

    c.P_ARREST_RESP = []
    f = open('./assets/data/passenger_arrest_response.txt')
    data = f.read().splitlines()
    f.close()
    for line in data:
        c.P_ARREST_RESP.append(line)
    random.shuffle(c.P_ARREST_RESP)

    c.P_REJECT_RESP = []
    f = open('./assets/data/passenger_reject_response.txt')
    data = f.read().splitlines()
    f.close()
    for line in data:
        c.P_REJECT_RESP.append(line)
    random.shuffle(c.P_REJECT_RESP)

    c.BP_APPR_ACT = []
    f = open('./assets/data/bad_passenger_approach.txt')
    data = f.read().splitlines()
    f.close()
    for line in data:
        c.BP_APPR_ACT.append(line)
    random.shuffle(c.BP_APPR_ACT)

    c.P_BOARD_RSP = []
    f = open('./assets/data/passenger_board_response.txt')
    data = f.read().splitlines()
    f.close()
    for line in data:
        c.P_BOARD_RSP.append(line)
    random.shuffle(c.P_BOARD_RSP)

    c.SECOFF_ARREST_RSP = []
    f = open('./assets/data/secoff_arrest.txt')
    data = f.read().splitlines()
    f.close()
    for line in data:
        c.SECOFF_ARREST_RSP.append(line)
    random.shuffle(c.SECOFF_ARREST_RSP)

    c.SECOFF_REJECT_RSP = []
    f = open('./assets/data/secoff_reject.txt')
    data = f.read().splitlines()
    f.close()
    for line in data:
        c.SECOFF_REJECT_RSP.append(line)
    random.shuffle(c.SECOFF_REJECT_RSP)

    c.SECOFF_BOARD_RSP = []
    f = open('./assets/data/secoff_board.txt')
    data = f.read().splitlines()
    f.close()
    for line in data:
        c.SECOFF_BOARD_RSP.append(line)
    random.shuffle(c.SECOFF_BOARD_RSP)

    c.ALLERGIES = []
    f = open('./assets/data/allergies.txt')
    data = f.read().splitlines()
    f.close()
    for line in data:
        c.ALLERGIES.append(line)
    random.shuffle(c.ALLERGIES)

    c.BLOOD_TYPES = []
    f = open('./assets/data/blood_type.txt')
    data = f.read().splitlines()
    f.close()
    for line in data:
        c.BLOOD_TYPES.append(line)
    random.shuffle(c.BLOOD_TYPES)

    c.VALID_KEYS = []
    f = open("./assets/data/alfanum.txt", "r")
    data = f.read()
    f.close()
    for ch in data:
        c.VALID_KEYS.append(ch)

    c.MARITAL_STATUS = []
    f = open('./assets/data/marital_status.txt')
    data = f.read().splitlines()
    f.close()
    for line in data:
        c.MARITAL_STATUS.append(line.upper())
    random.shuffle(c.MARITAL_STATUS)

    c.PROFESSION = []
    f = open('./assets/data/professions.txt')
    data = f.read().splitlines()
    f.close()
    for line in data:
        c.PROFESSION.append(line.upper())
    random.shuffle(c.PROFESSION)

    c.HAIR_COLOUR = []
    f = open('./assets/data/hair_colours.txt')
    data = f.read().splitlines()
    f.close()
    for line in data:
        c.HAIR_COLOUR.append(line.upper())
    random.shuffle(c.HAIR_COLOUR)

    c.P_SCAN_RESP = []
    f = open('./assets/data/passenger_scan_response.txt')
    data = f.read().splitlines()
    f.close()
    for line in data:
        c.P_SCAN_RESP.append(line.upper())
    random.shuffle(c.P_SCAN_RESP)

    c.SO_SCAN_REQ = []
    f = open('./assets/data/secoff_scan_request')
    data = f.read().splitlines()
    f.close()
    for line in data:
        c.SO_SCAN_REQ.append(line.upper())
    random.shuffle(c.SO_SCAN_REQ)

    c.SO_WELC = []
    f = open('./assets/data/secoff_welcome.txt')
    data = f.read().splitlines()
    f.close()
    for line in data:
        c.SO_WELC.append(line.upper())
    random.shuffle(c.SO_WELC)

    c.P_APPR_ACT = []
    f = open('./assets/data/passenger_approach.txt')
    data = f.read().splitlines()
    f.close()
    for line in data:
        c.P_APPR_ACT.append(line.upper())
    random.shuffle(c.P_APPR_ACT)

    c.MALE_NAMES = []
    f = open('./assets/data/male_names.txt')
    data = f.read().splitlines()
    f.close()
    for line in data:
        c.MALE_NAMES.append(line.upper())
    random.shuffle(c.MALE_NAMES)

    c.FEMALE_NAMES = []
    f = open('./assets/data/female_names.txt')
    data = f.read().splitlines()
    f.close()
    for line in data:
        c.FEMALE_NAMES.append(line.upper())
    random.shuffle(c.FEMALE_NAMES)

    c.COUNTRY_NAMES = []
    f = open('./assets/data/country_names.txt')
    data = f.read().splitlines()
    f.close()
    for line in data:
        c.COUNTRY_NAMES.append(line.upper())
    random.shuffle(c.COUNTRY_NAMES)

    c.CABIN_CLASS = []
    f = open('./assets/data/cabin_classes.txt')
    data = f.read().splitlines()
    f.close()
    for line in data:
        c.CABIN_CLASS.append(line)
    random.shuffle(c.CABIN_CLASS)

    c.CREDIT_RATING = []
    f = open('./assets/data/credit_rating.txt')
    data = f.read().splitlines()
    f.close()
    for line in data:
        c.CREDIT_RATING.append(line)
    random.shuffle(c.CREDIT_RATING)

    c.EDU_LVS = []
    f = open('./assets/data/education_level.txt')
    data = f.read().splitlines()
    f.close()
    for line in data:
        c.EDU_LVS.append(line)
    random.shuffle(c.EDU_LVS)

    c.MENTAK_ALIGNMENTS = []
    f = open('./assets/data/mentak_alignments.txt')
    data = f.read().splitlines()
    f.close()
    for line in data:
        c.MENTAK_ALIGNMENTS.append(line)
    random.shuffle(c.MENTAK_ALIGNMENTS)
