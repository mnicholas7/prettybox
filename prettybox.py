#!/usr/bin/python3
import sys
import time
import re
import random
import fileinput


def SNOOZE(x):

    print(f"  SNOOZE for {x} total seconds!")
    z = range(x, 1, -1)
    for i in z:
        m = RAND_CH()
        # MSG = f"{m} {i}"
        MSG = f"{m}"
        # printf(MSG)
        if i % 4 == 0:
            print(MSG, end=" ", flush=True)
        elif i % 1 == 0:
            print(".", end=" ", flush=True)

        time.sleep(1)


def MAX_PAD(LIST):
    MAX = max([len(i) for i in LIST])
    return MAX


def RAND_CH(COLOR=None):

    # COLOR = 1

    # HEADER = '\033[95m'
    # OKBLUE = '\033[94m'
    # OKCYAN = '\033[96m'
    # OKGREEN = '\033[92m'
    # WARNING = '\033[93m'
    # FAIL = '\033[91m'
    # ENDC = '\033[0m'
    # BOLD = '\033[1m'
    # UNDERLINE = '\033[4m'

    color = [
        "\033[95m",
        "\033[94m",
        "\033[96m",
        "\033[92m",
        "\033[93m",
        "\033[91m",
        "\033[0m",
        "\033[1m",
        "\033[4m",
    ]

    mylist = [
        "Ω",
        "∑",
        "ф",
        "Ш",
        "ǒ",
        "∆",
        "∝",
        "ǯ",
        "λ",
        "ô",
        "ŕ",
        "÷",
        "έ",
        "√",
        "♢",
        "♣",
        "♠",
        "☼",
        " ",
        "ﬁ",
        "©",
        "¬",
        "¬",
        "ĳ",
        "¢",
        "æ",
        "¿",
        "¡",
        "½",
        "⑃",
        "⑀",
        "℗",
        "≈",
        "«",
        "»",
        "³",
        "∀",
        "∞",
        "⊙",
        " ",
        "♫",
        "¹",
        "ý",
        "ė",
        "õ",
        "ï",
        "ö",
        "ř",
        "φ",
        "Ϟ",
        "ж",
        "Д",
        "δ",
        "Љ",
        "Ψ",
        "š",
        "Λ",
        "Μ",
        "ŧ",
        "°",
        "ש",
        "Π",
        " ",
        "ẘ",
        "ḿ",
        "ق",
        "†",
        "₩",
        "⁸",
        "▢",
        "∴",
        "▣",
        "▦",
        "▧",
        "▩",
        "▭",
        "□",
        "␣",
        "₽",
        " ",
        "◐",
        "◑",
        "◊",
        "¬",
        "▽",
        "♪",
        "ﬀ",
        "☆",
        "°",
        "©",
        "¥",
        "¯",
        "¢",
        "Ï",
        "ć",
        "ċ",
        "£",
        "ƣ",
        "Œ",
        "œ",
        "Φ",
        "џ",
        "Ḻ",
        "ל",
        "ζ",
        "ς",
        "ѫ",
        "ج",
        "ד",
        "ж",
        "پ",
        "љ",
        "ƶ",
        "я",
        "x",
        "Г",
        "π",
        "ΐ",
        "ξ",
        "â",
        "¶",
        "ẘ",
        "ẙ",
        "⇒",
        "≤",
        "‴",
        "•",
        "₇",
        "۰",
        "Ζ",
        "گ",
        "Ħ",
        "ы",
        "Л",
        "ע",
        "ח",
        "ט",
        "י",
        "ґ",
        "כ",
        "ר",
        "ą",
        "ץ",
        "ط",
        "آ",
        "ї",
        "ס",
        "Ĺ",
        "ϛ",
        "ή",
        "ך",
        "ם",
        "ג",
        "Γ",
        "γ",
        "φ",
        "ⅷ",
        "Ⅰ",
        "Á",
        "Ⅰ",
        "Ⅱ",
        "Ⅲ",
        "Ⅳ",
        "Ⅴ",
        "Ⅵ",
        "Ⅶ",
        "Ⅷ",
        "Ⅸ",
        "◑",
        "۰",
        "۱",
        "۲",
        "۳",
        "۴",
        "۵",
        "۶",
        "۷",
        "۸",
        "۹",
        "б",
        "※",
        "ⁿ",
        "ŀ",
        "ĵ",
        "İ",
        "т",
        "⅓",
        "⅕",
        "⅔",
        "⅖",
        "∾",
        "∧",
        "∨",
        "┌",
        "┘",
        "∃",
        "Ǯ",
        "п",
        "‖",
    ]

    CH = random.choice(mylist)
    color = random.choice(color)

    if COLOR:
        CH = color + CH
        return str(CH)
    else:
        pass

    return str(CH)


def LOOP_TEST(LOOPCOUNT):

    MSG = """
    
    help> topics
    
    Here is a list of available topics.  Enter any topic name to get more help.
    
    ASSERTION           DELETION            LOOPING             SHIFTING
    ASSIGNMENT          DICTIONARIES        MAPPINGMETHODS      SLICINGS
    ATTRIBUTEMETHODS    DICTIONARYLITERALS  MAPPINGS            SPECIALATTRIBUTES
    ATTRIBUTES          DYNAMICFEATURES     METHODS             SPECIALIDENTIFIERS
    AUGMENTEDASSIGNMENT ELLIPSIS            MODULES             SPECIALMETHODS
    BASICMETHODS        EXCEPTIONS          NAMESPACES          STRINGMETHODS
    BINARY              EXECUTION           NONE                STRINGS
    BITWISE             EXPRESSIONS         NUMBERMETHODS       SUBSCRIPTS
    BOOLEAN             FLOAT               NUMBERS             TRACEBACKS
    CALLABLEMETHODS     FORMATTING          OBJECTS             TRUTHVALUE
    CALLS               FRAMEOBJECTS        OPERATORS           TUPLELITERALS
    CLASSES             FRAMES              PACKAGES            TUPLES
    CODEOBJECTS         FUNCTIONS           POWER               TYPEOBJECTS
    COMPARISON          IDENTIFIERS         PRECEDENCE          TYPES
    COMPLEX             IMPORTING           PRIVATENAMES        UNARY
    CONDITIONAL         INTEGER             RETURNING           UNICODE
    CONTEXTMANAGERS     LISTLITERALS        SCOPING
    CONVERSIONS         LISTS               SEQUENCEMETHODS
    DEBUGGING           LITERALS            SEQUENCES
    
    
    
    
    """

    for i in range(1, LOOPCOUNT):
        x = RAND_CH()

        x = RAND_CH()
        print(NEW(f"This is iteration {i}", 9, 1))
        MSG_OUT = NEW(MSG, 9, 1)
        # print(NEW(MSG2,9,1))
        print(MSG_OUT)
        SNOOZE(4)


def NEW(MSG, COMPLEXITY, QUIET=None):
    def DRAW_BOX(MSG):

        LIST = MSG.split("\n")

        LIST = [re.sub(r"^\s+", "", i) for i in LIST]
        LIST = [re.sub(r"\s+$", "", i) for i in LIST]
        LIST = [re.sub(r"^\s+$", "", i) for i in LIST]
        LIST = [i for i in LIST if i]

        BORDER_SPACE = random.randint(0, 9)

        OPT = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

        if BORDER_SPACE == OPT[0]:
            pass

        elif BORDER_SPACE == OPT[1]:

            LIST = [re.sub(r"^", " ", i) for i in LIST]
            LIST = [re.sub(r"$", " ", i) for i in LIST]

        elif BORDER_SPACE == OPT[2]:

            LIST = [re.sub(r"^", "  ", i) for i in LIST]
            LIST = [re.sub(r"$", "  ", i) for i in LIST]

        elif BORDER_SPACE == OPT[3]:

            LIST = [re.sub(r"^", "    ", i) for i in LIST]
            LIST = [re.sub(r"$", "    ", i) for i in LIST]

        elif BORDER_SPACE == OPT[4]:

            LIST = [re.sub(r"^", " ", i) for i in LIST]
            LIST = [re.sub(r"$", "  ", i) for i in LIST]

        elif BORDER_SPACE == OPT[5]:

            LIST = [re.sub(r"^(\s+)", r" \1", i) for i in LIST]
            LIST = [re.sub(r"$", " ", i) for i in LIST]

        elif BORDER_SPACE == OPT[6]:

            LIST = [re.sub(r"^", "    ", i) for i in LIST]
            LIST = [re.sub(r"$", "", i) for i in LIST]

        elif BORDER_SPACE == OPT[7]:

            LIST = [re.sub(r"^", "", i) for i in LIST]
            LIST = [re.sub(r"$", "    ", i) for i in LIST]

        elif BORDER_SPACE == OPT[8]:

            LIST = [re.sub(r"^", "", i) for i in LIST]
            LIST = [re.sub(r"$", "   ", i) for i in LIST]

        elif BORDER_SPACE == OPT[8]:

            LIST = [re.sub(r"^", "", i) for i in LIST]
            LIST = [re.sub(r"$", "  ", i) for i in LIST]

        elif BORDER_SPACE == OPT[7]:

            LIST = [re.sub(r"^", "    ", i) for i in LIST]
            LIST = [re.sub(r"$", "", i) for i in LIST]

        elif BORDER_SPACE == OPT[8]:

            LIST = [re.sub(r"^", "    ", i) for i in LIST]
            LIST = [re.sub(r"$", " ", i) for i in LIST]

        elif BORDER_SPACE == OPT[9]:

            LIST = [re.sub(r"^", "     ", i) for i in LIST]
            LIST = [re.sub(r"$", "  ", i) for i in LIST]

        VERT_SPACE = random.randint(0, 8)

        OPT = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        if VERT_SPACE == OPT[0]:
            pass

        elif VERT_SPACE == OPT[1]:
            LIST = ["\n"] + LIST[:] + ["\n"]

        elif VERT_SPACE == OPT[2]:

            LIST = ["\n", "\n"] + LIST[:] + ["\n", "\n"]

        elif VERT_SPACE == OPT[3]:

            LIST = ["\n", "\n", "\n"] + LIST[:] + ["\n", "\n"]

        elif VERT_SPACE == OPT[4]:

            LIST = ["\n"] + LIST[:]

        elif VERT_SPACE == OPT[5]:

            LIST = ["\n", "\n"] + LIST[:]

        elif VERT_SPACE == OPT[6]:

            LIST = ["\n", "\n", "\n"] + LIST[:]

        elif VERT_SPACE == OPT[7]:

            LIST = ["\n"] + LIST[:]

        elif VERT_SPACE == OPT[8]:

            LIST = LIST[:] + ["\n"]

        MAX_PAD = max([len(i) for i in LIST])

        if len(LIST) > 1:
            MSG += "\n".join([f"{line:{MAX_PAD}}" for line in LIST])

        x = RAND_CH()

        QUAD = round(MAX_PAD / 4)
        QUAD_RAND_INT = random.randint(1, QUAD)
        NEG_QUAD_SPACE = QUAD - QUAD_RAND_INT or 1

        EIGHT = round(MAX_PAD / 8)
        EIGHT_RAND_INT = random.randint(1, EIGHT)
        DIFF_EIGHT = EIGHT - EIGHT_RAND_INT

        E1 = EIGHT_RAND_INT
        E2 = DIFF_EIGHT

        THIRD = round(MAX_PAD / 3)
        THIRD_RAND_INT = random.randint(1, THIRD)
        DIFF_THIRD = THIRD - THIRD_RAND_INT

        RAND_INT = random.randint(1, MAX_PAD)
        DIFF_INT = MAX_PAD - RAND_INT  # DONT USE THIS, YOU'LL USE ALL THAT"S LEFT !
        DIFF_INT2 = round(DIFF_INT / 3)

        NL = "\n"

        BOX1 = f"""
{x *     3}{' ' * int(DIFF_INT2)}{x * int((DIFF_INT2))}{' ' * int(DIFF_INT2)}{x * RAND_INT}   
{NL.    join([f"{x}{line:{int(MAX_PAD )}}{x}" for line in LIST])}
{x *     RAND_INT}{' ' * int(DIFF_INT2)}{x * int((DIFF_INT2))}{' ' * int(DIFF_INT2)}{x * 3}
"""
        BOX1A = f"""
{x *     3}{' ' * int(DIFF_INT2)}{x * int((DIFF_INT2))}{' ' * int(DIFF_INT2)}{x * RAND_INT}   
{NL.    join([f"{line:{int(MAX_PAD )}}" for line in LIST])}
{x *     RAND_INT}{' ' * int(DIFF_INT2)}{x * int((DIFF_INT2))}{' ' * int(DIFF_INT2)}{x * 3}
"""
        BOX2 = f"""
{x *     RAND_INT}{' ' * int(DIFF_INT2)}{x * int((DIFF_INT2))}{' ' * int(DIFF_INT2)}{x * 3}
{NL.    join([f"{x}{line:{int(MAX_PAD )}}{x}" for line in LIST])}
{x *     3}{' ' * int(DIFF_INT2)}{x * int((DIFF_INT2))}{' ' * int(DIFF_INT2)}{x * RAND_INT}   
"""
        BOX2A = f"""
{x *     RAND_INT}{' ' * int(DIFF_INT2)}{x * int((DIFF_INT2))}{' ' * int(DIFF_INT2)}{x * 3}
{NL.    join([f"{line:{int(MAX_PAD )}}" for line in LIST])}
{x *     3}{' ' * int(DIFF_INT2)}{x * int((DIFF_INT2))}{' ' * int(DIFF_INT2)}{x * RAND_INT}   
"""

        BOX3 = f"""
{' '     * int(DIFF_INT2)}{x * int((DIFF_INT2))}{' ' * int(DIFF_INT2)}{x * RAND_INT}
{NL.    join([f"{x}{line:{int(MAX_PAD )}}{x}" for line in LIST])}
{x *     RAND_INT}{' ' * int(DIFF_INT2)}{x * int((DIFF_INT2))}{' ' * int(DIFF_INT2)}
"""

        BOX4 = f"""
{' '     * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}
{NL.    join([f"{x}{line:{int(MAX_PAD )}}{x}" for line in LIST])}
{x *     int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}
"""

        BOX5 = f"""
{x *     int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x}
{NL.    join([f"{x}{line:{int(MAX_PAD )}}{x}" for line in LIST])}
{x}{    ' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}
"""

        BOX6 = f"""
{x *     QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2)}{x * QUAD_RAND_INT}{x * QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2)}{x * QUAD_RAND_INT}
{NL.    join([f"{line:{int(MAX_PAD )}}" for line in LIST])}
{x *     QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2)}{x * QUAD_RAND_INT}{x * QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2)}{x * QUAD_RAND_INT}
"""
        BOX7 = f"""
{x *     int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}
{NL.    join([f"{line:{int(MAX_PAD )}}" for line in LIST])}
{x *     int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}
"""

        BOX8 = f"""
{x *     int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x}
{NL.    join([f"{x}{line:{int(MAX_PAD )}}{x}" for line in LIST])}
{x *     int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x}
"""
        BOX9 = f"""
{x *     int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x}
{NL.    join([f"{x}{line:{int(MAX_PAD )}}{x}" for line in LIST])}
{x}{    ' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}
"""
        BOX9A = f"""
{x *     int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x}
{NL.    join([f"{line:{int(MAX_PAD )}}" for line in LIST])}
{x}{    ' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}
"""

        BOX10 = f"""
{x *     QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2)}{x * QUAD_RAND_INT}{x * QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2 + 1)}{x * QUAD_RAND_INT}
{NL.    join([f"{x}{line:{int(MAX_PAD )}}{x}" for line in LIST])}
{x *     QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2)}{x * QUAD_RAND_INT}{x * QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2 + 1)}{x * QUAD_RAND_INT}
"""
        BOX11 = f"""
{x *     QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2)}{' ' * QUAD_RAND_INT}{' ' * QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2 + 1)}{x * QUAD_RAND_INT}
{NL.    join([f"{x}{line:{int(MAX_PAD )}}{x}" for line in LIST])}
{x *     QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2)}{' ' * QUAD_RAND_INT}{' ' * QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2 + 1)}{x * QUAD_RAND_INT}
"""
        BOX12 = f"""
{x *     THIRD_RAND_INT}{' ' * int(DIFF_THIRD)}{x * THIRD_RAND_INT}{' ' * int(DIFF_THIRD)}{x * THIRD_RAND_INT}{' ' * int(DIFF_THIRD)}{x}
{NL.    join([f"{x}{line:{int(MAX_PAD )}}{x}" for line in LIST])}
{x}{    ' ' * int(DIFF_THIRD)}{x * THIRD_RAND_INT}{' ' * int(DIFF_THIRD)}{x * THIRD_RAND_INT}{' ' * int(DIFF_THIRD)}{x * THIRD_RAND_INT}
"""
        BOX12A = f"""
{x *     THIRD_RAND_INT}{' ' * int(DIFF_THIRD)}{x * THIRD_RAND_INT}{' ' * int(DIFF_THIRD)}{x * THIRD_RAND_INT}{' ' * int(DIFF_THIRD)}{x}
{NL.    join([f"{line:{int(MAX_PAD )}}" for line in LIST])}
{x}{    ' ' * int(DIFF_THIRD)}{x * THIRD_RAND_INT}{' ' * int(DIFF_THIRD)}{x * THIRD_RAND_INT}{' ' * int(DIFF_THIRD)}{x * THIRD_RAND_INT}
"""
        BOX13 = f"""
{x}{    ' ' * int(DIFF_THIRD)}{x * THIRD_RAND_INT}{' ' * int(DIFF_THIRD)}{x * THIRD_RAND_INT}{' ' * int(DIFF_THIRD)}{x * THIRD_RAND_INT}
{NL.    join([f"{x}{line:{int(MAX_PAD )}}{x}" for line in LIST])}
{x *     THIRD_RAND_INT}{' ' * int(DIFF_THIRD)}{x * THIRD_RAND_INT}{' ' * int(DIFF_THIRD)}{x * THIRD_RAND_INT}{' ' * int(DIFF_THIRD)}{x}
"""
        BOX13A = f"""
{x}{    ' ' * int(DIFF_THIRD)}{x * THIRD_RAND_INT}{' ' * int(DIFF_THIRD)}{x * THIRD_RAND_INT}{' ' * int(DIFF_THIRD)}{x * THIRD_RAND_INT}
{NL.    join([f"{line:{int(MAX_PAD )}}" for line in LIST])}
{x *     THIRD_RAND_INT}{' ' * int(DIFF_THIRD)}{x * THIRD_RAND_INT}{' ' * int(DIFF_THIRD)}{x * THIRD_RAND_INT}{' ' * int(DIFF_THIRD)}{x}
"""
        BOX14 = f"""
{x *     int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x}
{NL.    join([f"{x}{line:{int(MAX_PAD )}}{x}" for line in LIST])}
{x}{    ' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}
"""
        BOX14A = f"""
{x *     int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x}
{NL.    join([f"{line:{int(MAX_PAD )}}" for line in LIST])}
{x}{    ' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}
"""

        BOX15 = f"""
{x *     QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2)}{' ' * QUAD_RAND_INT}{' ' * QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2 + 1)}{x * QUAD_RAND_INT}
{NL.    join([f"{x}{line:{int(MAX_PAD )}}{x}" for line in LIST])}
{x *     QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2)}{' ' * QUAD_RAND_INT}{' ' * QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2 + 1)}{x * QUAD_RAND_INT}
"""
        BOX15A = f"""
{x *     QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2)}{' ' * QUAD_RAND_INT}{' ' * QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2 + 1)}{x * QUAD_RAND_INT}
{NL.    join([f"{line:{int(MAX_PAD )}}" for line in LIST])}
{x *     QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2)}{' ' * QUAD_RAND_INT}{' ' * QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2 + 1)}{x * QUAD_RAND_INT}
"""
        BOX16 = f"""
{x *     QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2)}{x * QUAD_RAND_INT}{x * QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2 + 1)}{x * QUAD_RAND_INT}
{NL.    join([f"{x}{line:{int(MAX_PAD )}}{x}" for line in LIST])}
{x *     QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2)}{x * QUAD_RAND_INT}{x * QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2 + 1)}{x * QUAD_RAND_INT}
"""
        BOX17 = f"""
{x *     QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2)}{' ' * QUAD_RAND_INT}{' ' * QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2)}{x * QUAD_RAND_INT}
{NL.    join([f"{line:{int(MAX_PAD )}}" for line in LIST])}
{x *     QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2)}{' ' * QUAD_RAND_INT}{' ' * QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2)}{x * QUAD_RAND_INT}
"""
        BOX18 = f"""
{x *     QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2)}{' ' * QUAD_RAND_INT}{' ' * QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2)}{x * QUAD_RAND_INT}
{NL.    join([f"{line:{int(MAX_PAD )}}" for line in LIST])}
{x *     QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2)}{' ' * QUAD_RAND_INT}{' ' * QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2)}{x * QUAD_RAND_INT}
"""

        LIST = [
            BOX1,
            BOX1A,
            BOX2,
            BOX2A,
            BOX3,
            BOX4,
            BOX5,
            BOX6,
            BOX8,
            BOX9,
            BOX10,
            BOX11,
            BOX12,
            BOX12A,
            BOX13,
            BOX13A,
            BOX14,
            BOX14A,
            BOX15,
            BOX15A,
            BOX16,
            BOX17,
            BOX18,
        ]
        OUT = random.choice(LIST)
        return OUT

    LUCKY = random.randint(1, 7)

    if LUCKY == 1 or COMPLEXITY == 1:
        FIRST = DRAW_BOX(MSG)

        if QUIET:
            return FIRST
        else:
            print(FIRST)
            return

    elif LUCKY == 2 or COMPLEXITY == 2:
        FIRST = DRAW_BOX(MSG)
        TWO = DRAW_BOX(FIRST)

        if QUIET:
            return TWO
        else:
            print(TWO)
            return

    elif LUCKY == 3 or COMPLEXITY == 3:
        FIRST = DRAW_BOX(MSG)
        TWO = DRAW_BOX(FIRST)
        THREE = DRAW_BOX(TWO)

        if QUIET:
            return THREE
        else:
            print(THREE)
            return

    elif LUCKY == 4 or COMPLEXITY == 4:
        FIRST = DRAW_BOX(MSG)
        TWO = DRAW_BOX(FIRST)
        THREE = DRAW_BOX(TWO)
        FOUR = DRAW_BOX(THREE)

        if QUIET:
            return FOUR
        else:
            print(FOUR)
            return

    elif LUCKY >= 5:
        MSG = DRAW_BOX(MSG)
        MSG = DRAW_BOX(MSG)
        MSG = DRAW_BOX(MSG)
        MSG = DRAW_BOX(MSG)

        if QUIET:
            return MSG
        else:
            print(MSG)
            return

def main():

    INPUT = []

    for line in fileinput.input():
        INPUT += line

    MSG = "".join(INPUT)
    NEW(MSG,9)

        

if __name__ == '__main__':

    main()



