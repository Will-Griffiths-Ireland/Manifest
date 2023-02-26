import random
import config as c

def gen_data_lists():
    """
        Build lists from stored data
        Input key list
        Passenger attributes
        Dialog responses
    """
    #global VALID_KEYS

    c.VALID_KEYS = []
    f = open("./assets/data/alfanum.txt", "r")
    data = f.read()
    f.close()
    for ch in data:
        c.VALID_KEYS.append(ch)
    
    c.MARITAL_STATUS = []
    f = open('./assets/data/marital_status.text')
    data = f.read().splitlines()
    f.close()
    for line in data:
        c.MARITAL_STATUS.append(line.upper())

    c.PROFESSION = []
    f = open('./assets/data/professions.text')
    data = f.read().splitlines()
    f.close()
    for line in data:
        c.PROFESSION.append(line.upper())

    c.HAIR_COLOUR = []
    f = open('./assets/data/hair_colours.text')
    data = f.read().splitlines()
    f.close()
    for line in data:
        c.HAIR_COLOUR.append(line.upper())

    c.P_SCAN_RESP = []
    f = open('./assets/data/passenger_scan_response.txt')
    data = f.read().splitlines()
    f.close()
    for line in data:
        c.P_SCAN_RESP.append(line.upper())

    c.SO_SCAN_REQ = []
    f = open('./assets/data/secoff_scan_request')
    data = f.read().splitlines()
    f.close()
    for line in data:
        c.SO_SCAN_REQ.append(line.upper())

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

    c.MALE_NAMES = []
    f = open('./assets/data/male_names.txt')
    data = f.read().splitlines()
    f.close()
    for line in data:
        c.MALE_NAMES.append(line.upper())

    c.FEMALE_NAMES = []
    f = open('./assets/data/female_names.txt')
    data = f.read().splitlines()
    f.close()
    for line in data:
        c.FEMALE_NAMES.append(line.upper())
    
    c.COUNTRY_NAMES = []
    f = open('./assets/data/country_names.txt')
    data = f.read().splitlines()
    f.close()
    for line in data:
        c.COUNTRY_NAMES.append(line.upper())