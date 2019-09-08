"""Module for generating passwords and measure strength"""
import random

UPPERCASE_CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWERCASE_CHARACTERS = "abcdefghijklmnopqrstuvwxyz"
LETTERS = UPPERCASE_CHARACTERS + LOWERCASE_CHARACTERS
NUMERICAL_CHARACTERS = "0123456789"
SYMBOL_CHARACTERS = "*$-+?_&=!%{}/"
ALL_CHARACTERS = UPPERCASE_CHARACTERS + LOWERCASE_CHARACTERS + \
                 NUMERICAL_CHARACTERS + SYMBOL_CHARACTERS


def generate_password(length):
    """Generates Password of a given length from possible character set."""
    possible_characters_count = len(ALL_CHARACTERS)
    password = ""
    for _ in range(length):
        random_int = random.randint(0, possible_characters_count - 1)
        password = password + ALL_CHARACTERS[random_int]
    return password


def measure_strength(password):
    """Password strength measurer. Returns integer value"""
    strength = 0
    length = len(password)
    if length == 0:
        return strength
    upper = 0
    lower = 0
    digits = 0
    special = 0

    for i in range(length):
        if password[i].isalpha():
            if password[i].islower():
                lower = lower + 1
            else:
                upper = upper + 1
        elif password[i].isdigit():
            digits = digits + 1
        else:
            special = special + 1

    strength = strength + length * 4
    strength = strength + (length - upper) * 2
    strength = strength + (length - lower) * 2
    strength = strength + digits * 4
    strength = strength + special * 6

    if only_contains_these(password, LETTERS):
        strength = strength - length * 2
    if only_contains_these(password, NUMERICAL_CHARACTERS):
        strength = strength - length * 2

    return strength


def only_contains_these(password, char_set):
    """Checks if password only contains a certain set of characters."""
    password = set(password)
    char_set = set(char_set)
    result = password & char_set
    if len(result) == len(password):
        return True
    return False
