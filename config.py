""" Global variables. Lists and flags """

# Animation delay setting
ANI_DLA = 0.0
DIFFICULTY = "CHAOS"
PSNGR_LIST = []
# Game active flag
GAME_ACT = False
GAME_ENDED = False
ENCRYPT_ON = True
DSP_GAME_TMR = False
CUR_PSNGR_NO = 0
# Decryption game active flag
DRG_ACT = False
TIME_LIMIT = 600
# Confirm action flag
CONFIRM_ACTION = False
# Decrption available flag
DECRYPT_AVAILABLE = True
DECRYPT_SUCCESS = False
# Cursor postion used for threading screen updates
G_CUR_YX = (0, 0)
# Valid input keys alphanum
VALID_KEYS = []
# Passenger data lists
CABIN_CLASS = []
MALE_NAMES = []
FEMALE_NAMES = []
COUNTRY_NAMES = []
HAIR_COLOUR = []
PROFESSION = []
MARITAL_STATUS = []
BLOOD_TYPES = []
ALLERGIES = []
CREDIT_RATING = []
EDU_LVS = []
MENTAK_ALIGNMENTS = []
# Dialog responses lists
P_APPR_ACT = []
BP_APPR_ACT = []
P_SCAN_RESP = []
BP_SCAN_RESP = []
P_REJECT_RESP = []
BP_REJECT_RESP = []
P_ARREST_RESP = []
BP_ARREST_RESP = []
P_BOARD_RSP = []
SO_WELC = []
SO_SCAN_REQ = []
SECOFF_BOARD_RSP = []
SECOFF_REJECT_RSP = []
SECOFF_ARREST_RSP = []
# Debug counters
DUP_COUNT = 0