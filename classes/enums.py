from enum import Enum

class Time(Enum):
    TEN_AM = 1
    ELEVEN_AM = 2
    TWELVE_PM = 3
    ONE_PM = 4
    TWO_PM = 5
    THREE_PM = 6

class Faculty(Enum):
    GHARIBI = 1
    GLADBACH = 2
    HARE = 3
    NAIT_ABDESSELAM = 4
    SHAH = 5
    SONG = 6
    UDDIN = 7
    XU = 8
    ZAMAN = 9
    ZEIN_EL_DIN = 10

class Room(Enum):
    KATZ_003 = 1
    FH_216 = 2
    ROYALL_206 = 3
    ROYALL_201 = 4
    FH_310 = 5
    HAAG_201 = 6
    HAAG_301 = 7
    MNLC_325 = 8
    BLOCH_119 = 9

class Course(Enum):
    CS101 = 1
    CS191 = 2
    CS201 = 3
    CS291 = 4
    CS303 = 5
    CS304 = 6
    CS394 = 7
    CS449 = 8
    CS451 = 9
    CS499 = 10