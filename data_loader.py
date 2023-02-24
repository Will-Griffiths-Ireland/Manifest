# Passenger data lists
MALE_NAMES = []
FEMALE_NAMES = []
COUNTRY_NAMES = []
HAIR_COLOUR = []
# Dialog responses lists
P_APPR_ACT = []
P_SCAN_RESP = []
SO_WELC = []
SO_SCAN_REQ = []


def gen_data_lists():
    """
        Gen lists
    """
    global MALE_NAMES
    global FEMALE_NAMES
    global COUNTRY_NAMES
    global HAIR_COLOUR
    global PROFESSION
    global MARITAL_STATUS
    global P_APPR_ACT
    global SO_WELC
    global SO_SCAN_REQ
    global P_SCAN_RESP

    MARITAL_STATUS = []
    f = open('./assets/data/marital_status.text')
    data = f.read().splitlines()
    f.close()
    for line in data:
        MARITAL_STATUS.append(line.upper())

    PROFESSION = []
    f = open('./assets/data/professions.text')
    data = f.read().splitlines()
    f.close()
    for line in data:
        PROFESSION.append(line.upper())

    HAIR_COLOUR = []
    f = open('./assets/data/hair_colours.text')
    data = f.read().splitlines()
    f.close()
    for line in data:
        HAIR_COLOUR.append(line.upper())

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