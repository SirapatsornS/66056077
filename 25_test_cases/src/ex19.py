"""
Exercise 19 : Password Generator
"""
import random

LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'    # 26
UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'    # 26
NUMBERS = '1234567890'                          # 10
SPECIAL = '~!@#$%^&*()_+'                       # 13

ALL_CHARS = LOWER_LETTERS + UPPER_LETTERS + NUMBERS + SPECIAL


def gen_password(passlength):
    # Fix : complete this
    if passlength < 12:
        passlength = 12
    ranpass = []
    ranpass.append(LOWER_LETTERS[random.randint(0, 25)])
    ranpass.append(UPPER_LETTERS[random.randint(0, 25)])
    ranpass.append(NUMBERS[random.randint(0, 9)])
    ranpass.append(SPECIAL[random.randint(0, 12)])

    while len(ranpass) < passlength:
        ranpass.append(ALL_CHARS[random.randint(0, 74)])
        random.shuffle(ranpass)

    return ''.join(ranpass)