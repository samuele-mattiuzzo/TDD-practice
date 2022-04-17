import re
from curses import ERR

ERROR_MESSAGES = {
    'LENGTH': 'Password must be at least 8 characters',
    'NUMBERS': 'Password must contain at least 2 numbers',
    'CAPITAL': 'Password must contain at least one capital letter',
    'SPECIAL': 'Password must contain at least one special character'
}

VALID_PASSWORD_LENGTH = 8
TWO_NUMBERS_REGEX = r'\d.*\d'
CAPITAL_LETTER_REGEX = r'[A-Z]'
SPECIAL_CHAR_REGEX = r'[^a-zA-Z\d]'


def password_validator(password):
    errors = []

    if len(password) < VALID_PASSWORD_LENGTH:
        errors.append(ERROR_MESSAGES['LENGTH'])

    if not bool(re.search(TWO_NUMBERS_REGEX, password)):
        errors.append(ERROR_MESSAGES['NUMBERS'])

    if not bool(re.search(CAPITAL_LETTER_REGEX, password)):
        errors.append(ERROR_MESSAGES['CAPITAL'])

    if not bool(re.search(SPECIAL_CHAR_REGEX, password)):
        errors.append(ERROR_MESSAGES['SPECIAL'])

    return (len(errors) == 0, errors)
