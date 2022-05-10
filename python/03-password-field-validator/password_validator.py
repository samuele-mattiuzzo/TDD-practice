import re

ERROR_MESSAGES = {
    'LENGTH': 'Password must be at least 8 characters',
    'NUMBERS': 'Password must contain at least 2 numbers',
    'CAPITAL': 'Password must contain at least one capital letter',
    'SPECIAL': 'Password must contain at least one special character'
}

VALID_PASSWORD_LENGTH = 8
NUMBERS_REGEX = r'\d.*\d'
CAPITAL_REGEX = r'[A-Z]'
SPECIAL_REGEX = r'[^a-zA-Z\d]'


def password_validator(password):
    errors = []

    if len(password) < VALID_PASSWORD_LENGTH:
        errors.append(ERROR_MESSAGES['LENGTH'])

    if not bool(re.search(NUMBERS_REGEX, password)):
        errors.append(ERROR_MESSAGES['NUMBERS'])

    if not bool(re.search(CAPITAL_REGEX, password)):
        errors.append(ERROR_MESSAGES['CAPITAL'])

    if not bool(re.search(SPECIAL_REGEX, password)):
        errors.append(ERROR_MESSAGES['SPECIAL'])

    return (len(errors) == 0, errors)
